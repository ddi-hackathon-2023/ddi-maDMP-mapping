from abc import ABC, abstractmethod
from typing import Dict, Optional, Any
from lxml.etree import SubElement, Element, ElementTree, tostring

import pandas


class DocumentBuilder(ABC):
    @abstractmethod
    def add_node_to_current_leaf(self, current_node_ref: Optional[Element], node_name: str, attributes: Dict[str, str], value: Optional[Any]=None, is_raw: bool = False) -> Element:
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
        self.json_doc_flat = self._complete_tree(
            pandas.json_normalize(self.json_doc_tree, sep='/').to_dict(orient="records").pop()
        )

    @staticmethod
    def _complete_tree(tree_dict):
        missing_entries = []
        for key in tree_dict.keys():
            previous = ""
            for element in key.split("/"):
                element = previous + "" + element
                if element not in tree_dict.keys():
                    missing_entries.append(element)
                    previous = element + "/"
        for element in missing_entries:
            tree_dict[element] = {}
        return tree_dict


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
        elif node_name:
            current_node_ref = SubElement(current_node_ref, node_name, attrib=attributes)
        if is_raw:
            current_node_ref.append(value)
        else:
            current_node_ref.text = value
        return current_node_ref

    def get_document_as_string(self) -> str:
        return tostring(self.root_node, self.encoding, method="xml", xml_declaration=self.with_xml_declaration)  # type: ignore

    def set_value_of_current_leaf(self, current_node_ref: Element, value) -> Element:
        current_node_ref.text = value
        return current_node_ref

    def find(self, full_xpath) -> Optional[Element]:
        # TODO: extend to be able to handle namespaces also
        search_path = full_xpath.strip("/").replace("/text()", "").split("@").pop(0)
        if self.root_node is None:
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
    def get_document_as_raw(self) -> Optional[Element]:
        return self.root_node
