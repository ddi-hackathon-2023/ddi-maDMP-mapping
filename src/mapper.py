from sssom.parsers import parse_sssom_table

from dto import SSSOMOtherField
from src.document_builder import DocumentBuilder, DocumentReader
from pathlib import Path

class SSSOMMapper:
    def __init__(self, subject_document: DocumentReader, object_document: DocumentBuilder, sssom_mapping_set_tsv: str) -> None:
        self._load_mapping_set_def(sssom_mapping_set_tsv)
        self.subject_document = subject_document
        self.object_document = object_document

    def _load_mapping_set_def(self, sssom_mapping_set_tsv: str):
        self.input_msdf = parse_sssom_table(sssom_mapping_set_tsv)
        self.mappings = self.input_msdf.df.to_dict(orient="records")
        self.mappings = sorted(self.mappings, key=lambda x: Path(x["object_id"]))

    def _other_field_parser(self, sssom_mapping_other_field: str):
        things = sssom_mapping_other_field.split("|")
        things = {key: value for thing in things for key, value in thing.split(":")}
        return SSSOMOtherField(**things)

    def _cardinality_type_solver(self, of: SSSOMOtherField):


        pass
        # solver = {
        #     ("0..1", "")
        # }
        # return solver[(of.subject_cardinality, of.subject_type, of.object_cardinality, of.object_type)]

    def convert(self):
        for mapping in self.mappings:
            other_field = self._other_field_parser(mapping["other"])
            pass
