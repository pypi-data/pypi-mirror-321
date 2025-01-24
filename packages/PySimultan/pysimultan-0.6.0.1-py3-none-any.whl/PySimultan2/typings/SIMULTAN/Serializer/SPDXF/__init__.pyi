import abc
from SIMULTAN.Serializer.DXF import DXFSectionParserElement_1
from SIMULTAN.Data.SitePlanner import SitePlannerProject
from System.IO import FileInfo
from SIMULTAN.Projects import ProjectData

class SiteplannerDxfIO(abc.ABC):
    @classmethod
    @property
    def SiteplannerSectionElement(cls) -> DXFSectionParserElement_1[SitePlannerProject]: ...
    @staticmethod
    def CreateEmptySitePlannerProject(file: FileInfo, projectData: ProjectData) -> None: ...

