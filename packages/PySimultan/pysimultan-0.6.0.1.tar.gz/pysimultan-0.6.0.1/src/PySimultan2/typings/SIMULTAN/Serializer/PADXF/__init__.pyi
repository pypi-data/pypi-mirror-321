import typing
from System.IO import FileInfo
from SIMULTAN.Serializer.DXF import DXFParserInfo
from SIMULTAN.Projects import ProjectData
from System.Collections.Generic import IEnumerable_1
from SIMULTAN.Data.Components import SimBaseParameter

class ParameterDxfIO:
    def __init__(self) -> None: ...
    @staticmethod
    def Read(file: FileInfo, parserInfo: DXFParserInfo) -> None: ...
    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, projectData: ProjectData) -> None:...
        @typing.overload
        def __call__(self, file: FileInfo, projectData: ProjectData, parameters: IEnumerable_1[SimBaseParameter]) -> None:...


