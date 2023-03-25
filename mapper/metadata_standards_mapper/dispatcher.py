from common_utils.common_utils.dispatcher import Dispatcher
from mapper.metadata_standards_mapper.metadata_standards_mapping_service import MetadataStandardsMappingService


class MetadataStandardsDispatcher(Dispatcher):

    def __init__(self, metadata_standards_mapping_service: MetadataStandardsMappingService) -> None:
        self._register_callback("getMainTranslation", metadata_standards_mapping_service.get_main_translation)
        self._register_callback("getAdditionalTranslations", metadata_standards_mapping_service.get_additional_translations)
        self._register_callback("getAllTranslations", metadata_standards_mapping_service.get_all_translations)
        self._register_callback("getInternalIdentifier", metadata_standards_mapping_service.get_internal_identifier)
        self._register_callback("getFieldValue", metadata_standards_mapping_service.get_field_value)
        self._register_callback("getDOI", metadata_standards_mapping_service.get_doi)
        self._register_callback("getDynamicFieldTranslations", metadata_standards_mapping_service.get_dynamic_field_translations)
        self._register_callback("getPIs", metadata_standards_mapping_service.get_PIs)
        self._register_callback("getPublisher", metadata_standards_mapping_service.get_publisher)
        self._register_callback("getPublicationDate", metadata_standards_mapping_service.get_publication_date)
        self._register_callback("getElementTranslation", metadata_standards_mapping_service.get_element_translation)
        self._register_callback("getElementsTranslation", metadata_standards_mapping_service.get_elements_translation)
        self._register_callback("getFileNames", metadata_standards_mapping_service.get_file_names)
        self._register_callback("getLanguageCode", metadata_standards_mapping_service.get_language_code)
