from dataclasses import dataclass


@dataclass
class SSSOMOtherField:
    subject_cardinality: str
    subject_type: str
    object_cardinality: str
    object_type: str
