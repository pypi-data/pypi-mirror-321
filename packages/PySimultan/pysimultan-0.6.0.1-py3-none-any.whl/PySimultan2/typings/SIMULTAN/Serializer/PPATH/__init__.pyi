import abc
from System.Collections.Generic import List_1
from System.IO import FileInfo
from SIMULTAN.Projects import ProjectData

class PPathIO(abc.ABC):
    @staticmethod
    def Read(file: FileInfo) -> List_1[str]: ...
    @staticmethod
    def Write(file: FileInfo, projectData: ProjectData) -> None: ...

