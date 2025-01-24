import typing, clr, abc
from System.Collections.ObjectModel import ObservableCollection_1
from System.Collections.Generic import IEnumerable_1, IReadOnlyCollection_1, IReadOnlyDictionary_2, KeyValuePair_2, ICollection_1, IEnumerator_1, IDictionary_2
from System.Collections.Specialized import INotifyCollectionChanged
from System.ComponentModel import INotifyPropertyChanged
from System import Comparison_1

class ElectivelyObservableCollection_GenericClasses(abc.ABCMeta):
    Generic_ElectivelyObservableCollection_GenericClasses_ElectivelyObservableCollection_1_T = typing.TypeVar('Generic_ElectivelyObservableCollection_GenericClasses_ElectivelyObservableCollection_1_T')
    def __getitem__(self, types : typing.Type[Generic_ElectivelyObservableCollection_GenericClasses_ElectivelyObservableCollection_1_T]) -> typing.Type[ElectivelyObservableCollection_1[Generic_ElectivelyObservableCollection_GenericClasses_ElectivelyObservableCollection_1_T]]: ...

ElectivelyObservableCollection : ElectivelyObservableCollection_GenericClasses

ElectivelyObservableCollection_1_T = typing.TypeVar('ElectivelyObservableCollection_1_T')
class ElectivelyObservableCollection_1(typing.Generic[ElectivelyObservableCollection_1_T], ObservableCollection_1[ElectivelyObservableCollection_1_T], IReadOnlyObservableCollection_1[ElectivelyObservableCollection_1_T]):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, collection: IEnumerable_1[ElectivelyObservableCollection_1_T]) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> ElectivelyObservableCollection_1_T: ...
    @Item.setter
    def Item(self, value: ElectivelyObservableCollection_1_T) -> ElectivelyObservableCollection_1_T: ...
    @property
    def SuppressNotification(self) -> bool: ...
    @SuppressNotification.setter
    def SuppressNotification(self, value: bool) -> bool: ...


class IReadOnlyObservableCollection_GenericClasses(abc.ABCMeta):
    Generic_IReadOnlyObservableCollection_GenericClasses_IReadOnlyObservableCollection_1_T = typing.TypeVar('Generic_IReadOnlyObservableCollection_GenericClasses_IReadOnlyObservableCollection_1_T')
    def __getitem__(self, types : typing.Type[Generic_IReadOnlyObservableCollection_GenericClasses_IReadOnlyObservableCollection_1_T]) -> typing.Type[IReadOnlyObservableCollection_1[Generic_IReadOnlyObservableCollection_GenericClasses_IReadOnlyObservableCollection_1_T]]: ...

IReadOnlyObservableCollection : IReadOnlyObservableCollection_GenericClasses

IReadOnlyObservableCollection_1_T = typing.TypeVar('IReadOnlyObservableCollection_1_T')
class IReadOnlyObservableCollection_1(typing.Generic[IReadOnlyObservableCollection_1_T], IReadOnlyCollection_1[IReadOnlyObservableCollection_1_T], INotifyCollectionChanged, typing.Protocol):
    pass


class IReadonlyObservableDictionary_GenericClasses(abc.ABCMeta):
    Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TKey = typing.TypeVar('Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TKey')
    Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TValue = typing.TypeVar('Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TKey], typing.Type[Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TValue]]) -> typing.Type[IReadonlyObservableDictionary_2[Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TKey, Generic_IReadonlyObservableDictionary_GenericClasses_IReadonlyObservableDictionary_2_TValue]]: ...

IReadonlyObservableDictionary : IReadonlyObservableDictionary_GenericClasses

IReadonlyObservableDictionary_2_TKey = typing.TypeVar('IReadonlyObservableDictionary_2_TKey')
IReadonlyObservableDictionary_2_TValue = typing.TypeVar('IReadonlyObservableDictionary_2_TValue')
class IReadonlyObservableDictionary_2(typing.Generic[IReadonlyObservableDictionary_2_TKey, IReadonlyObservableDictionary_2_TValue], IReadOnlyDictionary_2[IReadonlyObservableDictionary_2_TKey, IReadonlyObservableDictionary_2_TValue], INotifyCollectionChanged, typing.Protocol):
    pass


class MultiDictionary_GenericClasses(abc.ABCMeta):
    Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TKey = typing.TypeVar('Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TKey')
    Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TValue = typing.TypeVar('Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TKey], typing.Type[Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TValue]]) -> typing.Type[MultiDictionary_2[Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TKey, Generic_MultiDictionary_GenericClasses_MultiDictionary_2_TValue]]: ...

MultiDictionary : MultiDictionary_GenericClasses

MultiDictionary_2_TKey = typing.TypeVar('MultiDictionary_2_TKey')
MultiDictionary_2_TValue = typing.TypeVar('MultiDictionary_2_TValue')
class MultiDictionary_2(typing.Generic[MultiDictionary_2_TKey, MultiDictionary_2_TValue], IEnumerable_1[KeyValuePair_2[MultiDictionary_2_TKey, IEnumerable_1[MultiDictionary_2_TValue]]]):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, original: MultiDictionary_2[MultiDictionary_2_TKey, MultiDictionary_2_TValue]) -> None: ...
    @property
    def Item(self) -> IEnumerable_1[MultiDictionary_2_TValue]: ...
    @property
    def Keys(self) -> ICollection_1[MultiDictionary_2_TKey]: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: MultiDictionary_2_TKey) -> bool: ...
    def GetEnumerator(self) -> IEnumerator_1[KeyValuePair_2[MultiDictionary_2_TKey, IEnumerable_1[MultiDictionary_2_TValue]]]: ...
    def TryGetValues(self, key: MultiDictionary_2_TKey, values: clr.Reference[IEnumerable_1[MultiDictionary_2_TValue]]) -> bool: ...
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup[MultiDictionary_2_TKey, MultiDictionary_2_TValue]
    Add_MethodGroup_MultiDictionary_2_TKey = typing.TypeVar('Add_MethodGroup_MultiDictionary_2_TKey')
    Add_MethodGroup_MultiDictionary_2_TValue = typing.TypeVar('Add_MethodGroup_MultiDictionary_2_TValue')
    class Add_MethodGroup(typing.Generic[Add_MethodGroup_MultiDictionary_2_TKey, Add_MethodGroup_MultiDictionary_2_TValue]):
        Add_MethodGroup_MultiDictionary_2_TKey = MultiDictionary_2.Add_MethodGroup_MultiDictionary_2_TKey
        Add_MethodGroup_MultiDictionary_2_TValue = MultiDictionary_2.Add_MethodGroup_MultiDictionary_2_TValue
        @typing.overload
        def __call__(self, key: Add_MethodGroup_MultiDictionary_2_TKey, values: IEnumerable_1[Add_MethodGroup_MultiDictionary_2_TValue]) -> None:...
        @typing.overload
        def __call__(self, key: Add_MethodGroup_MultiDictionary_2_TKey, value: Add_MethodGroup_MultiDictionary_2_TValue) -> None:...

    # Skipped Remove due to it being static, abstract and generic.

    Remove : Remove_MethodGroup[MultiDictionary_2_TKey, MultiDictionary_2_TValue]
    Remove_MethodGroup_MultiDictionary_2_TKey = typing.TypeVar('Remove_MethodGroup_MultiDictionary_2_TKey')
    Remove_MethodGroup_MultiDictionary_2_TValue = typing.TypeVar('Remove_MethodGroup_MultiDictionary_2_TValue')
    class Remove_MethodGroup(typing.Generic[Remove_MethodGroup_MultiDictionary_2_TKey, Remove_MethodGroup_MultiDictionary_2_TValue]):
        Remove_MethodGroup_MultiDictionary_2_TKey = MultiDictionary_2.Remove_MethodGroup_MultiDictionary_2_TKey
        Remove_MethodGroup_MultiDictionary_2_TValue = MultiDictionary_2.Remove_MethodGroup_MultiDictionary_2_TValue
        @typing.overload
        def __call__(self, key: Remove_MethodGroup_MultiDictionary_2_TKey) -> bool:...
        @typing.overload
        def __call__(self, key: Remove_MethodGroup_MultiDictionary_2_TKey, value: Remove_MethodGroup_MultiDictionary_2_TValue) -> bool:...



class MultiDictionaryOptimized_GenericClasses(abc.ABCMeta):
    Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TKey = typing.TypeVar('Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TKey')
    Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TValue = typing.TypeVar('Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TKey], typing.Type[Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TValue]]) -> typing.Type[MultiDictionaryOptimized_2[Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TKey, Generic_MultiDictionaryOptimized_GenericClasses_MultiDictionaryOptimized_2_TValue]]: ...

MultiDictionaryOptimized : MultiDictionaryOptimized_GenericClasses

MultiDictionaryOptimized_2_TKey = typing.TypeVar('MultiDictionaryOptimized_2_TKey')
MultiDictionaryOptimized_2_TValue = typing.TypeVar('MultiDictionaryOptimized_2_TValue')
class MultiDictionaryOptimized_2(typing.Generic[MultiDictionaryOptimized_2_TKey, MultiDictionaryOptimized_2_TValue]):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, original: MultiDictionaryOptimized_2[MultiDictionaryOptimized_2_TKey, MultiDictionaryOptimized_2_TValue]) -> None: ...
    @property
    def Item(self) -> IReadOnlyCollection_1[MultiDictionaryOptimized_2_TValue]: ...
    def Add(self, key: MultiDictionaryOptimized_2_TKey, value: MultiDictionaryOptimized_2_TValue) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: MultiDictionaryOptimized_2_TKey) -> bool: ...
    def TryGetValues(self, key: MultiDictionaryOptimized_2_TKey, values: clr.Reference[IEnumerable_1[MultiDictionaryOptimized_2_TValue]]) -> bool: ...
    # Skipped Remove due to it being static, abstract and generic.

    Remove : Remove_MethodGroup[MultiDictionaryOptimized_2_TKey, MultiDictionaryOptimized_2_TValue]
    Remove_MethodGroup_MultiDictionaryOptimized_2_TKey = typing.TypeVar('Remove_MethodGroup_MultiDictionaryOptimized_2_TKey')
    Remove_MethodGroup_MultiDictionaryOptimized_2_TValue = typing.TypeVar('Remove_MethodGroup_MultiDictionaryOptimized_2_TValue')
    class Remove_MethodGroup(typing.Generic[Remove_MethodGroup_MultiDictionaryOptimized_2_TKey, Remove_MethodGroup_MultiDictionaryOptimized_2_TValue]):
        Remove_MethodGroup_MultiDictionaryOptimized_2_TKey = MultiDictionaryOptimized_2.Remove_MethodGroup_MultiDictionaryOptimized_2_TKey
        Remove_MethodGroup_MultiDictionaryOptimized_2_TValue = MultiDictionaryOptimized_2.Remove_MethodGroup_MultiDictionaryOptimized_2_TValue
        @typing.overload
        def __call__(self, key: Remove_MethodGroup_MultiDictionaryOptimized_2_TKey) -> bool:...
        @typing.overload
        def __call__(self, key: Remove_MethodGroup_MultiDictionaryOptimized_2_TKey, value: Remove_MethodGroup_MultiDictionaryOptimized_2_TValue) -> bool:...



class ObservableDictionary_GenericClasses(abc.ABCMeta):
    Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TKey = typing.TypeVar('Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TKey')
    Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TValue = typing.TypeVar('Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TValue')
    def __getitem__(self, types : typing.Tuple[typing.Type[Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TKey], typing.Type[Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TValue]]) -> typing.Type[ObservableDictionary_2[Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TKey, Generic_ObservableDictionary_GenericClasses_ObservableDictionary_2_TValue]]: ...

ObservableDictionary : ObservableDictionary_GenericClasses

ObservableDictionary_2_TKey = typing.TypeVar('ObservableDictionary_2_TKey')
ObservableDictionary_2_TValue = typing.TypeVar('ObservableDictionary_2_TValue')
class ObservableDictionary_2(typing.Generic[ObservableDictionary_2_TKey, ObservableDictionary_2_TValue], IReadonlyObservableDictionary_2[ObservableDictionary_2_TKey, ObservableDictionary_2_TValue], IDictionary_2[ObservableDictionary_2_TKey, ObservableDictionary_2_TValue], INotifyPropertyChanged):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, dictionary: IDictionary_2[ObservableDictionary_2_TKey, ObservableDictionary_2_TValue]) -> None: ...
    @typing.overload
    def __init__(self, input: IEnumerable_1[KeyValuePair_2[ObservableDictionary_2_TKey, ObservableDictionary_2_TValue]]) -> None: ...
    @typing.overload
    def __init__(self, keys: IEnumerable_1[ObservableDictionary_2_TKey], values: IEnumerable_1[ObservableDictionary_2_TValue]) -> None: ...
    @property
    def Count(self) -> int: ...
    @property
    def Item(self) -> ObservableDictionary_2_TValue: ...
    @Item.setter
    def Item(self, value: ObservableDictionary_2_TValue) -> ObservableDictionary_2_TValue: ...
    @property
    def Keys(self) -> ICollection_1[ObservableDictionary_2_TKey]: ...
    @property
    def Values(self) -> ICollection_1[ObservableDictionary_2_TValue]: ...
    def Add(self, key: ObservableDictionary_2_TKey, value: ObservableDictionary_2_TValue) -> None: ...
    def Clear(self) -> None: ...
    def ContainsKey(self, key: ObservableDictionary_2_TKey) -> bool: ...
    def ContainsValue(self, value: ObservableDictionary_2_TValue) -> bool: ...
    def Remove(self, key: ObservableDictionary_2_TKey) -> bool: ...
    def TryGetValue(self, key: ObservableDictionary_2_TKey, value: clr.Reference[ObservableDictionary_2_TValue]) -> bool: ...
    # Skipped AddRange due to it being static, abstract and generic.

    AddRange : AddRange_MethodGroup[ObservableDictionary_2_TKey, ObservableDictionary_2_TValue]
    AddRange_MethodGroup_ObservableDictionary_2_TKey = typing.TypeVar('AddRange_MethodGroup_ObservableDictionary_2_TKey')
    AddRange_MethodGroup_ObservableDictionary_2_TValue = typing.TypeVar('AddRange_MethodGroup_ObservableDictionary_2_TValue')
    class AddRange_MethodGroup(typing.Generic[AddRange_MethodGroup_ObservableDictionary_2_TKey, AddRange_MethodGroup_ObservableDictionary_2_TValue]):
        AddRange_MethodGroup_ObservableDictionary_2_TKey = ObservableDictionary_2.AddRange_MethodGroup_ObservableDictionary_2_TKey
        AddRange_MethodGroup_ObservableDictionary_2_TValue = ObservableDictionary_2.AddRange_MethodGroup_ObservableDictionary_2_TValue
        @typing.overload
        def __call__(self, range: IEnumerable_1[KeyValuePair_2[AddRange_MethodGroup_ObservableDictionary_2_TKey, AddRange_MethodGroup_ObservableDictionary_2_TValue]]) -> None:...
        @typing.overload
        def __call__(self, keys: IEnumerable_1[AddRange_MethodGroup_ObservableDictionary_2_TKey], values: IEnumerable_1[AddRange_MethodGroup_ObservableDictionary_2_TValue]) -> None:...



class PriorityQueue_GenericClasses(abc.ABCMeta):
    Generic_PriorityQueue_GenericClasses_PriorityQueue_1_T = typing.TypeVar('Generic_PriorityQueue_GenericClasses_PriorityQueue_1_T')
    def __getitem__(self, types : typing.Type[Generic_PriorityQueue_GenericClasses_PriorityQueue_1_T]) -> typing.Type[PriorityQueue_1[Generic_PriorityQueue_GenericClasses_PriorityQueue_1_T]]: ...

PriorityQueue : PriorityQueue_GenericClasses

PriorityQueue_1_T = typing.TypeVar('PriorityQueue_1_T')
class PriorityQueue_1(typing.Generic[PriorityQueue_1_T]):
    # Constructor .ctor(isdesc : Boolean, comparison : Comparison`1) was skipped since it collides with above method
    @typing.overload
    def __init__(self, capacity: int, comparison: Comparison_1[PriorityQueue_1_T]) -> None: ...
    @typing.overload
    def __init__(self, capacity: int, isdesc: bool, comparison: Comparison_1[PriorityQueue_1_T]) -> None: ...
    @typing.overload
    def __init__(self, collection: IEnumerable_1[PriorityQueue_1_T], comparison: Comparison_1[PriorityQueue_1_T]) -> None: ...
    @typing.overload
    def __init__(self, collection: IEnumerable_1[PriorityQueue_1_T], isdesc: bool, comparison: Comparison_1[PriorityQueue_1_T]) -> None: ...
    @typing.overload
    def __init__(self, comparison: Comparison_1[PriorityQueue_1_T]) -> None: ...
    IsDescending : bool
    @property
    def Count(self) -> int: ...
    def Clear(self) -> None: ...
    def Dequeue(self) -> PriorityQueue_1_T: ...
    def Enqueue(self, x: PriorityQueue_1_T) -> None: ...
    def Peek(self) -> PriorityQueue_1_T: ...

