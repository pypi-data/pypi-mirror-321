import typing
from System.IO import FileInfo
from System.Collections.Generic import IEnumerable_1
from SIMULTAN.Data.Taxonomy import SimTaxonomy
from SIMULTAN.Projects import ExtendedProjectData
from SIMULTAN.Serializer.DXF import DXFStreamWriter, DXFParserInfo, DXFStreamReader

class SimTaxonomyDxfIO:
    def __init__(self) -> None: ...
    # Skipped Export due to it being static, abstract and generic.

    Export : Export_MethodGroup
    class Export_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, taxonomies: IEnumerable_1[SimTaxonomy], projectData: ExtendedProjectData) -> None:...
        @typing.overload
        def __call__(self, writer: DXFStreamWriter, taxonomies: IEnumerable_1[SimTaxonomy], projectData: ExtendedProjectData) -> None:...

    # Skipped Import due to it being static, abstract and generic.

    Import : Import_MethodGroup
    class Import_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, info: DXFParserInfo) -> None:...
        @typing.overload
        def __call__(self, reader: DXFStreamReader, parserInfo: DXFParserInfo) -> None:...

    # Skipped Read due to it being static, abstract and generic.

    Read : Read_MethodGroup
    class Read_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, info: DXFParserInfo) -> None:...
        @typing.overload
        def __call__(self, reader: DXFStreamReader, parserInfo: DXFParserInfo) -> None:...

    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        @typing.overload
        def __call__(self, file: FileInfo, taxonomies: IEnumerable_1[SimTaxonomy], projectData: ExtendedProjectData) -> None:...
        @typing.overload
        def __call__(self, writer: DXFStreamWriter, taxonomies: IEnumerable_1[SimTaxonomy], projectData: ExtendedProjectData) -> None:...


