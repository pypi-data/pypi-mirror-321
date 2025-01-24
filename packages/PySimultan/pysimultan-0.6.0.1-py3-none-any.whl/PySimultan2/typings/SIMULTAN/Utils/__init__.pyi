import typing, clr, abc
from System import ValueTuple_2, Predicate_1, ValueTuple_3, Func_2, Action_1, Version, TimeSpan, EventHandler, IEquatable_1, IAsyncResult, Delegate, Array_1
from System.IO import DirectoryInfo, FileInfo
from System.Collections.ObjectModel import ObservableCollection_1, Collection_1
from System.Collections.Generic import IEnumerable_1, List_1, IReadOnlyCollection_1, IList_1
from SIMULTAN.Data.SimMath import SimPoint3D, SimVector3D, SimMatrix3D, SimPoint, SimVector, SimQuaternion
from System.Collections import IList
from System.Collections.Specialized import NotifyCollectionChangedEventArgs
from System.Security import SecureString
from SIMULTAN.Data.Taxonomy import SimTaxonomy, SimTaxonomyEntryOrString
from System.Globalization import CultureInfo
from System.ComponentModel import ISynchronizeInvoke

class AdmissibilityQueries(abc.ABC):
    @staticmethod
    def DirectoryNameIsAdmissible(new_dir: DirectoryInfo, isAdmissible: Predicate_1[str], collisionFormat: str) -> ValueTuple_2[bool, str]: ...
    @staticmethod
    def FileNameIsAdmissible(new_file: FileInfo, isAdmissible: Predicate_1[str], collisionFormat: str) -> ValueTuple_2[bool, str]: ...
    @staticmethod
    def FindCopyName(name: str, isUsed: Predicate_1[str], copyFormat: str, copyCollisionFormat: str) -> str: ...
    @staticmethod
    def PropertyNameIsAdmissible(name: str, isAdmissible: Predicate_1[str], collisionNameFormat: str) -> ValueTuple_2[bool, str]: ...


class CollectionExtensions(abc.ABC):
    # Skipped AddRange due to it being static, abstract and generic.

    AddRange : AddRange_MethodGroup
    class AddRange_MethodGroup:
        def __getitem__(self, t:typing.Type[AddRange_1_T1]) -> AddRange_1[AddRange_1_T1]: ...

        AddRange_1_T1 = typing.TypeVar('AddRange_1_T1')
        class AddRange_1(typing.Generic[AddRange_1_T1]):
            AddRange_1_T = CollectionExtensions.AddRange_MethodGroup.AddRange_1_T1
            def __call__(self, collection: ObservableCollection_1[AddRange_1_T], items: IEnumerable_1[AddRange_1_T]) -> None:...


    # Skipped ArgMax due to it being static, abstract and generic.

    ArgMax : ArgMax_MethodGroup
    class ArgMax_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ArgMax_2_T1], typing.Type[ArgMax_2_T2]]) -> ArgMax_2[ArgMax_2_T1, ArgMax_2_T2]: ...

        ArgMax_2_T1 = typing.TypeVar('ArgMax_2_T1')
        ArgMax_2_T2 = typing.TypeVar('ArgMax_2_T2')
        class ArgMax_2(typing.Generic[ArgMax_2_T1, ArgMax_2_T2]):
            ArgMax_2_T = CollectionExtensions.ArgMax_MethodGroup.ArgMax_2_T1
            ArgMax_2_Key = CollectionExtensions.ArgMax_MethodGroup.ArgMax_2_T2
            def __call__(self, collection: IEnumerable_1[ArgMax_2_T], key: Func_2[ArgMax_2_T, ArgMax_2_Key]) -> ValueTuple_3[ArgMax_2_T, ArgMax_2_Key, int]:...


    # Skipped ArgMin due to it being static, abstract and generic.

    ArgMin : ArgMin_MethodGroup
    class ArgMin_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[ArgMin_2_T1], typing.Type[ArgMin_2_T2]]) -> ArgMin_2[ArgMin_2_T1, ArgMin_2_T2]: ...

        ArgMin_2_T1 = typing.TypeVar('ArgMin_2_T1')
        ArgMin_2_T2 = typing.TypeVar('ArgMin_2_T2')
        class ArgMin_2(typing.Generic[ArgMin_2_T1, ArgMin_2_T2]):
            ArgMin_2_T = CollectionExtensions.ArgMin_MethodGroup.ArgMin_2_T1
            ArgMin_2_Key = CollectionExtensions.ArgMin_MethodGroup.ArgMin_2_T2
            def __call__(self, collection: IEnumerable_1[ArgMin_2_T], key: Func_2[ArgMin_2_T, ArgMin_2_Key]) -> ValueTuple_3[ArgMin_2_T, ArgMin_2_Key, int]:...


    # Skipped Average due to it being static, abstract and generic.

    Average : Average_MethodGroup
    class Average_MethodGroup:
        def __getitem__(self, t:typing.Type[Average_1_T1]) -> Average_1[Average_1_T1]: ...

        Average_1_T1 = typing.TypeVar('Average_1_T1')
        class Average_1(typing.Generic[Average_1_T1]):
            Average_1_T = CollectionExtensions.Average_MethodGroup.Average_1_T1
            @typing.overload
            def __call__(self, enumerable: IEnumerable_1[Average_1_T], selector: Func_2[Average_1_T, SimPoint3D]) -> SimPoint3D:...
            @typing.overload
            def __call__(self, enumerable: IEnumerable_1[Average_1_T], selector: Func_2[Average_1_T, SimVector3D]) -> SimVector3D:...


    # Skipped DeepCopy due to it being static, abstract and generic.

    DeepCopy : DeepCopy_MethodGroup
    class DeepCopy_MethodGroup:
        def __getitem__(self, t:typing.Type[DeepCopy_1_T1]) -> DeepCopy_1[DeepCopy_1_T1]: ...

        DeepCopy_1_T1 = typing.TypeVar('DeepCopy_1_T1')
        class DeepCopy_1(typing.Generic[DeepCopy_1_T1]):
            DeepCopy_1_T = CollectionExtensions.DeepCopy_MethodGroup.DeepCopy_1_T1
            def __call__(self, source: List_1[List_1[DeepCopy_1_T]]) -> List_1[List_1[DeepCopy_1_T]]:...


    # Skipped DistinctBy due to it being static, abstract and generic.

    DistinctBy : DistinctBy_MethodGroup
    class DistinctBy_MethodGroup:
        def __getitem__(self, t:typing.Type[DistinctBy_1_T1]) -> DistinctBy_1[DistinctBy_1_T1]: ...

        DistinctBy_1_T1 = typing.TypeVar('DistinctBy_1_T1')
        class DistinctBy_1(typing.Generic[DistinctBy_1_T1]):
            DistinctBy_1_T = CollectionExtensions.DistinctBy_MethodGroup.DistinctBy_1_T1
            def __call__(self, enumerable: IEnumerable_1[DistinctBy_1_T], selector: Func_2[DistinctBy_1_T, typing.Any]) -> IEnumerable_1[DistinctBy_1_T]:...


    # Skipped FindIndex due to it being static, abstract and generic.

    FindIndex : FindIndex_MethodGroup
    class FindIndex_MethodGroup:
        def __getitem__(self, t:typing.Type[FindIndex_1_T1]) -> FindIndex_1[FindIndex_1_T1]: ...

        FindIndex_1_T1 = typing.TypeVar('FindIndex_1_T1')
        class FindIndex_1(typing.Generic[FindIndex_1_T1]):
            FindIndex_1_T = CollectionExtensions.FindIndex_MethodGroup.FindIndex_1_T1
            def __call__(self, list: IEnumerable_1[FindIndex_1_T], predicate: Predicate_1[FindIndex_1_T]) -> int:...


    # Skipped ForEach due to it being static, abstract and generic.

    ForEach : ForEach_MethodGroup
    class ForEach_MethodGroup:
        def __getitem__(self, t:typing.Type[ForEach_1_T1]) -> ForEach_1[ForEach_1_T1]: ...

        ForEach_1_T1 = typing.TypeVar('ForEach_1_T1')
        class ForEach_1(typing.Generic[ForEach_1_T1]):
            ForEach_1_T = CollectionExtensions.ForEach_MethodGroup.ForEach_1_T1
            @typing.overload
            def __call__(self, collection: ObservableCollection_1[ForEach_1_T], action: Action_1[ForEach_1_T]) -> None:...
            @typing.overload
            def __call__(self, collection: IReadOnlyCollection_1[ForEach_1_T], action: Action_1[ForEach_1_T]) -> None:...
            @typing.overload
            def __call__(self, collection: IEnumerable_1[ForEach_1_T], action: Action_1[ForEach_1_T]) -> None:...

        def __call__(self, collection: IList, action: Action_1[typing.Any]) -> None:...

    # Skipped HandleCollectionChanged due to it being static, abstract and generic.

    HandleCollectionChanged : HandleCollectionChanged_MethodGroup
    class HandleCollectionChanged_MethodGroup:
        def __getitem__(self, t:typing.Tuple[typing.Type[HandleCollectionChanged_2_T1], typing.Type[HandleCollectionChanged_2_T2]]) -> HandleCollectionChanged_2[HandleCollectionChanged_2_T1, HandleCollectionChanged_2_T2]: ...

        HandleCollectionChanged_2_T1 = typing.TypeVar('HandleCollectionChanged_2_T1')
        HandleCollectionChanged_2_T2 = typing.TypeVar('HandleCollectionChanged_2_T2')
        class HandleCollectionChanged_2(typing.Generic[HandleCollectionChanged_2_T1, HandleCollectionChanged_2_T2]):
            HandleCollectionChanged_2_TSource = CollectionExtensions.HandleCollectionChanged_MethodGroup.HandleCollectionChanged_2_T1
            HandleCollectionChanged_2_TTarget = CollectionExtensions.HandleCollectionChanged_MethodGroup.HandleCollectionChanged_2_T2
            def __call__(self, args: NotifyCollectionChangedEventArgs, target: IList_1[HandleCollectionChanged_2_TTarget], convert: Func_2[HandleCollectionChanged_2_TSource, HandleCollectionChanged_2_TTarget]) -> None:...


    # Skipped IndicesWhere due to it being static, abstract and generic.

    IndicesWhere : IndicesWhere_MethodGroup
    class IndicesWhere_MethodGroup:
        def __getitem__(self, t:typing.Type[IndicesWhere_1_T1]) -> IndicesWhere_1[IndicesWhere_1_T1]: ...

        IndicesWhere_1_T1 = typing.TypeVar('IndicesWhere_1_T1')
        class IndicesWhere_1(typing.Generic[IndicesWhere_1_T1]):
            IndicesWhere_1_T = CollectionExtensions.IndicesWhere_MethodGroup.IndicesWhere_1_T1
            def __call__(self, source: IEnumerable_1[IndicesWhere_1_T], predicate: Func_2[IndicesWhere_1_T, bool]) -> IEnumerable_1[int]:...


    # Skipped RemoveFirst due to it being static, abstract and generic.

    RemoveFirst : RemoveFirst_MethodGroup
    class RemoveFirst_MethodGroup:
        def __getitem__(self, t:typing.Type[RemoveFirst_1_T1]) -> RemoveFirst_1[RemoveFirst_1_T1]: ...

        RemoveFirst_1_T1 = typing.TypeVar('RemoveFirst_1_T1')
        class RemoveFirst_1(typing.Generic[RemoveFirst_1_T1]):
            RemoveFirst_1_T = CollectionExtensions.RemoveFirst_MethodGroup.RemoveFirst_1_T1
            @typing.overload
            def __call__(self, collection: Collection_1[RemoveFirst_1_T], predicate: Func_2[RemoveFirst_1_T, bool]) -> bool:...
            @typing.overload
            def __call__(self, collection: Collection_1[RemoveFirst_1_T], predicate: Func_2[RemoveFirst_1_T, bool], removed: clr.Reference[RemoveFirst_1_T]) -> bool:...


    # Skipped RemoveWhere due to it being static, abstract and generic.

    RemoveWhere : RemoveWhere_MethodGroup
    class RemoveWhere_MethodGroup:
        def __getitem__(self, t:typing.Type[RemoveWhere_1_T1]) -> RemoveWhere_1[RemoveWhere_1_T1]: ...

        RemoveWhere_1_T1 = typing.TypeVar('RemoveWhere_1_T1')
        class RemoveWhere_1(typing.Generic[RemoveWhere_1_T1]):
            RemoveWhere_1_T = CollectionExtensions.RemoveWhere_MethodGroup.RemoveWhere_1_T1
            @typing.overload
            def __call__(self, collection: Collection_1[RemoveWhere_1_T], predicate: Func_2[RemoveWhere_1_T, bool]) -> None:...
            @typing.overload
            def __call__(self, collection: IList_1[RemoveWhere_1_T], predicate: Func_2[RemoveWhere_1_T, bool]) -> None:...
            @typing.overload
            def __call__(self, collection: Collection_1[RemoveWhere_1_T], predicate: Func_2[RemoveWhere_1_T, bool], removeAction: Action_1[RemoveWhere_1_T]) -> None:...
            @typing.overload
            def __call__(self, collection: IList_1[RemoveWhere_1_T], predicate: Func_2[RemoveWhere_1_T, bool], removeAction: Action_1[RemoveWhere_1_T]) -> None:...


    # Skipped Split due to it being static, abstract and generic.

    Split : Split_MethodGroup
    class Split_MethodGroup:
        def __getitem__(self, t:typing.Type[Split_1_T1]) -> Split_1[Split_1_T1]: ...

        Split_1_T1 = typing.TypeVar('Split_1_T1')
        class Split_1(typing.Generic[Split_1_T1]):
            Split_1_T = CollectionExtensions.Split_MethodGroup.Split_1_T1
            def __call__(self, list: IEnumerable_1[Split_1_T], predicate: Predicate_1[Split_1_T]) -> ValueTuple_2[IEnumerable_1[Split_1_T], IEnumerable_1[Split_1_T]]:...


    # Skipped ToList due to it being static, abstract and generic.

    ToList : ToList_MethodGroup
    class ToList_MethodGroup:
        def __getitem__(self, t:typing.Type[ToList_1_T1]) -> ToList_1[ToList_1_T1]: ...

        ToList_1_T1 = typing.TypeVar('ToList_1_T1')
        class ToList_1(typing.Generic[ToList_1_T1]):
            ToList_1_T = CollectionExtensions.ToList_MethodGroup.ToList_1_T1
            def __call__(self, iList: IList) -> IList_1[ToList_1_T]:...


    # Skipped ToObservableCollection due to it being static, abstract and generic.

    ToObservableCollection : ToObservableCollection_MethodGroup
    class ToObservableCollection_MethodGroup:
        def __getitem__(self, t:typing.Type[ToObservableCollection_1_T1]) -> ToObservableCollection_1[ToObservableCollection_1_T1]: ...

        ToObservableCollection_1_T1 = typing.TypeVar('ToObservableCollection_1_T1')
        class ToObservableCollection_1(typing.Generic[ToObservableCollection_1_T1]):
            ToObservableCollection_1_T = CollectionExtensions.ToObservableCollection_MethodGroup.ToObservableCollection_1_T1
            def __call__(self, enumerable: IEnumerable_1[ToObservableCollection_1_T]) -> ObservableCollection_1[ToObservableCollection_1_T]:...


    # Skipped Transpose due to it being static, abstract and generic.

    Transpose : Transpose_MethodGroup
    class Transpose_MethodGroup:
        def __getitem__(self, t:typing.Type[Transpose_1_T1]) -> Transpose_1[Transpose_1_T1]: ...

        Transpose_1_T1 = typing.TypeVar('Transpose_1_T1')
        class Transpose_1(typing.Generic[Transpose_1_T1]):
            Transpose_1_T = CollectionExtensions.Transpose_MethodGroup.Transpose_1_T1
            def __call__(self, input: List_1[List_1[Transpose_1_T]]) -> List_1[List_1[Transpose_1_T]]:...


    # Skipped TryFirstOrDefault due to it being static, abstract and generic.

    TryFirstOrDefault : TryFirstOrDefault_MethodGroup
    class TryFirstOrDefault_MethodGroup:
        def __getitem__(self, t:typing.Type[TryFirstOrDefault_1_T1]) -> TryFirstOrDefault_1[TryFirstOrDefault_1_T1]: ...

        TryFirstOrDefault_1_T1 = typing.TypeVar('TryFirstOrDefault_1_T1')
        class TryFirstOrDefault_1(typing.Generic[TryFirstOrDefault_1_T1]):
            TryFirstOrDefault_1_T = CollectionExtensions.TryFirstOrDefault_MethodGroup.TryFirstOrDefault_1_T1
            def __call__(self, source: IEnumerable_1[TryFirstOrDefault_1_T], predicate: Predicate_1[TryFirstOrDefault_1_T], value: clr.Reference[TryFirstOrDefault_1_T]) -> bool:...


    # Skipped TryGetElementAt due to it being static, abstract and generic.

    TryGetElementAt : TryGetElementAt_MethodGroup
    class TryGetElementAt_MethodGroup:
        def __getitem__(self, t:typing.Type[TryGetElementAt_1_T1]) -> TryGetElementAt_1[TryGetElementAt_1_T1]: ...

        TryGetElementAt_1_T1 = typing.TypeVar('TryGetElementAt_1_T1')
        class TryGetElementAt_1(typing.Generic[TryGetElementAt_1_T1]):
            TryGetElementAt_1_T = CollectionExtensions.TryGetElementAt_MethodGroup.TryGetElementAt_1_T1
            def __call__(self, list: IEnumerable_1[TryGetElementAt_1_T], index: int, result: clr.Reference[TryGetElementAt_1_T]) -> bool:...




class CommonExtensions(abc.ABC):
    @staticmethod
    def ConvertToDoubleIfNumeric(value: typing.Any) -> float: ...
    @staticmethod
    def EqualsWithNan(d: float, other: float) -> bool: ...
    @staticmethod
    def GetVersion(version: Version, fieldCount: int) -> Version: ...
    @staticmethod
    def IsCollinear(v1: SimVector3D, v2: SimVector3D, threshold: float = ...) -> bool: ...
    @staticmethod
    def MatrixFromAxes(x: SimVector3D, y: SimVector3D, z: SimVector3D, p: SimPoint3D) -> SimMatrix3D: ...
    @staticmethod
    def SecureEquals(s1: SecureString, s2: SecureString) -> bool: ...
    @staticmethod
    def Transpose(m: SimMatrix3D) -> SimMatrix3D: ...
    # Skipped Clamp due to it being static, abstract and generic.

    Clamp : Clamp_MethodGroup
    class Clamp_MethodGroup:
        def __getitem__(self, t:typing.Type[Clamp_1_T1]) -> Clamp_1[Clamp_1_T1]: ...

        Clamp_1_T1 = typing.TypeVar('Clamp_1_T1')
        class Clamp_1(typing.Generic[Clamp_1_T1]):
            Clamp_1_T = CommonExtensions.Clamp_MethodGroup.Clamp_1_T1
            def __call__(self, val: Clamp_1_T, min: Clamp_1_T, max: Clamp_1_T) -> Clamp_1_T:...


    # Skipped InRange due to it being static, abstract and generic.

    InRange : InRange_MethodGroup
    class InRange_MethodGroup:
        def __getitem__(self, t:typing.Type[InRange_1_T1]) -> InRange_1[InRange_1_T1]: ...

        InRange_1_T1 = typing.TypeVar('InRange_1_T1')
        class InRange_1(typing.Generic[InRange_1_T1]):
            InRange_1_T = CommonExtensions.InRange_MethodGroup.InRange_1_T1
            def __call__(self, value: InRange_1_T, minRange: InRange_1_T, maxRange: InRange_1_T) -> bool:...




class IDispatcherTimer(typing.Protocol):
    @property
    def Interval(self) -> TimeSpan: ...
    @Interval.setter
    def Interval(self, value: TimeSpan) -> TimeSpan: ...
    @abc.abstractmethod
    def AddTickEventHandler(self, handler: EventHandler) -> None: ...
    @abc.abstractmethod
    def RemoveTickEventHandler(self, handler: EventHandler) -> None: ...
    @abc.abstractmethod
    def Start(self) -> None: ...
    @abc.abstractmethod
    def Stop(self) -> None: ...


class IDispatcherTimerFactory(typing.Protocol):
    @abc.abstractmethod
    def Create(self) -> IDispatcherTimer: ...


class IntIndex2D(IEquatable_1[IntIndex2D]):
    def __init__(self, x: int, y: int) -> None: ...
    @property
    def Item(self) -> int: ...
    @Item.setter
    def Item(self, value: int) -> int: ...
    @property
    def X(self) -> int: ...
    @X.setter
    def X(self, value: int) -> int: ...
    @property
    def Y(self) -> int: ...
    @Y.setter
    def Y(self, value: int) -> int: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, lhs: IntIndex2D, rhs: IntIndex2D) -> IntIndex2D: ...
    def __eq__(self, lhs: IntIndex2D, rhs: IntIndex2D) -> bool: ...
    def __ne__(self, lhs: IntIndex2D, rhs: IntIndex2D) -> bool: ...
    def __sub__(self, lhs: IntIndex2D, rhs: IntIndex2D) -> IntIndex2D: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: IntIndex2D) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class IntIndex3D(IEquatable_1[IntIndex3D]):
    def __init__(self, x: int, y: int, z: int) -> None: ...
    @property
    def Item(self) -> int: ...
    @Item.setter
    def Item(self, value: int) -> int: ...
    @property
    def X(self) -> int: ...
    @X.setter
    def X(self, value: int) -> int: ...
    @property
    def Y(self) -> int: ...
    @Y.setter
    def Y(self, value: int) -> int: ...
    @property
    def Z(self) -> int: ...
    @Z.setter
    def Z(self, value: int) -> int: ...
    def Equals(self, other: IntIndex3D) -> bool: ...
    def GetHashCode(self) -> int: ...


class IServicesProvider(typing.Protocol):
    # Skipped GetService due to it being static, abstract and generic.

    GetService : GetService_MethodGroup
    class GetService_MethodGroup:
        def __getitem__(self, t:typing.Type[GetService_1_T1]) -> GetService_1[GetService_1_T1]: ...

        GetService_1_T1 = typing.TypeVar('GetService_1_T1')
        class GetService_1(typing.Generic[GetService_1_T1]):
            GetService_1_T = IServicesProvider.GetService_MethodGroup.GetService_1_T1
            def __call__(self) -> GetService_1_T:...




class PointVectorExtensions(abc.ABC):
    @staticmethod
    def At(p: SimPoint3D, idx: int) -> float: ...
    @staticmethod
    def Divide(p: SimPoint3D, d: float) -> SimPoint3D: ...
    @staticmethod
    def Multiply(p: SimPoint3D, d: float) -> SimPoint3D: ...
    # Skipped Get due to it being static, abstract and generic.

    Get : Get_MethodGroup
    class Get_MethodGroup:
        @typing.overload
        def __call__(self, v: SimVector3D, idx: int) -> float:...
        @typing.overload
        def __call__(self, v: SimPoint3D, idx: int) -> float:...

    # Skipped XY due to it being static, abstract and generic.

    XY : XY_MethodGroup
    class XY_MethodGroup:
        @typing.overload
        def __call__(self, p: SimPoint3D) -> SimPoint:...
        @typing.overload
        def __call__(self, v: SimVector3D) -> SimVector:...



class Range3D:
    @typing.overload
    def __init__(self, minimum: SimPoint3D, maximum: SimPoint3D) -> None: ...
    @typing.overload
    def __init__(self, original: Range3D) -> None: ...
    @property
    def Maximum(self) -> SimPoint3D: ...
    @property
    def Minimum(self) -> SimPoint3D: ...
    # Skipped Contains due to it being static, abstract and generic.

    Contains : Contains_MethodGroup
    class Contains_MethodGroup:
        @typing.overload
        def __call__(self, position: SimPoint3D) -> bool:...
        @typing.overload
        def __call__(self, position: IntIndex3D) -> bool:...



class RowColumnIndex(IEquatable_1[RowColumnIndex]):
    def __init__(self, row: int, column: int) -> None: ...
    @property
    def Column(self) -> int: ...
    @Column.setter
    def Column(self, value: int) -> int: ...
    @property
    def Row(self) -> int: ...
    @Row.setter
    def Row(self, value: int) -> int: ...
    @staticmethod
    def FromIndex2D(index: IntIndex2D) -> RowColumnIndex: ...
    def GetHashCode(self) -> int: ...
    def __add__(self, lhs: RowColumnIndex, rhs: RowColumnIndex) -> RowColumnIndex: ...
    def __eq__(self, lhs: RowColumnIndex, rhs: RowColumnIndex) -> bool: ...
    def __ne__(self, lhs: RowColumnIndex, rhs: RowColumnIndex) -> bool: ...
    def __sub__(self, lhs: RowColumnIndex, rhs: RowColumnIndex) -> RowColumnIndex: ...
    def ToIndex2D(self) -> IntIndex2D: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: RowColumnIndex) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...



class RowColumnRange(IEquatable_1[RowColumnRange]):
    def __init__(self, rowStart: int, columnStart: int, rowCount: int, columnCount: int) -> None: ...
    @property
    def ColumnCount(self) -> int: ...
    @property
    def ColumnStart(self) -> int: ...
    @property
    def RowCount(self) -> int: ...
    @property
    def RowStart(self) -> int: ...
    def GetHashCode(self) -> int: ...
    def __eq__(self, lhs: RowColumnRange, rhs: RowColumnRange) -> bool: ...
    def __ne__(self, lhs: RowColumnRange, rhs: RowColumnRange) -> bool: ...
    # Skipped Equals due to it being static, abstract and generic.

    Equals : Equals_MethodGroup
    class Equals_MethodGroup:
        @typing.overload
        def __call__(self, other: RowColumnRange) -> bool:...
        @typing.overload
        def __call__(self, obj: typing.Any) -> bool:...

    # Skipped Merge due to it being static, abstract and generic.

    Merge : Merge_MethodGroup
    class Merge_MethodGroup:
        @typing.overload
        def __call__(self, lhs: RowColumnRange, rhs: RowColumnRange) -> RowColumnRange:...
        @typing.overload
        def __call__(self, lhs: RowColumnRange, rhs: RowColumnIndex) -> RowColumnRange:...



class ServicesProvider(IServicesProvider):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, serviceProvider: IServicesProvider) -> None: ...
    # Skipped AddService due to it being static, abstract and generic.

    AddService : AddService_MethodGroup
    class AddService_MethodGroup:
        def __getitem__(self, t:typing.Type[AddService_1_T1]) -> AddService_1[AddService_1_T1]: ...

        AddService_1_T1 = typing.TypeVar('AddService_1_T1')
        class AddService_1(typing.Generic[AddService_1_T1]):
            AddService_1_TServiceScope = ServicesProvider.AddService_MethodGroup.AddService_1_T1
            def __call__(self, service: AddService_1_TServiceScope) -> None:...


    # Skipped GetService due to it being static, abstract and generic.

    GetService : GetService_MethodGroup
    class GetService_MethodGroup:
        def __getitem__(self, t:typing.Type[GetService_1_T1]) -> GetService_1[GetService_1_T1]: ...

        GetService_1_T1 = typing.TypeVar('GetService_1_T1')
        class GetService_1(typing.Generic[GetService_1_T1]):
            GetService_1_T = ServicesProvider.GetService_MethodGroup.GetService_1_T1
            def __call__(self) -> GetService_1_T:...




class SimQuaternionExtensions(abc.ABC):
    @staticmethod
    def ToEulerAngles(q: SimQuaternion) -> SimVector3D: ...
    # Skipped CreateFromYawPitchRoll due to it being static, abstract and generic.

    CreateFromYawPitchRoll : CreateFromYawPitchRoll_MethodGroup
    class CreateFromYawPitchRoll_MethodGroup:
        @typing.overload
        def __call__(self, eulerAngles: SimVector3D) -> SimQuaternion:...
        @typing.overload
        def __call__(self, yaw: float, pitch: float, roll: float) -> SimQuaternion:...



class SystemTimerFactory(IDispatcherTimerFactory):
    def __init__(self) -> None: ...
    def Create(self) -> IDispatcherTimer: ...


class TaxonomyUtils(abc.ABC):
    @staticmethod
    def DuplicateLanguage(taxonomy: SimTaxonomy, source: CultureInfo, target: CultureInfo) -> bool: ...
    @staticmethod
    def GetLocalizedName(entry: SimTaxonomyEntryOrString, culture: CultureInfo) -> str: ...


class UnsyncedSynchronizationContext(ISynchronizeInvoke):
    def __init__(self) -> None: ...
    @property
    def InvokeRequired(self) -> bool: ...
    def BeginInvoke(self, method: Delegate, args: Array_1[typing.Any]) -> IAsyncResult: ...
    def EndInvoke(self, result: IAsyncResult) -> typing.Any: ...
    def Invoke(self, method: Delegate, args: Array_1[typing.Any]) -> typing.Any: ...

