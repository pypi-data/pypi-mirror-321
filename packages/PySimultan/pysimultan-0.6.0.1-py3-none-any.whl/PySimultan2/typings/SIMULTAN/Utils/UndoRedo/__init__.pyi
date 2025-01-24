import typing, abc
from System.Collections.Generic import IList_1, List_1

class CollectionUndoItem_GenericClasses(abc.ABCMeta):
    Generic_CollectionUndoItem_GenericClasses_CollectionUndoItem_1_T = typing.TypeVar('Generic_CollectionUndoItem_GenericClasses_CollectionUndoItem_1_T')
    def __getitem__(self, types : typing.Type[Generic_CollectionUndoItem_GenericClasses_CollectionUndoItem_1_T]) -> typing.Type[CollectionUndoItem_1[Generic_CollectionUndoItem_GenericClasses_CollectionUndoItem_1_T]]: ...

class CollectionUndoItem(CollectionUndoItem_0, metaclass =CollectionUndoItem_GenericClasses): ...

class CollectionUndoItem_0(abc.ABC):
    # Skipped Add due to it being static, abstract and generic.

    Add : Add_MethodGroup
    class Add_MethodGroup:
        def __getitem__(self, t:typing.Type[Add_1_T1]) -> Add_1[Add_1_T1]: ...

        Add_1_T1 = typing.TypeVar('Add_1_T1')
        class Add_1(typing.Generic[Add_1_T1]):
            Add_1_T = CollectionUndoItem_0.Add_MethodGroup.Add_1_T1
            def __call__(self, list: IList_1[Add_1_T], item: Add_1_T) -> CollectionUndoItem_1[Add_1_T]:...


    # Skipped Clear due to it being static, abstract and generic.

    Clear : Clear_MethodGroup
    class Clear_MethodGroup:
        def __getitem__(self, t:typing.Type[Clear_1_T1]) -> Clear_1[Clear_1_T1]: ...

        Clear_1_T1 = typing.TypeVar('Clear_1_T1')
        class Clear_1(typing.Generic[Clear_1_T1]):
            Clear_1_T = CollectionUndoItem_0.Clear_MethodGroup.Clear_1_T1
            def __call__(self, list: IList_1[Clear_1_T]) -> CollectionUndoItem_1[Clear_1_T]:...


    # Skipped Insert due to it being static, abstract and generic.

    Insert : Insert_MethodGroup
    class Insert_MethodGroup:
        def __getitem__(self, t:typing.Type[Insert_1_T1]) -> Insert_1[Insert_1_T1]: ...

        Insert_1_T1 = typing.TypeVar('Insert_1_T1')
        class Insert_1(typing.Generic[Insert_1_T1]):
            Insert_1_T = CollectionUndoItem_0.Insert_MethodGroup.Insert_1_T1
            def __call__(self, list: IList_1[Insert_1_T], item: Insert_1_T, idx: int) -> CollectionUndoItem_1[Insert_1_T]:...


    # Skipped Remove due to it being static, abstract and generic.

    Remove : Remove_MethodGroup
    class Remove_MethodGroup:
        def __getitem__(self, t:typing.Type[Remove_1_T1]) -> Remove_1[Remove_1_T1]: ...

        Remove_1_T1 = typing.TypeVar('Remove_1_T1')
        class Remove_1(typing.Generic[Remove_1_T1]):
            Remove_1_T = CollectionUndoItem_0.Remove_MethodGroup.Remove_1_T1
            def __call__(self, list: IList_1[Remove_1_T], item: Remove_1_T) -> CollectionUndoItem_1[Remove_1_T]:...


    # Skipped RemoveAt due to it being static, abstract and generic.

    RemoveAt : RemoveAt_MethodGroup
    class RemoveAt_MethodGroup:
        def __getitem__(self, t:typing.Type[RemoveAt_1_T1]) -> RemoveAt_1[RemoveAt_1_T1]: ...

        RemoveAt_1_T1 = typing.TypeVar('RemoveAt_1_T1')
        class RemoveAt_1(typing.Generic[RemoveAt_1_T1]):
            RemoveAt_1_T = CollectionUndoItem_0.RemoveAt_MethodGroup.RemoveAt_1_T1
            def __call__(self, list: IList_1[RemoveAt_1_T], idx: int) -> CollectionUndoItem_1[RemoveAt_1_T]:...




CollectionUndoItem_1_T = typing.TypeVar('CollectionUndoItem_1_T')
class CollectionUndoItem_1(typing.Generic[CollectionUndoItem_1_T], IUndoItem):
    def __init__(self, list: IList_1[CollectionUndoItem_1_T], action: UndoRedoAction, oldStartIndex: int, oldItems: IList_1[CollectionUndoItem_1_T], newStartIndex: int, newItems: IList_1[CollectionUndoItem_1_T]) -> None: ...
    def Execute(self) -> UndoExecutionResult: ...
    def Redo(self) -> None: ...
    def Undo(self) -> None: ...


class GroupUndoItem(IUndoItem):
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, items: List_1[IUndoItem]) -> None: ...
    @property
    def Items(self) -> List_1[IUndoItem]: ...
    def Execute(self) -> UndoExecutionResult: ...
    def Redo(self) -> None: ...
    def Undo(self) -> None: ...


class IUndoItem(typing.Protocol):
    @abc.abstractmethod
    def Execute(self) -> UndoExecutionResult: ...
    @abc.abstractmethod
    def Redo(self) -> None: ...
    @abc.abstractmethod
    def Undo(self) -> None: ...


class PropertyUndoItem(IUndoItem):
    def __init__(self, target: typing.Any, property: str, value: typing.Any) -> None: ...
    def Execute(self) -> UndoExecutionResult: ...
    def Redo(self) -> None: ...
    def Undo(self) -> None: ...


class UndoExecutionResult(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Executed : UndoExecutionResult # 0
    PartiallyExecuted : UndoExecutionResult # 1
    Failed : UndoExecutionResult # 2


class UndoRedoAction(typing.SupportsInt):
    @typing.overload
    def __init__(self, value : int) -> None: ...
    @typing.overload
    def __init__(self, value : int, force_if_true: bool) -> None: ...
    def __int__(self) -> int: ...
    
    # Values:
    Insert : UndoRedoAction # 0
    Remove : UndoRedoAction # 1
    Clear : UndoRedoAction # 2

