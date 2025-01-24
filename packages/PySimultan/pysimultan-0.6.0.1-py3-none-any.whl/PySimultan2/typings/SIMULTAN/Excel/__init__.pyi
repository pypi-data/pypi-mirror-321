from System.IO import FileInfo
from SIMULTAN.Data.MultiValues import SimMultiValueCollection

class ExcelStandardImporter:
    def __init__(self) -> None: ...
    COL_OFFSET : int
    COMPONENT_COL_OFFSET : int
    COMPONENT_NR_VALUE_COLUMNS : int
    MAX_NR_TABLE_ENTRIES : int
    MAX_NR_VALUE_COLUMNS : int
    ROW_OFFSET : int
    TABLE_NAME : str
    def ImportBigTableFromFile(self, file: FileInfo, factory: SimMultiValueCollection, unitX: str, unitY: str, rowNameFormat: str, rowUnit: str, maxRowCount: int = ...) -> None: ...
    def ImportBigTableWNamesFromFile(self, file: FileInfo, factory: SimMultiValueCollection, unitX: str, unitY: str, rowUnit: str, maxRowCount: int = ...) -> None: ...

