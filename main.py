import sys
from itertools import combinations_with_replacement, product
from pathlib import Path

from mapper import SSSOMMapper
from src.document_builder import XMLDocumentBuilder, JSONDocumentReader

def get_combi():
    cardinalities = ["0..1", "1", "0..n", "1..n", "n..n"]
    types = ["literal", "voc", "object", "list"]

    cardinalities_combos = list(combinations_with_replacement(cardinalities, 2))
    types_combos = list(combinations_with_replacement(types, 2))
    return [[(c_1, t_1, c_2, t_2) for t_1, t_2 in types_combos] for c_1, c_2 in cardinalities_combos ]


def main():
    args = sys.argv
    # input_subject_path = args[0]
    # input_mapping_dir = args[1]
    # output_file_path = args[2]
    input_subject_path = "exemples/madmp/ex1-header-fundedProject.json"
    input_mapping_tsv = "mapping_definitions/dmp-ddi25_mapping.tsv"
    output_file_path = "mapping_definitions/output.xml"

    print(get_combi())

    # hardcoded for now, could be chosen by suffix / config
    ddi25_document_output = XMLDocumentBuilder(output_file_path, "UTF-8", True)
    dmp_document_input = JSONDocumentReader(input_subject_path)

    mapper = SSSOMMapper(dmp_document_input, ddi25_document_output, input_mapping_tsv)
    mapper.convert()

if __name__ == "__main__":
    main()
