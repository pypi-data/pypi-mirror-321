import typing
from SIMULTAN.Data.Taxonomy import SimTaxonomyEntry
from SIMULTAN.Projects import ProjectData
from SIMULTAN.Data.Geometry import GeometryModel, OffsetAlgorithm
from SIMULTAN.Data.Assets import ResourceFileEntry
from System.Collections.Generic import List_1, IEnumerable_1, Dictionary_2
from System import Array_1

class SimGeoIO:
    def __init__(self) -> None: ...
    @classmethod
    @property
    def SimGeoVersion(cls) -> int: ...
    @staticmethod
    def GetLegacyParentTaxonomyEntry(projectData: ProjectData) -> SimTaxonomyEntry: ...
    @staticmethod
    def Load(geometryFile: ResourceFileEntry, projectData: ProjectData, errors: List_1[SimGeoIOError], offsetAlg: OffsetAlgorithm = ...) -> GeometryModel: ...
    @staticmethod
    def MigrateAfterImport(geometryFiles: IEnumerable_1[ResourceFileEntry], projectData: ProjectData, errors: List_1[SimGeoIOError], importedKeysLookup: Dictionary_2[int, int], importedFilesLookup: Dictionary_2[str, str], offsetAlg: OffsetAlgorithm = ...) -> None: ...
    @staticmethod
    def Save(model: GeometryModel, file: ResourceFileEntry, mode: SimGeoIO.WriteMode) -> bool: ...

    class WriteMode(typing.SupportsInt):
        @typing.overload
        def __init__(self, value : int) -> None: ...
        @typing.overload
        def __init__(self, value : int, force_if_true: bool) -> None: ...
        def __int__(self) -> int: ...
        
        # Values:
        Plaintext : SimGeoIO.WriteMode # 0



class SimGeoIOError:
    def __init__(self, reason: SimGeoIOErrorReason, data: Array_1[typing.Any]) -> None: ...
    @property
    def Data(self) -> Array_1[typing.Any]: ...
    @property
    def Reason(self) -> SimGeoIOErrorReason: ...


class SimGeoIOErrorReason(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    InvalidLinkedModel : SimGeoIOErrorReason # 0
    ReferenceConvertFailed : SimGeoIOErrorReason # 1
    ModelWithSameId : SimGeoIOErrorReason # 2

