import typing, abc

class IRandomizer(typing.Protocol):
    @abc.abstractmethod
    def Next(self) -> float: ...


class NormalDistributedRandomizer(IRandomizer):
    def __init__(self) -> None: ...
    def Next(self) -> float: ...

