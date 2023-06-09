from abc import ABC, abstractmethod
from typing import Dict, Optional, Any
from xml.etree.ElementTree import SubElement, Element, ElementTree, tostring
from xml.dom import minidom

import pandas


class DocumentBuilder(ABC):

    @abstractmethod
    def add_node_to_current_leaf(self, current_node_ref: Optional[Element], node_name: str, attributes: Dict[str, str], value: Optional[Any]=None, is_raw: bool = False) -> Element:
        raise NotImplementedError

    @abstractmethod
    def add_attribute_to_current_leaf(self, current_node_ref: Optional[Element], node_name: str, attributes: Dict[str, str], value: Optional[Any]=None, is_raw: bool = False) -> Element:
        raise NotImplementedError

    @abstractmethod
    def set_value_of_current_leaf(self, current_node_ref: Element, value) -> Element:
        raise NotImplementedError

    @abstractmethod
    def get_document_as_string(self) -> str:
        raise NotImplementedError

    @abstractmethod
    def get_document_as_raw(self) -> Optional[Element]:
        raise NotImplementedError


class DocumentReader(ABC):
    @abstractmethod
    def get_flattened_tree(self) -> Dict[str, Any]:
        raise NotImplementedError


class JSONDocumentReader(DocumentReader):

    def __init__(self, file_path: str) -> None:
        self.json_doc_tree = pandas.read_json(file_path).to_dict(orient="dict")
        self.json_doc_flat = pandas.json_normalize(self.json_doc_tree, sep='/').to_dict(orient="records").pop()

    def get_flattened_tree(self) -> Dict[str, Any]:
        return self.json_doc_flat


class XMLDocumentBuilder(DocumentBuilder):

    def __init__(self, file_path: str, encoding: str, with_xml_declaration: bool = False) -> None:
        self.encoding: str = encoding
        self.with_xml_declaration: bool = with_xml_declaration
        self.et: Optional[ElementTree] = None
        self.root_node: Optional[Element] = None

    def get_document_as_string(self) -> str:
        xml_string = tostring(self.root_node, "unicode", method="xml", xml_declaration=self.with_xml_declaration)
        return minidom.parseString(xml_string).toprettyxml(indent="   ")

    def get_document_as_raw(self) -> Optional[Element]:
        return self.root_node

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

    def add_attribute_to_current_leaf(self, current_node_ref: Element, attribute_name, attribute_value) -> Element:
        current_node_ref.attrib.update({attribute_name: attribute_value})
        return current_node_ref

    def set_value_of_current_leaf(self, current_node_ref: Element, value) -> Element:
        current_node_ref.text = value
        return current_node_ref

    def find(self, full_xpath) -> Optional[Element]:
        # TODO: extend to be able to handle namespaces also
        search_path = full_xpath.strip("/").replace("/text()", "").split("@").pop(0)
        if not self.root_node:
            return None, search_path
        root_tag = self.root_node.tag
        # remove start and end slashes text and attributes from node path
        existing_path = ""
        if search_path.startswith(root_tag):
            search_path = search_path[len(root_tag):]
            existing_path = root_tag
        node = self.et.find(f"./{search_path}")
        if node is not None:
            return node, ""
        current_node = None
        current_nodes = [self.root_node]
        current_path = ""
        for path in search_path.split("/"):
            current_names = [node.tag for node in current_nodes]
            if path in current_names:
                current_path += path + "/"
                current_node = current_nodes[current_names.index(path)]
                current_nodes = [current_node.getchildren()]
            else:
                return current_node, search_path[len(current_path)+1:]
