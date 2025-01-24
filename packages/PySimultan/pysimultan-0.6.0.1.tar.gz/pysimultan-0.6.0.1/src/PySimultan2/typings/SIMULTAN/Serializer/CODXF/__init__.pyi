import typing, abc
from SIMULTAN.Serializer.DXF import DXFSkipSectionParserElement, DXFParserInfo, DXFStreamReader, DXFStreamWriter, DXFSectionParserElement_1, DXFParserResultSet, DXFEntityParserElementBase_1
from System.IO import FileInfo
from System.Collections.Generic import IEnumerable_1
from SIMULTAN.Data.Components import SimComponent, SimSlot, SimBaseParameter
from SIMULTAN.Data.FlowNetworks import SimFlowNetwork
from SIMULTAN.Projects import ProjectData
from System import ValueTuple_2
from SIMULTAN.Data.ValueMappings import SimPrefilter, SimColorMap, SimValueMapping

class ComponentDxfIO(abc.ABC):
    ImportantSection : DXFSkipSectionParserElement
    @staticmethod
    def WriteLibrary(file: FileInfo, components: IEnumerable_1[SimComponent], networks: IEnumerable_1[SimFlowNetwork]) -> None: ...
    # Skipped Read due to it being static, abstract and generic.

    Read : Read_MethodGroup
    class Read_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, parserInfo: DXFParserInfo) -> None:...
        @typing.overload
        def __call__(self, reader: DXFStreamReader, parserInfo: DXFParserInfo) -> None:...

    # Skipped ReadLibrary due to it being static, abstract and generic.

    ReadLibrary : ReadLibrary_MethodGroup
    class ReadLibrary_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, parserInfo: DXFParserInfo) -> None:...
        @typing.overload
        def __call__(self, reader: DXFStreamReader, parserInfo: DXFParserInfo) -> None:...

    # Skipped ReadPublic due to it being static, abstract and generic.

    ReadPublic : ReadPublic_MethodGroup
    class ReadPublic_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, parserInfo: DXFParserInfo) -> None:...
        @typing.overload
        def __call__(self, reader: DXFStreamReader, parserInfo: DXFParserInfo) -> None:...

    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, projectData: ProjectData) -> None:...
        @typing.overload
        def __call__(self, writer: DXFStreamWriter, projectData: ProjectData) -> None:...

    # Skipped WritePublic due to it being static, abstract and generic.

    WritePublic : WritePublic_MethodGroup
    class WritePublic_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, projectData: ProjectData) -> None:...
        @typing.overload
        def __call__(self, writer: DXFStreamWriter, projectData: ProjectData) -> None:...



class ComponentDxfIOComponents(abc.ABC):
    ComponentSectionEntityElement : DXFSectionParserElement_1[ValueTuple_2[SimSlot, SimComponent]]
    @staticmethod
    def ParseBaseParameter(data: DXFParserResultSet, info: DXFParserInfo) -> SimBaseParameter: ...

    class ParameterType(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Double : ComponentDxfIOComponents.ParameterType # 0
        Integer : ComponentDxfIOComponents.ParameterType # 1
        Boolean : ComponentDxfIOComponents.ParameterType # 2
        String : ComponentDxfIOComponents.ParameterType # 3
        Enum : ComponentDxfIOComponents.ParameterType # 4



class ComponentDxfIONetworks(abc.ABC):
    pass


class ComponentDxfIOResources(abc.ABC):
    pass


class ComponentDxfIOSimNetworks(abc.ABC):
    pass


class ComponentDxfIOValueMappings(abc.ABC):
    AveragePrefilterEntityElement : DXFEntityParserElementBase_1[SimPrefilter]
    DefaultPrefilterEntityElement : DXFEntityParserElementBase_1[SimPrefilter]
    LinearGradientColorMapEntityElement : DXFEntityParserElementBase_1[SimColorMap]
    MaximumPrefilterEntityElement : DXFEntityParserElementBase_1[SimPrefilter]
    MinimumPrefilterEntityElement : DXFEntityParserElementBase_1[SimPrefilter]
    ThresholdColorMapEntityElement : DXFEntityParserElementBase_1[SimColorMap]
    ValueMappingEntityElement : DXFEntityParserElementBase_1[SimValueMapping]

