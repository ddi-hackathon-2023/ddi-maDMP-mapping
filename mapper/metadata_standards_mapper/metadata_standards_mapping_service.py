from typing import List, Dict, Optional, Any

import logging

from common_utils.common_utils.utils import filter_obj_list_by_value, get_iso_8601_date_formatted_with_z
from common_utils.dsu.dsu_service import DSUService
from mapper.mapper.dtos import MappingNodeDTO
from mapper.mapper.base_mapping_service import BaseMappingService
from mapper.mapper.dtos import NodeContentDTO
from mapper.metadata_standards_mapper.exceptions import MissingFieldPath
from mapper.metadata_standards_mapper.settings_dto import MetadataStandardsSettings
from mapper.metadata_standards_mapper.dtos import DatasetMetadataDTO


class MetadataStandardsMappingService(BaseMappingService):

    def __init__(self, metadata_standards_settings: MetadataStandardsSettings,
                 dsu_service: DSUService):
        self.logger = logging.getLogger(__name__)
        self.logger.info("Creating instance of MetadataStandardsMappingService")
        self.metadata_standards_settings = metadata_standards_settings
        self.dsu_service = dsu_service

    @staticmethod
    def _get_sub_field_value(field_path: str, node_data: DatasetMetadataDTO) -> Any:
        field_names = field_path.split("/")
        cur_field_value = node_data
        for field_name in field_names:
            cur_field_value = getattr(cur_field_value, field_name) if hasattr(cur_field_value, field_name) else []

        return cur_field_value

    @staticmethod
    def _get_sub_dynamic_field_value(field_path: str, dynamic_field_content: Dict) -> Any:
        field_names = field_path.split("/")
        cur_field_value = dynamic_field_content
        for field_name in field_names:
            cur_field_value = cur_field_value[field_name] if field_name in cur_field_value else []

        return cur_field_value

    def get_main_translation(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> NodeContentDTO:
        language_field_path = node_mappings.subTargetFields["languagePath"]     # type: ignore
        translations_field_path = node_mappings.subTargetFields["translationsPath"]     # type: ignore
        metadata_language_code = self._get_sub_field_value(language_field_path, node_data)
        translations = self._get_sub_field_value(translations_field_path, node_data)
        main_translation = filter_obj_list_by_value(translations, metadata_language_code, "languageCode")

        if main_translation:
            return NodeContentDTO(nodeValue=main_translation.translation, attributeValues={"xml:lang": main_translation.languageCode})
        else:
            return NodeContentDTO(nodeValue="", attributeValues={})

    def get_additional_translations(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []
        language_field_path = node_mappings.subTargetFields["languagePath"]     # type: ignore
        translations_field_path = node_mappings.subTargetFields["translationsPath"]     # type: ignore
        metata_language_code = self._get_sub_field_value(language_field_path, node_data)
        translations = self._get_sub_field_value(translations_field_path, node_data)

        for translation in translations:
            if translation.languageCode != metata_language_code:
                node_content_dtos.append(NodeContentDTO(nodeValue=translation.translation, attributeValues={"xml:lang": translation.languageCode}))

        return node_content_dtos

    def get_all_translations(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []
        translations_field_path = node_mappings.subTargetFields["translationsPath"]     # type: ignore
        translations = self._get_sub_field_value(translations_field_path, node_data)

        for translation in translations:
            node_content_dtos.append(NodeContentDTO(nodeValue=translation.translation, attributeValues={"xml:lang": translation.languageCode}))

        return node_content_dtos

    def get_internal_identifier(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> NodeContentDTO:
        internal_identifier = "{}-{}-{}".format(node_data.datasetReferenceNumber, node_data.datasetVersionNumber, node_data.datasetRevisionNumber)
        return NodeContentDTO(nodeValue=internal_identifier, attributeValues=self._get_default_attribute_values(node_mappings))

    def get_field_value(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> Optional[NodeContentDTO]:
        try:
            field_path = node_mappings.subTargetFields["fieldPath"]     # type: ignore
        except (KeyError, TypeError):
            raise MissingFieldPath()
        field_value = self._get_sub_field_value(field_path, node_data)
        if field_value:
            return NodeContentDTO(nodeValue=field_value, attributeValues=self._get_default_attribute_values(node_mappings))
        else:
            return None

    def get_doi(self, method_args: List[str], node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> NodeContentDTO:
        attributes = self._get_default_attribute_values(node_mappings)
        attributes["URI"] = "{}/{}".format(getattr(self.metadata_standards_settings, method_args.pop()), node_data.doi)
        return NodeContentDTO(nodeValue="", attributeValues=attributes)

    def get_dynamic_field_translations(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []
        dynamic_field_path = node_mappings.subTargetFields["fieldPath"]     # type: ignore
        dynamic_field_dto_list = self._get_sub_field_value(dynamic_field_path, node_data)
        if dynamic_field_dto_list:
            dynamic_field_dto = filter_obj_list_by_value(dynamic_field_dto_list, node_mappings.subTargetDynamicConfig["configBlockId"], "configBlockId")    # type: ignore
            dynamic_field = self._get_sub_dynamic_field_value(node_mappings.subTargetDynamicConfig["dynamicPath"], dynamic_field_dto.jsonBlock)     # type: ignore

            if dynamic_field:
                for locale_code, translation in dynamic_field["translations"].items():
                    node_content_dtos.append(NodeContentDTO(nodeValue=translation, attributeValues={"xml:lang": locale_code}))

        return node_content_dtos

    @staticmethod
    def get_PIs(node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []

        for author in node_data.authors:
            if author.role.code == "principal-investigator":
                concat_name = "{}, {}".format(author.lastName, author.firstName)
                node_content_dtos.append(NodeContentDTO(nodeValue=concat_name, attributeValues=None))

        return node_content_dtos

    def get_publisher(self, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []

        dsu_names = self.dsu_service.dsu_by_discipline_id(node_data.disciplineId).dsu_config.names
        for languageCode, translation in dsu_names.items():
            node_content_dtos.append(NodeContentDTO(nodeValue=translation, attributeValues={"xml:lang": languageCode}))

        return node_content_dtos

    @staticmethod
    def get_publication_date(node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> NodeContentDTO:
        publication_year = str(node_data.publicationDate.year)
        iso_date = get_iso_8601_date_formatted_with_z(node_data.publicationDate)
        return NodeContentDTO(nodeValue=publication_year, attributeValues={"date": iso_date})

    def get_element_translation(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []
        element_path = node_mappings.subTargetFields["element"]     # type: ignore
        element_value = self._get_sub_field_value(element_path, node_data)

        for translation in element_value.translations:
            node_content_dtos.append(NodeContentDTO(nodeValue=translation.translation, attributeValues={"xml:lang": translation.languageCode}))

        return node_content_dtos

    def get_elements_translation(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []
        elements_path = node_mappings.subTargetFields["elements"]     # type: ignore
        element_values = self._get_sub_field_value(elements_path, node_data)

        if element_values:
            for element_value in element_values:
                for translation in element_value.translations:
                    node_content_dtos.append(NodeContentDTO(nodeValue=translation.translation, attributeValues={"xml:lang": translation.languageCode}))

        return node_content_dtos

    def get_file_names(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> List[NodeContentDTO]:
        node_content_dtos: List[NodeContentDTO] = []
        object_list_path = node_mappings.subTargetFields["objectListPath"]     # type: ignore
        object_values = self._get_sub_field_value(object_list_path, node_data)

        for object_value in object_values:
            field_path = node_mappings.subTargetFields["fieldPath"]  # type: ignore
            field_value = self._get_sub_field_value(field_path, object_value)
            node_content_dtos.append(NodeContentDTO(nodeValue=field_value, attributeValues={"xml:lang": node_data.language.code}))

        return node_content_dtos

    def get_language_code(self, node_mappings: MappingNodeDTO, node_data: DatasetMetadataDTO, **kwargs: Dict[str, Any]) -> DatasetMetadataDTO:
        attributes = self._get_default_attribute_values(node_mappings)
        attributes["xml:lang"] = node_data.language.code
        setattr(node_data, "attributeValues", attributes)
        return node_data
