from dataclasses import dataclass


@dataclass
class MetadataStandardsSettings:
    DOI_PROXY: str = "https://proxy.mock"
    METADATA_MAPPING_SCHEMA_PACKAGE: str = "mapper.metadata_standards_mapper.mappings"
