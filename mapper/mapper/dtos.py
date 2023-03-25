from dataclasses import dataclass
from typing import List, Dict, Optional, Any


@dataclass
class MappingDataDTO:
    pass


@dataclass
class NodeAttributeDTO:
    attributeName: str
    attributeValue: List[str]


@dataclass
class NodeContentDTO(MappingDataDTO):
    nodeValue: Optional[Any]
    attributeValues: Optional[Dict[str, str]]
    isRaw: bool = False


@dataclass
class AttributeMappingDTO:
    subAttributeName: str
    subDefaultValue: Optional[str]
    subRequired: Optional[bool]


@dataclass
class MappingNodeDTO:
    type: str
    required: Optional[List[str]]
    properties: Optional[Dict[str, 'MappingNodeDTO']]
    items: Optional['MappingNodeDTO']
    subNodePath: Optional[str]
    subNodeAttributes: Optional[List[AttributeMappingDTO]]
    subTargetFields: Optional[Dict[str, str]]
    subTargetDynamicConfig: Optional[Dict[str, Any]]
    subCallbackMethod: Optional[List[str]]
    subNodeDefaultValue: Optional[str]


@dataclass
class MappingDocumentDTO(MappingNodeDTO):
    title: str
    subTargetSchema: str
    subTargetSchemaNamespace: str
    subTargetSchemaNotes: Optional[str]
    subMappingsVersion: str
    subIdentifier: str
