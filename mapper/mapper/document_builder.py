from abc import ABC, abstractmethod
from typing import Dict, Optional, Any
from xml.etree.ElementTree import SubElement, Element, ElementTree, tostring


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


class XMLDocumentBuilder(DocumentBuilder):

    def __init__(self, encoding: str, with_xml_declaration: bool = False) -> None:
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
