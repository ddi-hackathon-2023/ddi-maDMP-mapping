from datetime import datetime, date
from typing import Dict, List, Optional, Union
from dataclasses import dataclass

from common_utils.common_utils.language_utils import LanguageCode, Locale
from mapper.mapper.dtos import MappingDataDTO

### IMPORTANT ###
# When modifying something here, always make sure that the changes fits the "TopLevelDatasetDoc" defined in the index lib
# Both "TopLevelDatasetDoc" and ""DatasetsMetadataDTO" must always be in sync, since one describes the index, and the other
# the result of a query from that index

@dataclass
class TranslationDTO:
    languageCode: Union[LanguageCode, Locale, str]
    translation: str


@dataclass
class VocElementMappingDTO:
    id: int
    code: str
    translations: List[TranslationDTO]


@dataclass
class AuthorsDTO:
    firstName: str
    lastName: str
    role: VocElementMappingDTO


@dataclass
class DynamicMetadataDTO:
    configBlockId: int
    schemaVersion: str
    jsonBlock: Optional[Dict]


@dataclass
class DataFileMetadataDTO:
    fileDescriptionId: int
    fileReferenceNumber: int
    title: str
    dynamicMetadata: Optional[List[DynamicMetadataDTO]]


@dataclass
class DatasetMetadataDTO(MappingDataDTO):
    createUpdateTimestamp: datetime
    # Study
    studyId: int
    studyVersionId: int
    disciplineId: int
    authors: List[AuthorsDTO]
    abstract: List[TranslationDTO]
    countries: List[VocElementMappingDTO]
    topicClasses: Optional[List[VocElementMappingDTO]]
    # Dataset
    datasetVersionId: int
    datasetReferenceNumber: int
    datasetVersionNumber: int
    datasetRevisionNumber: int
    language: VocElementMappingDTO
    title: List[TranslationDTO]
    doi: Optional[str]
    publicationDate: date
    restriction: VocElementMappingDTO
    specialPermission: VocElementMappingDTO
    dynamicMetadata: Optional[List[DynamicMetadataDTO]]
    dataFiles: List[DataFileMetadataDTO]


@dataclass
class DatasetsMetadataDTO(MappingDataDTO):
    datasetMetadata: List[DatasetMetadataDTO]
    total: int
