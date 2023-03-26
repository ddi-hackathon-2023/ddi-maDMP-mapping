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
