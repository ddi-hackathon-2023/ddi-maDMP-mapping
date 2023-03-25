from xml.etree.ElementTree import Element

from typing import List, Any, Optional, Union, Iterable

from common_utils.common_utils.dispatcher import Dispatcher, DispatcherNoSuchCallback

from mapper.mapper.dtos import MappingDocumentDTO, MappingNodeDTO
from mapper.mapper.document_builder import DocumentBuilder
from mapper.mapper.dtos import MappingDataDTO, NodeContentDTO
from mapper.mapper.exceptions import MissingDefaultValue, NotAnArray, MissingMappingMethod


class DynamicMapper:
    dispatcher: Dispatcher
    document_builder: DocumentBuilder

    def __init__(self, dispatcher: Dispatcher, document_builder: DocumentBuilder) -> None:
        self.dispatcher = dispatcher
        self.document_builder = document_builder

    @staticmethod
    def _get_child_nodes(node_mappings: MappingNodeDTO) -> List[MappingNodeDTO]:
        child_nodes: List = []

        if not (hasattr(node_mappings, "properties") and node_mappings.properties):
            return child_nodes

        for key, value in node_mappings.properties.items():
            child_nodes.append(value)

        return child_nodes

    def _add_node_hierarchy(self, current_node_ref: Optional[Element], node_mappings: MappingNodeDTO, node_data: NodeContentDTO) -> Optional[Element]:
        if node_mappings.subNodePath:
            attribute_values = dict()
            node_value: str = ""
            is_raw: bool = False
            node_path_hiercharchy = node_mappings.subNodePath.split("/")
            last_path = node_path_hiercharchy.pop() # Only leaf node will get attributes. Upper nodes are just containers

            for current_path in node_path_hiercharchy:
                current_node_ref = self.document_builder.add_node_to_current_leaf(current_node_ref, current_path, {})

            if hasattr(node_data, "attributeValues") and node_data.attributeValues:
                attribute_values = node_data.attributeValues

            if hasattr(node_data, "nodeValue") and node_data.nodeValue is not None:
                node_value = node_data.nodeValue

            if hasattr(node_data, "isRaw") and node_data.isRaw:
                is_raw = node_data.isRaw

            return self.document_builder.add_node_to_current_leaf(current_node_ref, last_path, attribute_values, node_value, is_raw)
        return None

    @staticmethod
    def _get_default_node_value(node_mappings: MappingNodeDTO) -> NodeContentDTO:
        if node_mappings.subNodeDefaultValue is None:
            raise MissingDefaultValue()
        return NodeContentDTO(nodeValue=node_mappings.subNodeDefaultValue, attributeValues=dict())

    @staticmethod
    def _add_default_attribute_values(node_mappings: MappingNodeDTO, node_data: NodeContentDTO) -> None:
        if hasattr(node_mappings, "subNodeAttributes") and node_mappings.subNodeAttributes:
            if not node_data.attributeValues:
                node_data.attributeValues = {}
            for attribute in node_mappings.subNodeAttributes:
                if hasattr(attribute, "subDefaultValue") and attribute.subDefaultValue:
                    node_data.attributeValues[attribute.subAttributeName] = attribute.subDefaultValue

    def _execute_mapping_method(self, method_name_and_args: List[str], root_data_tree: MappingDataDTO, node_mappings: MappingNodeDTO, node_data: MappingDataDTO) -> Any:
        method_name = method_name_and_args[0]
        method_args = method_name_and_args[1:]
        try:
            return self.dispatcher.execute_callback(method_name, method_args=method_args, root_data_tree=root_data_tree, node_mappings=node_mappings, node_data=node_data)
        except DispatcherNoSuchCallback:
            raise MissingMappingMethod()

    def _create_node_and_process_children(self, node_ref: Optional[Element], root_data_tree: MappingDataDTO, node_mappings: MappingNodeDTO,
                      node_data: Any, parent_node_data: Any, child_nodes: List[MappingNodeDTO]) -> None:
        current_node_ref = self._add_node_hierarchy(node_ref, node_mappings, node_data)
        for child_node in child_nodes:
            self._process_mapping_node(current_node_ref, root_data_tree, child_node, parent_node_data)

    def _process_mapping_node(self, current_node_ref: Optional[Element], root_data_tree: MappingDataDTO,
                              current_node_mappings: MappingNodeDTO, parent_node_data: MappingDataDTO) -> None:
        current_node_data: Optional[Union[NodeContentDTO, List[NodeContentDTO]]] = None
        child_nodes = self._get_child_nodes(current_node_mappings)

        if hasattr(current_node_mappings, "subCallbackMethod") and current_node_mappings.subCallbackMethod:
            current_node_data = self._execute_mapping_method(current_node_mappings.subCallbackMethod, root_data_tree, current_node_mappings, parent_node_data)
        elif hasattr(current_node_mappings, "subNodeDefaultValue") and current_node_mappings.subNodeDefaultValue:
            current_node_data = self._get_default_node_value(current_node_mappings)

        # todo: validation of required attr
        if current_node_mappings.type == "array":
            if isinstance(current_node_data, Iterable):
                parent_node_ref = current_node_ref
                for node_data_item in current_node_data:
                    self._create_node_and_process_children(parent_node_ref, root_data_tree, current_node_mappings, node_data_item, node_data_item, child_nodes)
            else:
                raise NotAnArray()
        else:
            if current_node_data:
                self._create_node_and_process_children(current_node_ref, root_data_tree, current_node_mappings, current_node_data, current_node_data, child_nodes)
            elif child_nodes:   # Default attributes are set for current node and parent data is passed to children
                current_node_data = NodeContentDTO(nodeValue="", attributeValues={})
                self._add_default_attribute_values(current_node_mappings, current_node_data)
                self._create_node_and_process_children(current_node_ref, root_data_tree, current_node_mappings, current_node_data, parent_node_data, child_nodes)

    def generate_document(self, root_data: MappingDataDTO, oai_mapping_schema: MappingDocumentDTO) -> str:
        self._process_mapping_node(None, root_data, oai_mapping_schema, root_data)
        return self.document_builder.get_document_as_string()

    def generate_raw_document(self, root_data: MappingDataDTO, oai_mapping_schema: MappingDocumentDTO) -> Optional[Element]:
        self._process_mapping_node(None, root_data, oai_mapping_schema, root_data)
        return self.document_builder.get_document_as_raw()
