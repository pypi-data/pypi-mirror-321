import typing, abc
from System.Collections.Generic import IEnumerable_1, Dictionary_2, List_1
from System import Guid, Attribute, IDisposable, ValueTuple_2, Array_1, Action_2, Action_3
from SIMULTAN.Projects import ExtendedProjectData
from System.IO import FileInfo

class AssetSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    RESOURCE_KEY : AssetSaveCode # 7001
    CONTENT : AssetSaveCode # 7002
    REFERENCE_COL : AssetSaveCode # 7003
    REFERENCE_LOCALID : AssetSaveCode # 7004
    REFERENCE_GLOBALID : AssetSaveCode # 7005
    WORKING_DIR : AssetSaveCode # 7090
    WORKING_PATHS : AssetSaveCode # 7091
    APATH_COLLECTION : AssetSaveCode # 7101
    APATH_USER : AssetSaveCode # 7102
    APATH_KEY : AssetSaveCode # 7103
    APATH_REL_PATH : AssetSaveCode # 7104
    APATH_ISCONTAINED : AssetSaveCode # 7105
    APATH_FULL_PATH : AssetSaveCode # 7106
    APATHS_AS_OBJECTS : AssetSaveCode # 7107
    ASSET_COLLECTION : AssetSaveCode # 7111


class CalculationSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NAME : CalculationSaveCode # 1301
    EXPRESSION : CalculationSaveCode # 1302
    PARAMS_INPUT : CalculationSaveCode # 1303
    PARAMS_OUTPUT : CalculationSaveCode # 1304
    LOST_REFS : CalculationSaveCode # 1305
    LOST_REFS_MSG : CalculationSaveCode # 1306
    VECTOR_CALC_OPERATIONS : CalculationSaveCode # 1307
    VECTOR_CALC_RANGES : CalculationSaveCode # 1308
    VECTOR_CALC_ITERATION_COUNT : CalculationSaveCode # 1309
    VECTOR_CALC_AGGREGATION : CalculationSaveCode # 1310
    VECTOR_CALC_RANDOM : CalculationSaveCode # 1311
    VECTOR_CALC_OVERRIDE : CalculationSaveCode # 1312


class CalculatorMappingSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NAME : CalculatorMappingSaveCode # 1701
    CALCULATOR_LOCALID : CalculatorMappingSaveCode # 1702
    INPUT_MAPPING : CalculatorMappingSaveCode # 1703
    INPUT_DATAPARAMETER_LOCALID : CalculatorMappingSaveCode # 1704
    INPUT_CALCULATORPARAMETER_LOCALID : CalculatorMappingSaveCode # 1705
    OUTPUT_MAPPING : CalculatorMappingSaveCode # 1706
    OUTPUT_DATAPARAMETER_LOCALID : CalculatorMappingSaveCode # 1707
    OUTPUT_CALCULATORPARAMETER_LOCALID : CalculatorMappingSaveCode # 1708
    CALCULATOR_GLOBALID : CalculatorMappingSaveCode # 1709
    INPUT_DATAPARAMETER_GLOBALID : CalculatorMappingSaveCode # 1710
    INPUT_CALCULATORPARAMETER_GLOBALID : CalculatorMappingSaveCode # 1711
    OUTPUT_DATAPARAMETER_GLOBALID : CalculatorMappingSaveCode # 1712
    OUTPUT_CALCULATORPARAMETER_GLOBALID : CalculatorMappingSaveCode # 1713


class ChatItemSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TYPE : ChatItemSaveCode # 8001
    AUTHOR : ChatItemSaveCode # 8002
    VR_ADDRESS : ChatItemSaveCode # 8003
    VR_PASSWORD : ChatItemSaveCode # 8004
    GIT_COMMIT : ChatItemSaveCode # 8005
    TIMESTAMP : ChatItemSaveCode # 8006
    MESSAGE : ChatItemSaveCode # 8007
    STATE : ChatItemSaveCode # 8008
    EXPECTED_REACTIONS_FROM : ChatItemSaveCode # 8009
    CHILDREN : ChatItemSaveCode # 8010
    CONVERSATION : ChatItemSaveCode # 8101


class CommonParserElements(abc.ABC):
    VersionSectionElement : DXFSectionParserElement_1[DXFParserInfo]


class ComponentAccessProfileSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    MANAGER : ComponentAccessProfileSaveCode # 1433
    ACTION_TARGET_ID : ComponentAccessProfileSaveCode # 1434
    ACTION_SUPERVIZE : ComponentAccessProfileSaveCode # 1435
    ACTION_RELEASE : ComponentAccessProfileSaveCode # 1436
    ACTION_TIME_STAMP : ComponentAccessProfileSaveCode # 1437
    ACTION_ACTOR : ComponentAccessProfileSaveCode # 1438


class ComponentAccessTrackerSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    FLAGS : ComponentAccessTrackerSaveCode # 1421
    WRITE_PREV : ComponentAccessTrackerSaveCode # 1422
    WRITE_LAST : ComponentAccessTrackerSaveCode # 1423
    SUPERVIZE_PREV : ComponentAccessTrackerSaveCode # 1424
    SUPERVIZE_LAST : ComponentAccessTrackerSaveCode # 1425
    RELEASE_PREV : ComponentAccessTrackerSaveCode # 1426
    RELEASE_LAST : ComponentAccessTrackerSaveCode # 1427


class ComponentFileMetaInfoSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    MAX_CALCULATION_ID : ComponentFileMetaInfoSaveCode # 1801


class ComponentInstanceSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NAME : ComponentInstanceSaveCode # 1601
    INSTANCE_TYPE : ComponentInstanceSaveCode # 1602
    GEOM_IDS_X : ComponentInstanceSaveCode # 1603
    GEOM_IDS_Y : ComponentInstanceSaveCode # 1604
    GEOM_IDS_Z : ComponentInstanceSaveCode # 1605
    GEOM_CS : ComponentInstanceSaveCode # 1606
    TRANSF_WC2LC : ComponentInstanceSaveCode # 1607
    TRANSF_LC2WC : ComponentInstanceSaveCode # 1608
    STATE_ISREALIZED : ComponentInstanceSaveCode # 1609
    INST_ROTATION : ComponentInstanceSaveCode # 1619
    INST_SIZE : ComponentInstanceSaveCode # 1620
    INST_NETWORKELEMENT_ID : ComponentInstanceSaveCode # 1621
    INST_NWE_NAME : ComponentInstanceSaveCode # 1622
    INST_PATH : ComponentInstanceSaveCode # 1623
    GEOM_IDS_W : ComponentInstanceSaveCode # 1630
    INST_SIZE_TRANSFERSETTINGS : ComponentInstanceSaveCode # 1640
    INST_SIZE_TS_SOURCE : ComponentInstanceSaveCode # 1641
    INST_SIZE_TS_INITVAL : ComponentInstanceSaveCode # 1642
    INST_SIZE_TS_PARAMETER_LOCALID : ComponentInstanceSaveCode # 1643
    INST_SIZE_TS_ADDEND : ComponentInstanceSaveCode # 1644
    INST_SIZE_TS_PARAMETER_GLOBALID : ComponentInstanceSaveCode # 1645
    INST_PARAMS : ComponentInstanceSaveCode # 1650
    INST_PARAM_ID : ComponentInstanceSaveCode # 1651
    INST_PARAM_VAL : ComponentInstanceSaveCode # 1652
    INST_REFS : ComponentInstanceSaveCode # 1660
    INST_REFS_KEY : ComponentInstanceSaveCode # 1661
    INST_REFS_VAL : ComponentInstanceSaveCode # 1662
    GEOM_REF_FILE : ComponentInstanceSaveCode # 1663
    GEOM_REF_ID : ComponentInstanceSaveCode # 1664
    STATE_CONNECTION_STATE : ComponentInstanceSaveCode # 1665
    INST_NETWORKELEMENT_LOCATION : ComponentInstanceSaveCode # 1666
    INST_PROPAGATE_PARAM_CHANGES : ComponentInstanceSaveCode # 1667
    INST_SIMNWE_NAME : ComponentInstanceSaveCode # 1668
    INST_PLACEMENTS : ComponentInstanceSaveCode # 1670
    INST_SIMNWE_LOCATION : ComponentInstanceSaveCode # 1671
    PLACEMENT_STATE : ComponentInstanceSaveCode # 1672
    PLACEMENT_INSTANCE_TYPE : ComponentInstanceSaveCode # 1673


class ComponentSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NAME : ComponentSaveCode # 1401
    DESCRIPTION : ComponentSaveCode # 1402
    CATEGORY : ComponentSaveCode # 1403
    ACCESS_RECORD : ComponentSaveCode # 1404
    FUNCTION_SLOTS_ALL : ComponentSaveCode # 1405
    MAIN_SLOT : ComponentSaveCode # 1406
    CONTAINED_COMPONENTS : ComponentSaveCode # 1407
    CONTAINED_COMPONENT_SLOTS : ComponentSaveCode # 1408
    REFERENCED_COMPONENTS : ComponentSaveCode # 1409
    CONTAINED_PARAMETERS : ComponentSaveCode # 1410
    CONTAINED_CALCULATIONS : ComponentSaveCode # 1411
    TIME_STAMP : ComponentSaveCode # 1412
    SYMBOL_ID : ComponentSaveCode # 1413
    INSTANCES : ComponentSaveCode # 1414
    GENERATED_AUTOMATICALLY : ComponentSaveCode # 1415
    CALCULATOR_MAPPINGS : ComponentSaveCode # 1416
    REFERENCES_INTACT : ComponentSaveCode # 1417
    MAPPINGS_TO_EXCEL_TOOLS : ComponentSaveCode # 1418
    VISIBILTY : ComponentSaveCode # 1419
    COLOR : ComponentSaveCode # 1420
    SORTING_TYPE : ComponentSaveCode # 1421
    SLOTS : ComponentSaveCode # 1422
    INSTANCE_TYPE : ComponentSaveCode # 1428
    ACCESS_STATE : ComponentSaveCode # 1431
    PROFILE : ComponentSaveCode # 1432
    SLOT_TAXONOMY_ENTRY_ID : ComponentSaveCode # 1461
    SLOT_TAXONOMY_ENTRY_PROJECT_ID : ComponentSaveCode # 1462


class DataMappingSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    RULE_NAME : DataMappingSaveCode # 6001
    RULE_SHEETNAME : DataMappingSaveCode # 6002
    RULE_OFFSETPARENT_X : DataMappingSaveCode # 6003
    RULE_OFFSETPARENT_Y : DataMappingSaveCode # 6004
    RULE_SUBJECT : DataMappingSaveCode # 6005
    RULE_PROPERTIES : DataMappingSaveCode # 6006
    RULE_MAPPINGRANGE : DataMappingSaveCode # 6007
    RULE_ORDER_HORIZONTALLY : DataMappingSaveCode # 6008
    RULE_PREPEND_CONTENT_TO_CHILDREN : DataMappingSaveCode # 6009
    RULE_FILTER : DataMappingSaveCode # 6010
    RULE_OFFSETCONSECUTIVE_X : DataMappingSaveCode # 6011
    RULE_OFFSETCONSECUTIVE_Y : DataMappingSaveCode # 6012
    RULE_CHILDREN : DataMappingSaveCode # 6013
    RULE_DIRECTION : DataMappingSaveCode # 6014
    RULE_REFERENCEPOSITIONPARENT : DataMappingSaveCode # 6015
    RULE_FILTER_PROPERTY : DataMappingSaveCode # 6016
    RULE_FILTER_TYPE : DataMappingSaveCode # 6017
    RULE_FILTER_VALUE : DataMappingSaveCode # 6018
    RULE_FILTER_VALUE2 : DataMappingSaveCode # 6019
    RULE_MAPPED_COMPONENTS : DataMappingSaveCode # 6020
    RULE_PARAMETER_GLOBALID : DataMappingSaveCode # 6021
    RULE_PARAMETER_LOCALID : DataMappingSaveCode # 6022
    RULE_RANGE_COLUMNSTART : DataMappingSaveCode # 6023
    RULE_RANGE_ROWSTART : DataMappingSaveCode # 6024
    RULE_RANGE_COLUMNCOUNT : DataMappingSaveCode # 6025
    RULE_RANGE_ROWCOUNT : DataMappingSaveCode # 6026
    RULE_REFERENCEPOSITIONCONSECUTIVE : DataMappingSaveCode # 6027
    TOOL_NAME : DataMappingSaveCode # 6101
    TOOL_MACRO_NAME : DataMappingSaveCode # 6102
    TOOL_MAPPINGRULES : DataMappingSaveCode # 6103
    TOOL_LAST_PATH_TO_FILE : DataMappingSaveCode # 6104
    TOOL_OUTPUTRANGERULES : DataMappingSaveCode # 6105
    TOOL_OUTPUTRULES : DataMappingSaveCode # 6106
    MAP_PATH : DataMappingSaveCode # 6201
    MAP_TOOL_NAME : DataMappingSaveCode # 6202
    MAP_TOOL_FILE_PATH : DataMappingSaveCode # 6203
    MAP_RULE_NAME : DataMappingSaveCode # 6204
    MAP_RULE_INDEX : DataMappingSaveCode # 6205
    MAP_COL_OWNER_ID : DataMappingSaveCode # 6301
    MAP_COL_OWNER_MANAGER : DataMappingSaveCode # 6302
    MAP_COL_RULES : DataMappingSaveCode # 6303
    MAP_COL_TODO : DataMappingSaveCode # 6304
    DATA_MAP_SHEET_NAME : DataMappingSaveCode # 6501
    DATA_MAP_RANGE_X : DataMappingSaveCode # 6502
    DATA_MAP_RANGE_Y : DataMappingSaveCode # 6503
    DATA_MAP_RANGE_Z : DataMappingSaveCode # 6504
    DATA_MAP_RANGE_W : DataMappingSaveCode # 6505
    DATA_MAP_TYPE : DataMappingSaveCode # 6506
    UNMAP_FILTER_SWITCH : DataMappingSaveCode # 6521
    UNMAP_TARGET_COMP_ID : DataMappingSaveCode # 6522
    UNMAP_TARGET_PARAM : DataMappingSaveCode # 6523
    UNMAP_FILTER_COMP : DataMappingSaveCode # 6524
    UNMAP_FILTER_PARAM : DataMappingSaveCode # 6525
    UNMAP_PARAM_POINTER_X : DataMappingSaveCode # 6526
    UNMAP_PARAM_POINTER_Y : DataMappingSaveCode # 6527
    UNMAP_DATA : DataMappingSaveCode # 6528
    UNMAP_TARGET_COMP_LOCATION : DataMappingSaveCode # 6529
    RULE_MAXMATCHES : DataMappingSaveCode # 6601
    RULE_MAXDEPTH : DataMappingSaveCode # 6602
    RULE_TRAVERSE_STRATEGY : DataMappingSaveCode # 6603
    TRAVERSAL_ACTIVATED : DataMappingSaveCode # 6604
    VERSION : DataMappingSaveCode # 6701


class DXFArrayEntryParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFArrayEntryParserElement_GenericClasses_DXFArrayEntryParserElement_1_T = typing.TypeVar('Generic_DXFArrayEntryParserElement_GenericClasses_DXFArrayEntryParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFArrayEntryParserElement_GenericClasses_DXFArrayEntryParserElement_1_T]) -> typing.Type[DXFArrayEntryParserElement_1[Generic_DXFArrayEntryParserElement_GenericClasses_DXFArrayEntryParserElement_1_T]]: ...

class DXFArrayEntryParserElement(DXFArrayEntryParserElement_0, metaclass =DXFArrayEntryParserElement_GenericClasses): ...

class DXFArrayEntryParserElement_0(DXFEntryParserElement):
    @property
    def Code(self) -> int: ...
    @property
    def ElementCode(self) -> int: ...


DXFArrayEntryParserElement_1_T = typing.TypeVar('DXFArrayEntryParserElement_1_T')
class DXFArrayEntryParserElement_1(typing.Generic[DXFArrayEntryParserElement_1_T], DXFArrayEntryParserElement_0):
    @property
    def Code(self) -> int: ...
    @property
    def ElementCode(self) -> int: ...


class DXFBase64SingleEntryParserElement(DXFEntryParserElement):
    @property
    def Code(self) -> int: ...


class DXFComplexEntityParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFComplexEntityParserElement_GenericClasses_DXFComplexEntityParserElement_1_T = typing.TypeVar('Generic_DXFComplexEntityParserElement_GenericClasses_DXFComplexEntityParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFComplexEntityParserElement_GenericClasses_DXFComplexEntityParserElement_1_T]) -> typing.Type[DXFComplexEntityParserElement_1[Generic_DXFComplexEntityParserElement_GenericClasses_DXFComplexEntityParserElement_1_T]]: ...

DXFComplexEntityParserElement : DXFComplexEntityParserElement_GenericClasses

DXFComplexEntityParserElement_1_T = typing.TypeVar('DXFComplexEntityParserElement_1_T')
class DXFComplexEntityParserElement_1(typing.Generic[DXFComplexEntityParserElement_1_T], DXFEntityParserElementBase_1[DXFComplexEntityParserElement_1_T]):
    @property
    def Entries(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class DXFENTCTNEntityParserElementV11_GenericClasses(abc.ABCMeta):
    Generic_DXFENTCTNEntityParserElementV11_GenericClasses_DXFENTCTNEntityParserElementV11_1_T = typing.TypeVar('Generic_DXFENTCTNEntityParserElementV11_GenericClasses_DXFENTCTNEntityParserElementV11_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFENTCTNEntityParserElementV11_GenericClasses_DXFENTCTNEntityParserElementV11_1_T]) -> typing.Type[DXFENTCTNEntityParserElementV11_1[Generic_DXFENTCTNEntityParserElementV11_GenericClasses_DXFENTCTNEntityParserElementV11_1_T]]: ...

DXFENTCTNEntityParserElementV11 : DXFENTCTNEntityParserElementV11_GenericClasses

DXFENTCTNEntityParserElementV11_1_T = typing.TypeVar('DXFENTCTNEntityParserElementV11_1_T')
class DXFENTCTNEntityParserElementV11_1(typing.Generic[DXFENTCTNEntityParserElementV11_1_T], DXFEntityParserElementBase_1[DXFENTCTNEntityParserElementV11_1_T]):
    @property
    def Entries(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class DXFEntityCasterElement_GenericClasses(abc.ABCMeta):
    Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_T = typing.TypeVar('Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_T')
    Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_U = typing.TypeVar('Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_U')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_T], typing.Type[Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_U]]) -> typing.Type[DXFEntityCasterElement_2[Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_T, Generic_DXFEntityCasterElement_GenericClasses_DXFEntityCasterElement_2_U]]: ...

DXFEntityCasterElement : DXFEntityCasterElement_GenericClasses

DXFEntityCasterElement_2_T = typing.TypeVar('DXFEntityCasterElement_2_T')
DXFEntityCasterElement_2_U = typing.TypeVar('DXFEntityCasterElement_2_U')
class DXFEntityCasterElement_2(typing.Generic[DXFEntityCasterElement_2_T, DXFEntityCasterElement_2_U], DXFEntityParserElementBase_1[DXFEntityCasterElement_2_T]):
    def __init__(self, content: DXFEntityParserElementBase_1[DXFEntityCasterElement_2_U]) -> None: ...
    @property
    def Entries(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class DXFEntityParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFEntityParserElement_GenericClasses_DXFEntityParserElement_1_T = typing.TypeVar('Generic_DXFEntityParserElement_GenericClasses_DXFEntityParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFEntityParserElement_GenericClasses_DXFEntityParserElement_1_T]) -> typing.Type[DXFEntityParserElement_1[Generic_DXFEntityParserElement_GenericClasses_DXFEntityParserElement_1_T]]: ...

DXFEntityParserElement : DXFEntityParserElement_GenericClasses

DXFEntityParserElement_1_T = typing.TypeVar('DXFEntityParserElement_1_T')
class DXFEntityParserElement_1(typing.Generic[DXFEntityParserElement_1_T], DXFEntityParserElementBase_1[DXFEntityParserElement_1_T]):
    @property
    def Entries(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class DXFEntityParserElementBase_GenericClasses(abc.ABCMeta):
    Generic_DXFEntityParserElementBase_GenericClasses_DXFEntityParserElementBase_1_T = typing.TypeVar('Generic_DXFEntityParserElementBase_GenericClasses_DXFEntityParserElementBase_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFEntityParserElementBase_GenericClasses_DXFEntityParserElementBase_1_T]) -> typing.Type[DXFEntityParserElementBase_1[Generic_DXFEntityParserElementBase_GenericClasses_DXFEntityParserElementBase_1_T]]: ...

DXFEntityParserElementBase : DXFEntityParserElementBase_GenericClasses

DXFEntityParserElementBase_1_T = typing.TypeVar('DXFEntityParserElementBase_1_T')
class DXFEntityParserElementBase_1(typing.Generic[DXFEntityParserElementBase_1_T], DXFParserElement, IDXFEntityParserElementBase):
    @property
    def Entries(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class DXFEntitySequenceAlwaysStartEndEntryParserElementV11_GenericClasses(abc.ABCMeta):
    Generic_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_GenericClasses_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1_T = typing.TypeVar('Generic_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_GenericClasses_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_GenericClasses_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1_T]) -> typing.Type[DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1[Generic_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_GenericClasses_DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1_T]]: ...

DXFEntitySequenceAlwaysStartEndEntryParserElementV11 : DXFEntitySequenceAlwaysStartEndEntryParserElementV11_GenericClasses

DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1_T = typing.TypeVar('DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1_T')
class DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1(typing.Generic[DXFEntitySequenceAlwaysStartEndEntryParserElementV11_1_T], DXFEntryParserElement, IDXFEntitySequenceEntryParserEntry):
    @property
    def Code(self) -> int: ...
    @property
    def Entities(self) -> IEnumerable_1[IDXFEntityParserElementBase]: ...


class DXFEntitySequenceEntryParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFEntitySequenceEntryParserElement_GenericClasses_DXFEntitySequenceEntryParserElement_1_T = typing.TypeVar('Generic_DXFEntitySequenceEntryParserElement_GenericClasses_DXFEntitySequenceEntryParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFEntitySequenceEntryParserElement_GenericClasses_DXFEntitySequenceEntryParserElement_1_T]) -> typing.Type[DXFEntitySequenceEntryParserElement_1[Generic_DXFEntitySequenceEntryParserElement_GenericClasses_DXFEntitySequenceEntryParserElement_1_T]]: ...

DXFEntitySequenceEntryParserElement : DXFEntitySequenceEntryParserElement_GenericClasses

DXFEntitySequenceEntryParserElement_1_T = typing.TypeVar('DXFEntitySequenceEntryParserElement_1_T')
class DXFEntitySequenceEntryParserElement_1(typing.Generic[DXFEntitySequenceEntryParserElement_1_T], DXFEntryParserElement, IDXFEntitySequenceEntryParserEntry):
    @property
    def Code(self) -> int: ...
    @property
    def Entities(self) -> IEnumerable_1[IDXFEntityParserElementBase]: ...


class DXFEntitySequenceNoStartEntryParserElementV11_GenericClasses(abc.ABCMeta):
    Generic_DXFEntitySequenceNoStartEntryParserElementV11_GenericClasses_DXFEntitySequenceNoStartEntryParserElementV11_1_T = typing.TypeVar('Generic_DXFEntitySequenceNoStartEntryParserElementV11_GenericClasses_DXFEntitySequenceNoStartEntryParserElementV11_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFEntitySequenceNoStartEntryParserElementV11_GenericClasses_DXFEntitySequenceNoStartEntryParserElementV11_1_T]) -> typing.Type[DXFEntitySequenceNoStartEntryParserElementV11_1[Generic_DXFEntitySequenceNoStartEntryParserElementV11_GenericClasses_DXFEntitySequenceNoStartEntryParserElementV11_1_T]]: ...

DXFEntitySequenceNoStartEntryParserElementV11 : DXFEntitySequenceNoStartEntryParserElementV11_GenericClasses

DXFEntitySequenceNoStartEntryParserElementV11_1_T = typing.TypeVar('DXFEntitySequenceNoStartEntryParserElementV11_1_T')
class DXFEntitySequenceNoStartEntryParserElementV11_1(typing.Generic[DXFEntitySequenceNoStartEntryParserElementV11_1_T], DXFEntryParserElement, IDXFEntitySequenceEntryParserEntry):
    @property
    def Code(self) -> int: ...
    @property
    def Entities(self) -> IEnumerable_1[IDXFEntityParserElementBase]: ...


class DXFEntryParserElement(DXFParserElement):
    @property
    def Code(self) -> int: ...


class DXFMultiLineTextElement(DXFEntryParserElement):
    @property
    def Code(self) -> int: ...


class DXFNestedListEntryParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFNestedListEntryParserElement_GenericClasses_DXFNestedListEntryParserElement_1_T = typing.TypeVar('Generic_DXFNestedListEntryParserElement_GenericClasses_DXFNestedListEntryParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFNestedListEntryParserElement_GenericClasses_DXFNestedListEntryParserElement_1_T]) -> typing.Type[DXFNestedListEntryParserElement_1[Generic_DXFNestedListEntryParserElement_GenericClasses_DXFNestedListEntryParserElement_1_T]]: ...

class DXFNestedListEntryParserElement(DXFNestedListEntryParserElement_0, metaclass =DXFNestedListEntryParserElement_GenericClasses): ...

class DXFNestedListEntryParserElement_0(DXFEntryParserElement):
    @property
    def Code(self) -> int: ...
    @property
    def ContinueCode(self) -> int: ...
    @property
    def Elements(self) -> IEnumerable_1[DXFEntryParserElement]: ...


DXFNestedListEntryParserElement_1_T = typing.TypeVar('DXFNestedListEntryParserElement_1_T')
class DXFNestedListEntryParserElement_1(typing.Generic[DXFNestedListEntryParserElement_1_T], DXFNestedListEntryParserElement_0):
    @property
    def Code(self) -> int: ...
    @property
    def ContinueCode(self) -> int: ...
    @property
    def Elements(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class DXFParserElement(abc.ABC):
    pass


class DXFParserInfo:
    def __init__(self, globalId: Guid, projectData: ExtendedProjectData) -> None: ...
    @property
    def CurrentFile(self) -> FileInfo: ...
    @CurrentFile.setter
    def CurrentFile(self, value: FileInfo) -> FileInfo: ...
    @property
    def FileVersion(self) -> int: ...
    @FileVersion.setter
    def FileVersion(self, value: int) -> int: ...
    @property
    def GlobalId(self) -> Guid: ...
    @property
    def ProjectData(self) -> ExtendedProjectData: ...
    def FinishLog(self) -> None: ...
    def Log(self, message: str) -> None: ...


class DXFParserResultSet:
    def __init__(self) -> None: ...


class DXFRecursiveEntityParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFRecursiveEntityParserElement_GenericClasses_DXFRecursiveEntityParserElement_1_T = typing.TypeVar('Generic_DXFRecursiveEntityParserElement_GenericClasses_DXFRecursiveEntityParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFRecursiveEntityParserElement_GenericClasses_DXFRecursiveEntityParserElement_1_T]) -> typing.Type[DXFRecursiveEntityParserElement_1[Generic_DXFRecursiveEntityParserElement_GenericClasses_DXFRecursiveEntityParserElement_1_T]]: ...

DXFRecursiveEntityParserElement : DXFRecursiveEntityParserElement_GenericClasses

DXFRecursiveEntityParserElement_1_T = typing.TypeVar('DXFRecursiveEntityParserElement_1_T')
class DXFRecursiveEntityParserElement_1(typing.Generic[DXFRecursiveEntityParserElement_1_T], DXFEntityParserElementBase_1[DXFRecursiveEntityParserElement_1_T]):
    @property
    def Entries(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class DXFSectionParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFSectionParserElement_GenericClasses_DXFSectionParserElement_1_T = typing.TypeVar('Generic_DXFSectionParserElement_GenericClasses_DXFSectionParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFSectionParserElement_GenericClasses_DXFSectionParserElement_1_T]) -> typing.Type[DXFSectionParserElement_1[Generic_DXFSectionParserElement_GenericClasses_DXFSectionParserElement_1_T]]: ...

DXFSectionParserElement : DXFSectionParserElement_GenericClasses

DXFSectionParserElement_1_T = typing.TypeVar('DXFSectionParserElement_1_T')
class DXFSectionParserElement_1(typing.Generic[DXFSectionParserElement_1_T], DXFParserElement):
    @property
    def Entities(self) -> Dictionary_2[str, DXFEntityParserElementBase_1[DXFSectionParserElement_1_T]]: ...
    @Entities.setter
    def Entities(self, value: Dictionary_2[str, DXFEntityParserElementBase_1[DXFSectionParserElement_1_T]]) -> Dictionary_2[str, DXFEntityParserElementBase_1[DXFSectionParserElement_1_T]]: ...
    def IsParsable(self, reader: DXFStreamReader, info: DXFParserInfo) -> bool: ...


class DXFSerializerTypeNameAttribute(Attribute):
    def __init__(self, name: str) -> None: ...
    @property
    def Name(self) -> str: ...
    @property
    def TypeId(self) -> typing.Any: ...


class DXFSingleEntryParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFSingleEntryParserElement_GenericClasses_DXFSingleEntryParserElement_1_T = typing.TypeVar('Generic_DXFSingleEntryParserElement_GenericClasses_DXFSingleEntryParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFSingleEntryParserElement_GenericClasses_DXFSingleEntryParserElement_1_T]) -> typing.Type[DXFSingleEntryParserElement_1[Generic_DXFSingleEntryParserElement_GenericClasses_DXFSingleEntryParserElement_1_T]]: ...

DXFSingleEntryParserElement : DXFSingleEntryParserElement_GenericClasses

DXFSingleEntryParserElement_1_T = typing.TypeVar('DXFSingleEntryParserElement_1_T')
class DXFSingleEntryParserElement_1(typing.Generic[DXFSingleEntryParserElement_1_T], DXFEntryParserElement):
    @property
    def Code(self) -> int: ...


class DXFSkipEntryParserElement(DXFEntryParserElement):
    def __init__(self, code: ComponentInstanceSaveCode) -> None: ...
    @property
    def Code(self) -> int: ...


class DXFSkipSectionParserElement(DXFParserElement):
    def __init__(self, sectionName: str) -> None: ...


class DXFStreamReader(IDisposable):
    def ClearPeek(self) -> None: ...
    def Dispose(self) -> None: ...
    def GetLast(self) -> ValueTuple_2[int, str]: ...
    def Peek(self) -> ValueTuple_2[int, str]: ...
    def Read(self) -> ValueTuple_2[int, str]: ...


class DXFStreamWriter(IDisposable):
    @classmethod
    @property
    def CurrentFileFormatVersion(cls) -> int: ...
    def Dispose(self) -> None: ...
    def EndComplexEntity(self) -> None: ...
    def EndSection(self) -> None: ...
    def StartComplexEntity(self) -> None: ...
    def StartSection(self, sectionName: str, numberOfElements: int) -> None: ...
    def WriteBase64(self, code: UserSaveCode, content: Array_1[int]) -> None: ...
    def WriteEOF(self) -> None: ...
    def WritePath(self, code: ResourceSaveCode, content: str) -> None: ...
    def WriteUnstructured(self, content: str) -> None: ...
    def WriteVersionSection(self) -> None: ...
    # Skipped Write due to it being static, abstract and generic.

    Write : Write_MethodGroup
    class Write_MethodGroup:
        def __getitem__(self, t:typing.Type[Write_1_T1]) -> Write_1[Write_1_T1]: ...

        Write_1_T1 = typing.TypeVar('Write_1_T1')
        class Write_1(typing.Generic[Write_1_T1]):
            Write_1_T = DXFStreamWriter.Write_MethodGroup.Write_1_T1
            @typing.overload
            def __call__(self, code: UserComponentListSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: DataMappingSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: GeometryRelationSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: UserSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ComponentAccessTrackerSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: CalculatorMappingSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ComponentInstanceSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ComponentSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ParameterSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ParamStructCommonSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: MultiValueSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: GeoMapSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: SitePlannerSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: CalculationSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ChatItemSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ResourceSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: AssetSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: FlowNetworkSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: SimNetworkSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ProjectSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: ValueMappingSaveCode, content: Write_1_T) -> None:...
            @typing.overload
            def __call__(self, code: TaxonomySaveCode, content: Write_1_T) -> None:...


    # Skipped WriteArray due to it being static, abstract and generic.

    WriteArray : WriteArray_MethodGroup
    class WriteArray_MethodGroup:
        def __getitem__(self, t:typing.Type[WriteArray_1_T1]) -> WriteArray_1[WriteArray_1_T1]: ...

        WriteArray_1_T1 = typing.TypeVar('WriteArray_1_T1')
        class WriteArray_1(typing.Generic[WriteArray_1_T1]):
            WriteArray_1_T = DXFStreamWriter.WriteArray_MethodGroup.WriteArray_1_T1
            @typing.overload
            def __call__(self, code: TaxonomySaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: UserComponentListSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: GeometryRelationSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ResourceSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ChatItemSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: DataMappingSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: CalculatorMappingSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ComponentInstanceSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: CalculationSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ComponentSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ParamStructCommonSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: GeoMapSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: MultiValueSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: SitePlannerSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: AssetSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: FlowNetworkSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ValueMappingSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: SimNetworkSaveCode, collection: IEnumerable_1[WriteArray_1_T], itemSerializer: Action_2[WriteArray_1_T, DXFStreamWriter]) -> None:...


    # Skipped WriteEntitySequence due to it being static, abstract and generic.

    WriteEntitySequence : WriteEntitySequence_MethodGroup
    class WriteEntitySequence_MethodGroup:
        def __getitem__(self, t:typing.Type[WriteEntitySequence_1_T1]) -> WriteEntitySequence_1[WriteEntitySequence_1_T1]: ...

        WriteEntitySequence_1_T1 = typing.TypeVar('WriteEntitySequence_1_T1')
        class WriteEntitySequence_1(typing.Generic[WriteEntitySequence_1_T1]):
            WriteEntitySequence_1_T = DXFStreamWriter.WriteEntitySequence_MethodGroup.WriteEntitySequence_1_T1
            @typing.overload
            def __call__(self, code: DataMappingSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ChatItemSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ComponentInstanceSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ComponentSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: SitePlannerSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ResourceSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: AssetSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: FlowNetworkSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: SimNetworkSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: ValueMappingSaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...
            @typing.overload
            def __call__(self, code: TaxonomySaveCode, collection: IEnumerable_1[WriteEntitySequence_1_T], itemSerializer: Action_2[WriteEntitySequence_1_T, DXFStreamWriter]) -> None:...


    # Skipped WriteGlobalId due to it being static, abstract and generic.

    WriteGlobalId : WriteGlobalId_MethodGroup
    class WriteGlobalId_MethodGroup:
        @typing.overload
        def __call__(self, code: CalculatorMappingSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: DataMappingSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: ComponentInstanceSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: GeometryRelationSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: MultiValueSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: ParameterSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: SitePlannerSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: GeoMapSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: ParamStructCommonSaveCode, globalId: Guid, currentProject: Guid) -> None:...
        @typing.overload
        def __call__(self, code: ValueMappingSaveCode, globalId: Guid, currentProject: Guid) -> None:...

    # Skipped WriteMultilineText due to it being static, abstract and generic.

    WriteMultilineText : WriteMultilineText_MethodGroup
    class WriteMultilineText_MethodGroup:
        @typing.overload
        def __call__(self, code: ComponentSaveCode, text: str) -> None:...
        @typing.overload
        def __call__(self, code: MultiValueSaveCode, text: str) -> None:...
        @typing.overload
        def __call__(self, code: TaxonomySaveCode, text: str) -> None:...

    # Skipped WriteNestedList due to it being static, abstract and generic.

    WriteNestedList : WriteNestedList_MethodGroup
    class WriteNestedList_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[WriteNestedList_2_T1], typing.Type[WriteNestedList_2_T2]]) -> WriteNestedList_2[WriteNestedList_2_T1, WriteNestedList_2_T2]: ...

        WriteNestedList_2_T1 = typing.TypeVar('WriteNestedList_2_T1')
        WriteNestedList_2_T2 = typing.TypeVar('WriteNestedList_2_T2')
        class WriteNestedList_2(typing.Generic[WriteNestedList_2_T1, WriteNestedList_2_T2]):
            WriteNestedList_2_T = DXFStreamWriter.WriteNestedList_MethodGroup.WriteNestedList_2_T1
            WriteNestedList_2_U = DXFStreamWriter.WriteNestedList_MethodGroup.WriteNestedList_2_T2
            def __call__(self, code: MultiValueSaveCode, lists: IEnumerable_1[WriteNestedList_2_T], itemSerializer: Action_3[WriteNestedList_2_U, int, DXFStreamWriter]) -> None:...




class DXFStructArrayEntryParserElement_GenericClasses(abc.ABCMeta):
    Generic_DXFStructArrayEntryParserElement_GenericClasses_DXFStructArrayEntryParserElement_1_T = typing.TypeVar('Generic_DXFStructArrayEntryParserElement_GenericClasses_DXFStructArrayEntryParserElement_1_T')
    def __getitem__(self, types : typing.Type[Generic_DXFStructArrayEntryParserElement_GenericClasses_DXFStructArrayEntryParserElement_1_T]) -> typing.Type[DXFStructArrayEntryParserElement_1[Generic_DXFStructArrayEntryParserElement_GenericClasses_DXFStructArrayEntryParserElement_1_T]]: ...

DXFStructArrayEntryParserElement : DXFStructArrayEntryParserElement_GenericClasses

DXFStructArrayEntryParserElement_1_T = typing.TypeVar('DXFStructArrayEntryParserElement_1_T')
class DXFStructArrayEntryParserElement_1(typing.Generic[DXFStructArrayEntryParserElement_1_T], DXFEntryParserElement, IDXFStructArrayEntryParserElement):
    @property
    def Code(self) -> int: ...
    @property
    def Elements(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class EOFParserElement:
    def Parse(self, reader: DXFStreamReader) -> None: ...


class FlowNetworkSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    CONTENT_ID : FlowNetworkSaveCode # 1501
    IS_VALID : FlowNetworkSaveCode # 1502
    POSITION_X : FlowNetworkSaveCode # 1503
    POSITION_Y : FlowNetworkSaveCode # 1504
    START_NODE_LOCALID : FlowNetworkSaveCode # 1505
    END_NODE_LOCALID : FlowNetworkSaveCode # 1506
    NAME : FlowNetworkSaveCode # 1507
    DESCRIPTION : FlowNetworkSaveCode # 1508
    MANAGER : FlowNetworkSaveCode # 1509
    TIMESTAMP : FlowNetworkSaveCode # 1510
    CONTAINED_NODES : FlowNetworkSaveCode # 1511
    CONTAINED_EDGES : FlowNetworkSaveCode # 1512
    CONTAINED_NETWORKS : FlowNetworkSaveCode # 1513
    NODE_SOURCE : FlowNetworkSaveCode # 1514
    NODE_SINK : FlowNetworkSaveCode # 1515
    CALC_RULES : FlowNetworkSaveCode # 1516
    CALC_RULE_SUFFIX_OPERANDS : FlowNetworkSaveCode # 1517
    CALC_RULE_SUFFIX_RESULT : FlowNetworkSaveCode # 1518
    CALC_RULE_DIRECTION : FlowNetworkSaveCode # 1519
    CALC_RULE_OPERATOR : FlowNetworkSaveCode # 1520
    GEOM_REP : FlowNetworkSaveCode # 1521
    GEOM_REP_FILE_KEY : FlowNetworkSaveCode # 1531
    GEOM_REP_GEOM_ID : FlowNetworkSaveCode # 1532
    IS_DIRECTED : FlowNetworkSaveCode # 1533
    CONTENT_LOCATION : FlowNetworkSaveCode # 1534
    START_NODE_GLOBALID : FlowNetworkSaveCode # 1535
    END_NODE_GLOBALID : FlowNetworkSaveCode # 1536


class GeoMapSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    MAP_PATH : GeoMapSaveCode # 10001
    GEOREFS : GeoMapSaveCode # 10002
    IMAGEPOS_X : GeoMapSaveCode # 10003
    IMAGEPOS_Y : GeoMapSaveCode # 10004
    LONGITUDE : GeoMapSaveCode # 10005
    LATITUDE : GeoMapSaveCode # 10006
    HEIGHT : GeoMapSaveCode # 10007
    MAP_PROJECT_ID : GeoMapSaveCode # 10008
    MAP_RESOURCE_ID : GeoMapSaveCode # 10009


class GeometryRelationSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    GEOMETRY_RELATION_TYPE_GLOBAL_ID : GeometryRelationSaveCode # 23001
    GEOMETRY_RELATION_TYPE_LOCAL_ID : GeometryRelationSaveCode # 23002
    GEOMETRY_RELATION_SOURCE_PROJECT_ID : GeometryRelationSaveCode # 23003
    GEOMETRY_RELATION_SOURCE_FILE_ID : GeometryRelationSaveCode # 23004
    GEOMETRY_RELATION_SOURCE_GEOMETRY_ID : GeometryRelationSaveCode # 23005
    GEOMETRY_RELATION_TARGET_PROJECT_ID : GeometryRelationSaveCode # 23006
    GEOMETRY_RELATION_TARGET_FILE_ID : GeometryRelationSaveCode # 23007
    GEOMETRY_RELATION_TARGET_GEOMETRY_ID : GeometryRelationSaveCode # 23008
    GEOMETRY_RELATION_IS_AUTOGENERATED : GeometryRelationSaveCode # 23009
    GEOMETRY_RELATION_FILE_MAPPINGS : GeometryRelationSaveCode # 23101
    GEOMETRY_RELATION_FILE_MAPPING_FILE_ID : GeometryRelationSaveCode # 23102
    GEOMETRY_RELATION_FILE_MAPPING_PATH : GeometryRelationSaveCode # 23103


class IDXFEntityParserElementBase(typing.Protocol):
    @property
    def Entries(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class IDXFEntitySequenceEntryParserEntry(typing.Protocol):
    @property
    def Entities(self) -> IEnumerable_1[IDXFEntityParserElementBase]: ...


class IDXFStructArrayEntryParserElement(typing.Protocol):
    @property
    def Elements(self) -> IEnumerable_1[DXFEntryParserElement]: ...


class ImportantParamVisSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ID : ImportantParamVisSaveCode # 5001
    POSITION_X : ImportantParamVisSaveCode # 5002
    POSITION_Y : ImportantParamVisSaveCode # 5003
    COLOR_R : ImportantParamVisSaveCode # 5004
    COLOR_G : ImportantParamVisSaveCode # 5005
    COLOR_B : ImportantParamVisSaveCode # 5006
    COLOR_A : ImportantParamVisSaveCode # 5007
    INDEX : ImportantParamVisSaveCode # 5008


class MultiValueSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    MVDATA_COLUMN_COUNT : MultiValueSaveCode # 901
    MV_TYPE : MultiValueSaveCode # 1101
    MV_CANINTERPOLATE : MultiValueSaveCode # 1102
    MV_NAME : MultiValueSaveCode # 1103
    MV_UNIT_X : MultiValueSaveCode # 1104
    MV_UNIT_Y : MultiValueSaveCode # 1105
    MV_UNIT_Z : MultiValueSaveCode # 1106
    MV_NRX : MultiValueSaveCode # 1107
    MV_MIN_X : MultiValueSaveCode # 1108
    MV_MAX_X : MultiValueSaveCode # 1109
    MV_NRY : MultiValueSaveCode # 1110
    MV_MIN_Y : MultiValueSaveCode # 1111
    MV_MAX_Y : MultiValueSaveCode # 1112
    MV_NRZ : MultiValueSaveCode # 1113
    MV_MIN_Z : MultiValueSaveCode # 1114
    MV_MAX_Z : MultiValueSaveCode # 1115
    MV_COL_NAMES : MultiValueSaveCode # 1116
    MV_XAXIS : MultiValueSaveCode # 1116
    MV_YAXIS : MultiValueSaveCode # 1117
    MV_COL_UNITS : MultiValueSaveCode # 1117
    MV_ZAXIS : MultiValueSaveCode # 1118
    MVDATA_ROW_COUNT : MultiValueSaveCode # 1119
    MV_ROW_NAMES : MultiValueSaveCode # 1120
    ADDITIONAL_INFO : MultiValueSaveCode # 1121
    MV_DATA : MultiValueSaveCode # 1122
    MV_ROW_UNITS : MultiValueSaveCode # 1123
    MVDisplayVector_NUMDIM : MultiValueSaveCode # 1200
    MVDisplayVector_CELL_INDEX_X : MultiValueSaveCode # 1201
    MVDisplayVector_CELL_INDEX_Y : MultiValueSaveCode # 1202
    MVDisplayVector_CELL_INDEX_Z : MultiValueSaveCode # 1203
    MVDisplayVector_CELL_INDEX_W : MultiValueSaveCode # 1204
    MVDisplayVector_POS_IN_CELL_REL_X : MultiValueSaveCode # 1205
    MVDisplayVector_POS_IN_CELL_REL_Y : MultiValueSaveCode # 1206
    MVDisplayVector_POS_IN_CELL_REL_Z : MultiValueSaveCode # 1207
    MVDisplayVector_POS_IN_CELL_ABS_X : MultiValueSaveCode # 1208
    MVDisplayVector_POS_IN_CELL_ABS_Y : MultiValueSaveCode # 1209
    MVDisplayVector_POS_IN_CELL_ABS_Z : MultiValueSaveCode # 1210
    MVDisplayVector_VALUE : MultiValueSaveCode # 1211
    MVDisplayVector_CELL_SIZE_W : MultiValueSaveCode # 1212
    MVDisplayVector_CELL_SIZE_H : MultiValueSaveCode # 1213
    MVSRC_GRAPHNAME : MultiValueSaveCode # 1214
    MVSRC_AXIS_X : MultiValueSaveCode # 1215
    MVSRC_AXIS_Y : MultiValueSaveCode # 1216
    MVSRC_AXIS_Z : MultiValueSaveCode # 1217
    MVSRC_LOCALID : MultiValueSaveCode # 1218
    MVSRC_GLOBALID : MultiValueSaveCode # 1219
    GEOSRC_PROPERTY : MultiValueSaveCode # 1220
    GEOSRC_FILTER : MultiValueSaveCode # 1221
    GEOSRC_FILTER_ENTRY_GLOBAL_ID : MultiValueSaveCode # 1222
    GEOSRC_FILTER_ENTRY_LOCAL_ID : MultiValueSaveCode # 1223


class ParameterSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NAME : ParameterSaveCode # 1001
    UNIT : ParameterSaveCode # 1002
    CATEGORY : ParameterSaveCode # 1003
    PROPAGATION : ParameterSaveCode # 1004
    VALUE_MIN : ParameterSaveCode # 1005
    VALUE_MAX : ParameterSaveCode # 1006
    VALUE_CURRENT : ParameterSaveCode # 1007
    IS_WITHIN_BOUNDS : ParameterSaveCode # 1008
    VALUE_FIELD_REF : ParameterSaveCode # 1009
    VALUE_TEXT : ParameterSaveCode # 1010
    IS_IMPORTANT : ParameterSaveCode # 1011
    ALLOWED_OPERATIONS : ParameterSaveCode # 1012
    IS_AUTOGENERATED : ParameterSaveCode # 1013
    INSTANCE_PROPAGATION : ParameterSaveCode # 1014
    TAXONOMY_PROJECT_ID : ParameterSaveCode # 1015
    TAXONOMY_ID : ParameterSaveCode # 1016
    TAXONOMY_ENTRY_ID : ParameterSaveCode # 1017
    ENUMPARAM_TAXONOMYENTRY_VALUE_LOCALID : ParameterSaveCode # 1030
    ENUMPARAM_TAXOMYENTRY_VALUE_GLOBALID : ParameterSaveCode # 1031
    ENUMPARAM_PARENT_TAXONOMYENTRY_LOCALID : ParameterSaveCode # 1032
    ENUMPARAM_PARENT_TAXONOMYENTRY_GLOBALID : ParameterSaveCode # 1033
    PARAMTYPE : ParameterSaveCode # 1034


class ParamStructCommonSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    ENTITY_START : ParamStructCommonSaveCode # 0
    ENTITY_NAME : ParamStructCommonSaveCode # 2
    COORDS_X : ParamStructCommonSaveCode # 10
    COORDS_Y : ParamStructCommonSaveCode # 20
    CLASS_NAME : ParamStructCommonSaveCode # 100
    ENTITY_GLOBAL_ID : ParamStructCommonSaveCode # 899
    ENTITY_LOCAL_ID : ParamStructCommonSaveCode # 900
    NUMBER_OF : ParamStructCommonSaveCode # 901
    TIME_STAMP : ParamStructCommonSaveCode # 902
    ENTITY_REF : ParamStructCommonSaveCode # 903
    ENTITY_KEY : ParamStructCommonSaveCode # 904
    STRING_VALUE : ParamStructCommonSaveCode # 909
    X_VALUE : ParamStructCommonSaveCode # 910
    Y_VALUE : ParamStructCommonSaveCode # 920
    Z_VALUE : ParamStructCommonSaveCode # 930
    W_VALUE : ParamStructCommonSaveCode # 940
    V5_VALUE : ParamStructCommonSaveCode # 950
    V6_VALUE : ParamStructCommonSaveCode # 960
    V7_VALUE : ParamStructCommonSaveCode # 970
    V8_VALUE : ParamStructCommonSaveCode # 980
    V9_VALUE : ParamStructCommonSaveCode # 990
    V10_VALUE : ParamStructCommonSaveCode # 1000
    INVALID_CODE : ParamStructCommonSaveCode # -11


class ParamStructFileExtensions(abc.ABC):
    FILE_EXT_COMPONENTS : str
    FILE_EXT_COMPONENTS_PUBLIC : str
    FILE_EXT_EXCEL_TOOL_COLLECTION : str
    FILE_EXT_GEOMAP : str
    FILE_EXT_GEOMETRY_INTERNAL : str
    FILE_EXT_GEOMETRY_RELATIONS : str
    FILE_EXT_GEOMETRY_RELATIONS_FILE_MAPPINGS : str
    FILE_EXT_IMAGES : str
    FILE_EXT_LINKS : str
    FILE_EXT_MASTER : str
    FILE_EXT_META : str
    FILE_EXT_MULTIVALUES : str
    FILE_EXT_MULTIVALUES_PUBLIC : str
    FILE_EXT_PARAMETERS : str
    FILE_EXT_PROJECT : str
    FILE_EXT_PROJECT_COMPACT : str
    FILE_EXT_PROJECT_COMPACT_BACKUP : str
    FILE_EXT_PUBLIC_PROJECT_PATHS : str
    FILE_EXT_SITEPLANNER : str
    FILE_EXT_TAXONOMY : str
    FILE_EXT_USERS : str
    PUBLIC_PROJECT_PATHS_SUFFIX : str
    @staticmethod
    def GetAllManagedFileExtensions() -> List_1[str]: ...


class ParamStructTypes(abc.ABC):
    ACCESS_ACTION : str
    ACCESS_PROFILE : str
    ACCESS_TRACKER : str
    ASSET_DOCU : str
    ASSET_GEOM : str
    ASSET_MANAGER : str
    ASSET_SECTION : str
    BIG_TABLE : str
    CALCULATION : str
    CHAT_ITEM : str
    CHAT_SEQ : str
    COLOR_IN_BYTES : str
    COLOR_MAP_MULTI_LINEAR_GRADIENT : str
    COLOR_MAP_MULTI_THRESHOLD : str
    COMMON_ACCESS_MARKER_SECTION : str
    COMMON_EXCEL_SECTION : str
    COMPONENT : str
    COMPONENT_INSTANCE : str
    CONVERSATIONS_SECTION : str
    DATAMAPPING_RULE_COMPONENT : str
    DATAMAPPING_RULE_FACE : str
    DATAMAPPING_RULE_INSTANCE : str
    DATAMAPPING_RULE_PARAMETER : str
    DATAMAPPING_RULE_READ : str
    DATAMAPPING_RULE_VOLUME : str
    DATAMAPPING_TOOL : str
    DATAMAPPINGTOOL_SECTION : str
    DELIMITER_WITHIN_ENTRY : str
    DELIMITER_WITHIN_ENTRY_BEFORE_V18 : str
    END_OF_SUBLIST : int
    ENTITY_CONTINUE : str
    ENTITY_SECTION : str
    ENTITY_SEQUENCE : str
    EOF : str
    EXCEL_DATA_RESULT : str
    EXCEL_MAPPING : str
    EXCEL_MAPPING_COL : str
    EXCEL_RULE : str
    EXCEL_SECTION : str
    EXCEL_TOOL : str
    EXCEL_UNMAPPING : str
    FILE_VERSION : str
    FLOWNETWORK : str
    FLOWNETWORK_EDGE : str
    FLOWNETWORK_NODE : str
    FUNCTION_FIELD : str
    GEOMAP : str
    GEOMAP_SECTION : str
    GEOMETRY_RELATION : str
    GEOMETRY_RELATION_FILE_MAPPING : str
    GEOMETRY_RELATION_FILE_MAPPING_SECTION : str
    GEOMETRY_RELATION_SECTION : str
    IMPORTANT_SECTION : str
    INSTANCE_PLACEMENT_GEOMETRY : str
    INSTANCE_PLACEMENT_NETWORK : str
    INSTANCE_PLACEMENT_SIMNETWORK : str
    IPARAM_VIS : str
    LIST_CONTINUE : int
    LIST_END : int
    MAPPING_TO_COMP : str
    META_SECTION : str
    MULTI_LINK : str
    MULTI_LINK_SECTION : str
    NETWORK_SECTION : str
    PARAMETER : str
    PREFILTER_AVERAGE : str
    PREFILTER_DEFAULT : str
    PREFILTER_MAXIMUM : str
    PREFILTER_MINIMUM : str
    PREFILTER_TIMELINE : str
    PROJECT_METADATA : str
    RESOURCE_DIR : str
    RESOURCE_FILE : str
    RESOURCE_LINK : str
    SECTION_END : str
    SECTION_START : str
    SEQUENCE_END : str
    SIMNETWORK : str
    SIMNETWORK_BLOCK : str
    SIMNETWORK_CONNECTOR : str
    SIMNETWORK_PORT : str
    SIMNETWORK_SECTION : str
    SIMVALUEMAPPING_SECTION : str
    SITEPLANNER : str
    SITEPLANNER_SECTION : str
    TAXONOMY : str
    TAXONOMY_ENTRY : str
    TAXONOMY_SECTION : str
    TYPED_COMPONENT : str
    USER : str
    USER_LIST : str
    USER_SECTION : str
    USERCOMPONENTLIST_SECTION : str
    VALUE_FIELD : str
    VALUEMAPPING : str
    VERSION_SECTION : str


class ProjectSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    PROJECT_ID : ProjectSaveCode # 200001
    NAME_OF_PUBLIC_VALUE_FILE : ProjectSaveCode # 200002
    NAME_OF_PUBLIC_COMPS_FILE : ProjectSaveCode # 200003
    NR_OF_CHILD_PROJECTS : ProjectSaveCode # 200004
    CHILD_PROJECT_ID : ProjectSaveCode # 200005
    CHILD_PROJECT_REL_PATH : ProjectSaveCode # 200006


class ResourceSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    RESOURCE_USER : ResourceSaveCode # 7201
    RESOURCE_KEY : ResourceSaveCode # 7202
    RESOURCE_NAME : ResourceSaveCode # 7203
    RESOURCE_RELATIVE_PATH : ResourceSaveCode # 7204
    RESOURCE_ANCHOR : ResourceSaveCode # 7205
    RESOURCE_FULL_PATH : ResourceSaveCode # 7206
    RESOURCE_CHILDREN : ResourceSaveCode # 7207
    RESOURCE_PROBLEM : ResourceSaveCode # 7208
    RESOURCE_HAS_PARENT : ResourceSaveCode # 7211
    RESOURCE_VISIBILITY : ResourceSaveCode # 7212
    RESOURCE_TAGS : ResourceSaveCode # 7213
    RESOURCE_TAGS_ENTRY_GLOBAL_ID : ResourceSaveCode # 7214
    RESOURCE_TAGS_ENTRY_LOCAL_ID : ResourceSaveCode # 7215


class SaveCodeNotInUseAttribute(Attribute):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, message: str) -> None: ...
    @property
    def TypeId(self) -> typing.Any: ...


class SimNetworkSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    BLOCKS : SimNetworkSaveCode # 9001
    POSITION_X : SimNetworkSaveCode # 9503
    POSITION_Y : SimNetworkSaveCode # 9504
    PORTS : SimNetworkSaveCode # 9505
    PORT_TYPE : SimNetworkSaveCode # 9506
    SUBNETWORKS : SimNetworkSaveCode # 9509
    SOURCE_PORT : SimNetworkSaveCode # 9511
    TARGET_PORT : SimNetworkSaveCode # 9512
    CONNECTORS : SimNetworkSaveCode # 9513
    GEOM_REP_FILE_KEY : SimNetworkSaveCode # 9514
    GEOM_REP_GEOM_ID : SimNetworkSaveCode # 9515
    GEOM_REP_INDEX : SimNetworkSaveCode # 9516
    SIMBLOCK_ISSTATIC : SimNetworkSaveCode # 9517
    COLOR : SimNetworkSaveCode # 9518
    WIDTH : SimNetworkSaveCode # 9519
    HEIGHT : SimNetworkSaveCode # 9520
    CONTROL_POINTS : SimNetworkSaveCode # 9521


class SitePlannerSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    GEOMAPS : SitePlannerSaveCode # 11001
    GEOMAP_PATH : SitePlannerSaveCode # 11002
    BUILDINGS : SitePlannerSaveCode # 11003
    BUILDING_INDEX : SitePlannerSaveCode # 11004
    BUILDING_GEOMETRYMODEL_PATH : SitePlannerSaveCode # 11005
    BUILDING_CUSTOM_COLOR : SitePlannerSaveCode # 11006
    BUILDING_ID : SitePlannerSaveCode # 11007
    ELEVATION_PROVIDER_TYPE : SitePlannerSaveCode # 11008
    GRID_CELL_SIZE : SitePlannerSaveCode # 11009
    VALUE_MAPPING_INDEX_USAGE : SitePlannerSaveCode # 11010
    VALUE_MAPPING_COLOR_MAP_TYPE : SitePlannerSaveCode # 11011
    VALUE_MAPPING_COLOR_MAP_PARAMS : SitePlannerSaveCode # 11012
    VALUE_MAPPING_PREFILTER_TYPE : SitePlannerSaveCode # 11013
    VALUE_MAPPING_PREFILTER_PARAMS : SitePlannerSaveCode # 11014
    VALUE_MAPPING_VALUE_TABLE_KEY : SitePlannerSaveCode # 11015
    VALUE_MAPPING_ASSOCIATIONS : SitePlannerSaveCode # 11016
    VALUE_MAPPING_ASSOCIATION_INDEX : SitePlannerSaveCode # 11017
    VALUE_MAPPING_ASSOCIATION_NAME : SitePlannerSaveCode # 11018
    VALUE_MAPPING_ACTIVE_ASSOCIATION_INDEX : SitePlannerSaveCode # 11019
    VALUE_MAPPING_VALUE_TABLE_LOCATION : SitePlannerSaveCode # 11020
    GEOMAP_PROJECT_ID : SitePlannerSaveCode # 11021
    GEOMAP_RESOURCE_ID : SitePlannerSaveCode # 11022
    BUILDING_GEOMETRYMODEL_PROJECT_ID : SitePlannerSaveCode # 11023
    BUILDING_GEOMETRYMODEL_RESOURCE_ID : SitePlannerSaveCode # 11024
    VALUE_MAPPING_COLOR_MAP : SitePlannerSaveCode # 11025
    VALUE_MAPPING_PREFILTER : SitePlannerSaveCode # 11026
    VALUE_MAPPING_COLOR_MAP_MARKER : SitePlannerSaveCode # 11027
    VALUE_MAPPING_COLOR_MAP_MARKER_VALUE : SitePlannerSaveCode # 11028
    VALUE_MAPPING_COLOR_MAP_MARKER_COLOR : SitePlannerSaveCode # 11029
    VALUE_MAPPING_PREFILTER_TIMELINE_CURRENT : SitePlannerSaveCode # 11030
    VALUE_MAPPING_GLOBAL_ID : SitePlannerSaveCode # 11031
    VALUE_MAPPING_LOCAL_ID : SitePlannerSaveCode # 11032


class TaxonomySaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TAXONOMY_ENTRIES : TaxonomySaveCode # 22001
    TAXONOMY_DESCRIPTION : TaxonomySaveCode # 22002
    TAXONOMY_ENTRY_KEY : TaxonomySaveCode # 22003
    TAXONOMY_KEY : TaxonomySaveCode # 22004
    TAXONOMY_IS_READONLY : TaxonomySaveCode # 22005
    TAXONOMY_IS_DELETABLE : TaxonomySaveCode # 22006
    TAXONOMY_SUPPORTED_LANGUAGES : TaxonomySaveCode # 22100
    TAXONOMY_LANGUAGE : TaxonomySaveCode # 22101
    TAXONOMY_LOCALIZATIONS : TaxonomySaveCode # 22102
    TAXONOMY_LOCALIZATION_CULTURE : TaxonomySaveCode # 22103
    TAXONOMY_LOCALIZATION_NAME : TaxonomySaveCode # 22104
    TAXONOMY_LOCALIZATION_DESCRIPTION : TaxonomySaveCode # 22105


class TypedComponentSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    TYPE_NAME : TypedComponentSaveCode # 1451
    TYPE_VALIDATOR_NAME : TypedComponentSaveCode # 1452


class UserComponentListSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    NAME : UserComponentListSaveCode # 21001
    ROOT_COMPONENTS : UserComponentListSaveCode # 21002


class UserSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    USER_ID : UserSaveCode # 9001
    USER_NAME : UserSaveCode # 9002
    USER_PSW_HASH : UserSaveCode # 9003
    USER_ROLE : UserSaveCode # 9004
    USER_ENCRYPTION_KEY : UserSaveCode # 9005


class ValueMappingSaveCode(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    VALUE_MAPPING_INDEX_USAGE : ValueMappingSaveCode # 11010
    VALUE_MAPPING_TABLE_LOCALID : ValueMappingSaveCode # 11015
    VALUE_MAPPING_NAME : ValueMappingSaveCode # 11018
    VALUE_MAPPING_TABLE_GLOBALID : ValueMappingSaveCode # 11020
    VALUE_MAPPING_COLOR_MAP : ValueMappingSaveCode # 11025
    VALUE_MAPPING_PREFILTER : ValueMappingSaveCode # 11026
    VALUE_MAPPING_COLOR_MAP_MARKER : ValueMappingSaveCode # 11027
    VALUE_MAPPING_COLOR_MAP_MARKER_VALUE : ValueMappingSaveCode # 11028
    VALUE_MAPPING_COLOR_MAP_MARKER_COLOR : ValueMappingSaveCode # 11029

