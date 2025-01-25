import json
import os
import pkgutil
import re
from copy import copy
from datetime import date
from pathlib import Path
from pprint import pprint
from typing import Optional

import pandas as pd
import wikipediaapi
from deepdiff import DeepDiff


def _scrape_sessions_from_wiki_class(root_section):
    if root_section.sections:
        return {
            deeper_section.title: _scrape_sessions_from_wiki_class(deeper_section)
            for deeper_section in root_section.sections
        }
    else:
        return root_section.title


def _define_depth_for_every_subfield(rem_section, rem_section_data, previous_subsection):
    current_subsections = previous_subsection[rem_section]

    subsections, substructures = {}, []
    for i, data in enumerate(rem_section_data, start=1):
        if isinstance(data, dict):
            subsections.update(data)
        elif data in current_subsections:
            subsections[data] = _define_depth_for_every_subfield(data, rem_section_data[i:], current_subsections)
        else:
            substructures.append(data)

    if subsections:
        subsections["Substructures"] = substructures
        return subsections
    return substructures


def scrape_human_brain_tree() -> dict:
    def recursive_set_adder(data_to_add):
        if isinstance(data_to_add, str):
            flattened_structure_dataset.add(data_to_add.capitalize())
        elif isinstance(data_to_add, dict):
            for subsection_name, recursive_subsection in data_to_add.items():
                if any(recursive_data.isdigit() for recursive_data in recursive_subsection):
                    for daughter_tag in recursive_subsection:
                        flattened_structure_dataset.add(f"{subsection_name} {daughter_tag}")
                else:
                    recursive_set_adder(recursive_subsection)
        else:
            for recursive_data in data_to_add:
                recursive_set_adder(recursive_data)

    deli = re.compile(r"[,;]")
    parenthesis_exp = re.compile(r"\([\w,; ]*\)")
    id_followed_by_numbering = re.compile(r"^[\w ]* \d+")

    wiki_api = wikipediaapi.Wikipedia(language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)

    wiki_page = wiki_api.page("List_of_regions_in_the_human_brain")

    section_titles = {}
    for section in wiki_page.sections:
        section_titles[section.title] = _scrape_sessions_from_wiki_class(section)

    data = {}
    section_data = []
    section = None
    for line in wiki_page.text.splitlines():
        if "Related topics" in line:
            break

        if not line or (":" not in line and len(line.split(" ")) >= 15):
            continue
        elif line in section_titles:
            if section:
                data[section] = copy(section_data)
                section_data = []
            section = line
        else:
            assert section
            if (parenthesis_exp_findings := re.findall(parenthesis_exp, line)) and len(parenthesis_exp_findings) == 1:
                split_line = re.split(parenthesis_exp, line)
                if len(split_line) == 2:
                    if not split_line[1]:
                        section_data.append(line.strip())
                        continue

            if " and " in line.lower():
                section_data.append(line)
            elif re.findall(deli, line):
                split_line = tuple(map(str.strip, re.split(deli, line)))
                if id_number := re.findall(id_followed_by_numbering, line):
                    split_id_number = id_number[0].split(" ")
                    parent = " ".join(split_id_number[:-1])
                    first_id = split_id_number[-1]
                    for idx, chunk in enumerate(split_line):
                        if first_id in chunk:
                            daughters = (
                                [first_id, *split_line[idx + 1 :]]
                                if "(" not in chunk
                                else [
                                    f"{first_id} {parenthesis_exp_findings[0]}",
                                    *split_line[idx + 2 :],
                                ]
                            )
                            break
                else:
                    parent, daughters = split_line[0], split_line[1:]
                if ":" in parent:
                    parent_split = parent.split(":")
                    if len(parent_split) != 1:
                        assert len(parent_split) == 2, len(parent_split)
                        parent = parent_split[0].strip()
                        if parent_split[1]:
                            daughters = [parent_split[1].strip(), *daughters]
                    else:
                        parent = parent.replace(":", "")

                # section_data.append({parent: [daughter for daughter in daughters if daughter.lower() == "other"]})
                section_data.append({parent: daughters})
            else:
                section_data.append(line)

    data_with_depth = {}
    for section, section_data in data.items():
        data_with_depth[section] = _define_depth_for_every_subfield(section, section_data, section_titles)

    organized_data = {"neuronal_structure": {}}
    for section_name, data in data_with_depth.items():
        if "Neurotransmitter pathways" == section_name:
            organized_data["neurotransmitter"] = data
        elif "Neural pathways" == section_name:
            organized_data["neuronal_pathway"] = data
        else:
            organized_data["neuronal_structure"][section_name] = data

    organized_data["neuro_endocrine_system"] = organized_data["neuronal_structure"].pop("Neuro endocrine systems")
    organized_data["neuro_vascular_system"] = organized_data["neuronal_structure"].pop("Neuro vascular systems")
    organized_data["dural_meningeal_system"] = organized_data["neuronal_structure"].pop("Dural meningeal system")

    flattened_structure_dataset = set()

    for subsection in organized_data["neuronal_structure"].values():
        recursive_set_adder(subsection)

    flattened_structure_dataset.remove("Surface")  # Absurd brain structure.
    flattened_structure_dataset = list(sorted(flattened_structure_dataset))

    standard_name_to_names = {}
    for names in flattened_structure_dataset:
        parenthesis_content = parenthesis_exp.findall(names)
        if not parenthesis_content:
            continue

        parenthesis_content = parenthesis_content[0][1:-1].strip()
        standard_name = names.split("(")[0].strip().lower()
        if "," in parenthesis_content:
            iterable = sorted(parenthesis_content.split(","))
        elif "and" in parenthesis_content:
            iterable = sorted(parenthesis_content.split("and"))
        else:
            iterable = (parenthesis_content,)
        [name.replace("also", "").strip().lower() for name in iterable if len(name) > 3]
        standard_name_to_names[names] = (standard_name, *iterable)

    organized_data["neuronal_structure_flat"] = flattened_structure_dataset
    organized_data["standard_name_to_names"] = dict(sorted(standard_name_to_names.items()))
    organized_data = dict(sorted(organized_data.items()))

    return organized_data


def scrape_neurotransmitter() -> dict:
    standard_neurotransmitter_names, neurotransmitter_with_alternative_names = [], []
    for row in pd.read_excel(pkgutil.get_data(__name__, "wikipedia_table.ods")).iterrows():
        row = row[1]
        name, abbreviation = row[1:3]

        name = name.strip().replace("\xa0", " ")
        if "(" in name:
            name, alternative_name = name.split("(")
            name = name.strip()
            alternative_name = alternative_name.strip(") ")
        else:
            alternative_name = None

        standard_neurotransmitter_names.append(name.lower().replace(" ", "_"))

        if isinstance(abbreviation, float):  # abbreviation is nan
            names = name
        else:
            abbreviation = abbreviation.strip().replace("\xa0", " ")
            names = f"{name}; {abbreviation}"
        if alternative_name:
            names += f"; {alternative_name}"

        neurotransmitter_with_alternative_names.append(names)

    return dict(zip(standard_neurotransmitter_names, neurotransmitter_with_alternative_names))


def scrape_model_organism() -> dict:
    def section_unpacker(recursive_section, current_dict: Optional[dict] = None):
        unpacked_data = current_dict or {}
        if recursive_section.text:
            for line in recursive_section.text.split("\n"):
                processed_line = line.split(",")[0].strip()

                if not processed_line or "References" in processed_line or ":" in processed_line:
                    continue

                parenthesis_split = processed_line.split(" (")
                scientific_names = parenthesis_split[0].strip()
                try:
                    cultural_name = parenthesis_split[1].replace(")", "").strip().capitalize()
                except IndexError:
                    # No cultural name defined
                    cultural_name = ""

                for species_name in scientific_names.split(" and "):
                    unpacked_data[species_name.capitalize()] = cultural_name

        else:
            for sub_section in recursive_section.sections:
                unpacked_data = section_unpacker(sub_section, unpacked_data)

        return unpacked_data

    wiki_api = wikipediaapi.Wikipedia(language="en", extract_format=wikipediaapi.ExtractFormat.WIKI)
    wiki_page = wiki_api.page("List_of_model_organisms")

    result = {}
    for section in wiki_page.sections:
        if "Eukaryotes" == section.title:
            for eu_section in section.sections:
                result[eu_section.title] = section_unpacker(section)
        else:
            result[section.title] = section_unpacker(section)

    return result


def save_all(output_directory: Path, make_directories: bool = False) -> None:
    datasets = {
        "scrape_human_brain_tree": scrape_human_brain_tree(),
        "scrape_model_organism": scrape_model_organism(),
        "neurotransmitter": scrape_neurotransmitter(),
    }
    for dataset_label, dataset in datasets.items():
        print(f"Saving {dataset_label} dataset")
        dataset_dir = output_directory / dataset_label
        if make_directories:
            os.mkdir(dataset_dir)

        try:
            latest_dataset_filename = str(os.listdir(dataset_dir)[-1])
        except IndexError:
            latest_dataset_filename = None

        if latest_dataset_filename:
            assert latest_dataset_filename.startswith(
                dataset_label
            ), f"dataset_label={dataset_label}, should be at the start of the filename"

            with open(dataset_dir / latest_dataset_filename, "rb") as in_json:
                latest_dataset = json.load(in_json)

            difference = DeepDiff(dataset, latest_dataset, ignore_order=True)
            difference.pop("type_changes", None)
            if not difference:
                return print("Done: No change in data since last save, nothing new to store")

            print("Difference:")
            pprint(difference, indent=2, width=200)

        new_dataset_filename = dataset_dir / f"{dataset_label}_{date.today()}.json"
        with open(new_dataset_filename, "w") as out_json:
            json.dump(dataset, out_json)

        print(f"Done: New dataset saved to {new_dataset_filename}\n\n")
