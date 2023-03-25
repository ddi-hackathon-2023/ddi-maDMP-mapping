from typing import Dict

from importlib.resources import contents, read_text
from json import loads

from dacite import from_dict

from mapper.mapper.dtos import MappingDocumentDTO, MappingNodeDTO
from mapper.mapper.exceptions import DuplicateMappingSchema, MissingMappingSchema


class BaseMappingService:
    _mapping_schemas: Dict[str, MappingDocumentDTO]

    @staticmethod
    def _get_default_attribute_values(node_mappings: MappingNodeDTO) -> Dict[str, str]:
        attributes = {}
        if hasattr(node_mappings, "subNodeAttributes") and node_mappings.subNodeAttributes:
            for attribute in node_mappings.subNodeAttributes:
                if hasattr(attribute, "subDefaultValue") and attribute.subDefaultValue:
                    attributes[attribute.subAttributeName] = attribute.subDefaultValue
        return attributes

    def load_mapping_schemas(self, mapping_schemas_package: str) -> None:
        self._mapping_schemas = dict()
        dir_file_names = contents(mapping_schemas_package)
        schema_file_names = list(filter(lambda el: el.endswith(".json"), dir_file_names))
        for schema_file_name in schema_file_names:
            schema_file = loads(read_text(mapping_schemas_package, schema_file_name))
            schema_dto = from_dict(data_class=MappingDocumentDTO, data=schema_file)
            if schema_dto.subIdentifier not in self._mapping_schemas.keys():
                self._mapping_schemas[schema_dto.subIdentifier] = schema_dto
            else:
                raise DuplicateMappingSchema()

    def get_mapping_schema_by_identifier(self, identifier: str) -> MappingDocumentDTO:
        try:
            return self._mapping_schemas[identifier]
        except KeyError:
            raise MissingMappingSchema()
