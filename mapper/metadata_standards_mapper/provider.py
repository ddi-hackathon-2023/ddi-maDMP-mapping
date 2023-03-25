from injector import Module, provider, singleton

from common_utils.dsu.dsu_service import DSUService
from mapper.metadata_standards_mapper.settings_dto import MetadataStandardsSettings
from mapper.metadata_standards_mapper.metadata_standards_mapping_service import MetadataStandardsMappingService


class MetadataStandardsMappingServiceProvider(Module):

    def __init__(self, metadata_standards_settings: MetadataStandardsSettings) -> None:
        self.metadata_standards_settings = metadata_standards_settings

    @provider
    @singleton
    def provide_oai_pmh_mapping_service(self, dsu_service: DSUService) -> MetadataStandardsMappingService:
        metadata_standards_mapping_service = MetadataStandardsMappingService(self.metadata_standards_settings, dsu_service)
        metadata_standards_mapping_service.load_mapping_schemas(self.metadata_standards_settings.METADATA_MAPPING_SCHEMA_PACKAGE)
        return metadata_standards_mapping_service
