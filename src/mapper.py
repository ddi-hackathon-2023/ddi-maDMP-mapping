from sssom.parsers import parse_sssom_table

from dto import SSSOMOtherField
from src.document_builder import DocumentBuilder, DocumentReader
from pathlib import Path

from src.solver import cardinality_type_solver

from pprint import pprint


class SSSOMMapper:
    def __init__(self, subject_document: DocumentReader, object_document: DocumentBuilder, sssom_mapping_set_tsv: str) -> None:
        self._load_mapping_set_def(sssom_mapping_set_tsv)
        self.subject_document = subject_document
        self.object_document = object_document

    def _load_mapping_set_def(self, sssom_mapping_set_tsv: str):
        self.input_msdf = parse_sssom_table(sssom_mapping_set_tsv)
        self.mappings = self.input_msdf.df.to_dict(orient="records")
        self.mappings = sorted(self.mappings, key=lambda x: Path(x["object_id"]))

    @staticmethod
    def _other_field_parser(sssom_mapping_other_field: str):
        keys_to_values = {}
        for key_value in sssom_mapping_other_field.split("|"):
            key, value = key_value.split(":")
            keys_to_values[key] = value
        return SSSOMOtherField(**keys_to_values)

    def convert(self):
        flat_subject_document = self.subject_document.get_flattened_tree()
<<<<<<< HEAD
        current_node = None
        for mapping_index, current_mapping in enumerate(self.mappings):
            object_id = current_mapping["object_id"]
            subject_id = current_mapping["subject_id"]
            subject_path = subject_id[1:]  # remove / at the beginning

            subject_value = recursive_subject_reader(flat_subject_document, subject_path)

            current_node, object_path = self.object_document.find(object_id)
            if current_node is None or not object_path:
                current_node = self.object_document.get_document_as_raw()
                for node_name in object_path.split("/"):
                    current_node = self.object_document.add_node_to_current_leaf(
                                current_node_ref=current_node, node_name=node_name, value=None, attributes={}
                            )
            if current_node is not None:
                if "@" in object_id:
                    _, attribute_name = object_id.split("@")
                    self.object_document.add_attribute_to_current_leaf(current_node, attribute_name, subject_value)
                elif object_id.endswith("/text()"):
                    self.object_document.set_value_of_current_leaf(current_node, subject_value)

            # TODO: remove this, dev help
            # try:
            #     pprint(self.object_document.get_document_as_string())
            # except:
            #     pass


def recursive_subject_reader(flat_subject_document, subject_path, current_index=0):
    if subject_path in flat_subject_document:
        return flat_subject_document[subject_path]
    parent_subject_path = subject_path.rsplit("/", 1).pop(0)
    while "/" in parent_subject_path:
        if parent_subject_path in flat_subject_document:
            break
        parent_subject_path = parent_subject_path.rsplit("/", 1).pop(0)
    if parent_subject_path not in flat_subject_document:
        for key in flat_subject_document.keys():
            if subject_path in key:
                return None
        raise ValueError
    partial_subject_document = flat_subject_document[parent_subject_path]
    partial_subject_path = subject_path[len(parent_subject_path)+1:]
    if isinstance(partial_subject_document, list):
        return recursive_subject_reader(partial_subject_document[current_index], partial_subject_path)
    return recursive_subject_reader(partial_subject_document, partial_subject_path)
=======
        for mapping in self.mappings:
            object_id = mapping["object_id"]
            subject_id = mapping["subject_id"]
            other_field = self._other_field_parser(mapping["other"])
            value = None
            try:
                func = cardinality_type_solver(other_field)
                value = func(flat_subject_document[subject_id[1:]])
            except KeyError:
                if other_field.subject_cardinality[0] != "0":
                    raise ValueError(f"This subject path {subject_id} is mandatory in the input format but not present!")
                elif other_field.object_cardinality[0] != "0":
                    raise ValueError(f"This object path {object_id} is mandatory for the output file!")
            node_name, attribute = object_id.rsplit("/", 1)
            self.object_document.add_node_to_current_leaf(current_node_ref=None, node_name=node_name, attributes={attribute: value})
        pprint(self.object_document.get_document_as_string())
>>>>>>> parent of 22f36d6 (Minimal naive working version, not using solver)
