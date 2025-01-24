import typing
from SIMULTAN.Projects import ProjectData
from System.IO import FileInfo, TextWriter
from System.Collections.Generic import IEnumerable_1
from SIMULTAN.Data.SimNetworks import SimNetwork

class XMIExporter:
    def __init__(self) -> None: ...
    # Skipped Export due to it being static, abstract and generic.

    Export : Export_MethodGroup
    class Export_MethodGroup:
        @typing.overload
        def __call__(self, projectData: ProjectData, fileToSave: FileInfo) -> None:...
        @typing.overload
        def __call__(self, projectData: ProjectData, writer: TextWriter) -> None:...
        @typing.overload
        def __call__(self, projectData: ProjectData, networks: IEnumerable_1[SimNetwork], fileToSave: FileInfo) -> None:...
        @typing.overload
        def __call__(self, projectData: ProjectData, networks: IEnumerable_1[SimNetwork], writer: TextWriter) -> None:...


