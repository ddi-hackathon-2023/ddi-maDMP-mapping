import sys

from mapper import SSSOMMapper
from document_builder import XMLDocumentBuilder, JSONDocumentReader


def main():
    args = sys.argv
    # input_subject_path = args[0]
    # input_mapping_dir = args[1]
    # output_file_path = args[2]
    input_subject_path = "exemples/madmp/ex1-header-fundedProject.json"
    input_mapping_tsv = "mapping_definitions/dmp-ddi25_mapping.tsv"
    output_file_path = "mapping_definitions/output.xml"


    # hardcoded for now, could be chosen by suffix / config
    ddi25_document_output = XMLDocumentBuilder(output_file_path, "UTF-8", True)
    dmp_document_input = JSONDocumentReader(input_subject_path)

    mapper = SSSOMMapper(dmp_document_input, ddi25_document_output, input_mapping_tsv)
    mapper.convert()
    print(mapper.object_document.get_document_as_string())


if __name__ == "__main__":
    main()
