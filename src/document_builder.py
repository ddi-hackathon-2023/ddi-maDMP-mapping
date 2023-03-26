import json
from abc import ABC, abstractmethod
from typing import Dict, Optional, Any
from xml.etree.ElementTree import SubElement, Element, ElementTree, tostring

import pandas


class DocumentBuilder(ABC):
    @abstractmethod
    def add_node_to_current_leaf(self, current_node_ref: Optional[Element], node_name: str, attributes: Dict[str, str], value: Optional[Any]=None, is_raw: bool = False) -> Element:
        pass

    @abstractmethod
    def add_node_to_current_leaf(self, current_node_ref: Optional[Element], node_name: str, attributes: Dict[str, str], value: Optional[Any] = None, is_raw: bool = False) -> Element:
        pass

    @abstractmethod
    def get_document_as_string(self) -> str:
        pass

    @abstractmethod
    def get_document_as_raw(self) -> Optional[Element]:
        pass


class DocumentReader(ABC):
    @abstractmethod
    def get_flattened_tree(self) -> Dict[str, Any]:
        pass


class JSONDocumentReader(DocumentReader):

    def __init__(self, file_path: str) -> None:
        self.json_doc_tree = pandas.read_json(file_path).to_dict(orient="dict")
        self.json_doc_flat = pandas.json_normalize(self.json_doc_tree, sep='/').to_dict(orient="records").pop()


    def get_flattened_tree(self) -> Dict[str, Any]:
        pass
        # df = pandas.json_normalize(self.json_doc, sep='/')
        #
        # return {element. for element in df.to_dict(orient="records")}
        #
        # print(df.to_dict(orient='records')[0])



class XMLDocumentBuilder(DocumentBuilder):

    def __init__(self, file_path: str, encoding: str, with_xml_declaration: bool = False) -> None:
        self.encoding: str = encoding
        self.with_xml_declaration: bool = with_xml_declaration
        self.et: Optional[ElementTree] = None
        self.root_node: Optional[Element] = None

    def add_node_to_current_leaf(self, current_node_ref: Optional[Element], node_name: str, attributes: Dict[str, str], value=None, is_raw: bool = False):
        if current_node_ref is None:
            current_node_ref = Element(node_name, attrib=attributes)
            self.root_node = current_node_ref
            self.et = ElementTree(self.root_node)
        else:
            current_node_ref = SubElement(current_node_ref, node_name, attrib=attributes)
        if is_raw:
            current_node_ref.append(value)
        else:
            current_node_ref.text = value
        return current_node_ref

    def get_document_as_string(self) -> str:
        return tostring(self.root_node, self.encoding, method="xml", xml_declaration=self.with_xml_declaration)  # type: ignore

    def get_document_as_raw(self) -> Optional[Element]:
        return self.root_node
