import abc
from SIMULTAN.Projects import HierarchicProjectMetaData
from System.IO import FileInfo
from SIMULTAN.Serializer.DXF import DXFParserInfo

class MetaDxfIO(abc.ABC):
    @staticmethod
    def Read(file: FileInfo, parserInfo: DXFParserInfo) -> HierarchicProjectMetaData: ...
    @staticmethod
    def Write(file: FileInfo, metaData: HierarchicProjectMetaData) -> None: ...

