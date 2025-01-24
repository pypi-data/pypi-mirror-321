import typing, abc
from System.IO import FileInfo
from SIMULTAN.Serializer.DXF import DXFParserInfo
from SIMULTAN.Projects import ProjectData
from System.Xml import XmlElement, XmlNamespaceManager, XmlWriter
from System import Action_1

class ExcelDxfIO(abc.ABC):
    @staticmethod
    def Read(file: FileInfo, parserInfo: DXFParserInfo) -> None: ...
    @staticmethod
    def ReadLibrary(file: FileInfo, parserInfo: DXFParserInfo) -> None: ...
    @staticmethod
    def Write(file: FileInfo, projectData: ProjectData) -> None: ...


class XMLIOExtensions(abc.ABC):
    @staticmethod
    def LoadInnerText(node: XmlElement, xpath: str, converter: Action_1[str], nsmgr: XmlNamespaceManager = ...) -> bool: ...
    # Skipped WriteKeyValue due to it being static, abstract and generic.

    WriteKeyValue : WriteKeyValue_MethodGroup
    class WriteKeyValue_MethodGroup:
        def __getitem__(self, t:typing.Type[WriteKeyValue_1_T1]) -> WriteKeyValue_1[WriteKeyValue_1_T1]: ...

        WriteKeyValue_1_T1 = typing.TypeVar('WriteKeyValue_1_T1')
        class WriteKeyValue_1(typing.Generic[WriteKeyValue_1_T1]):
            WriteKeyValue_1_T = XMLIOExtensions.WriteKeyValue_MethodGroup.WriteKeyValue_1_T1
            def __call__(self, sw: XmlWriter, key: str, value: WriteKeyValue_1_T) -> None:...



