from __future__ import annotations

import abc
import functools
from typing import *

from datarepr import datarepr
from frozendict import frozendict
from makeprop import makeprop
from unhash import unhash

__all__ = ["ArgumentHolder", "FrozenArgumentHolder"]


class BaseArgumentHolder(abc.ABC):

    __slots__ = ("_args", "_kwargs")

    @abc.abstractmethod
    def __eq__(self, other: Any, /) -> bool: ...

    @abc.abstractmethod
    def __init__(self, *args: Any, **kwargs: Any): ...

    def __len__(self) -> int:
        "This magic method implements len(self)."
        return len(self.args) + len(self.kwargs)

    def __repr__(self) -> str:
        "This magic method implements repr(self)."
        return datarepr(type(self).__name__, *self.args, **self.kwargs)

    @property
    @abc.abstractmethod
    def args(self): ...

    def call(self, callable: Callable, /) -> Any:
        "This method calls a callable using the arguments in the current instance."
        return callable(*self.args, **self.kwargs)

    def copy(self):
        "This method makes a copy of the current instance."
        return self.call(type(self))

    @property
    @abc.abstractmethod
    def kwargs(self): ...

    def partial(self, callable: Callable, /) -> functools.partial:
        "This method creates a functools.partial object."
        return functools.partial(callable, *self.args, **self.kwargs)

    def partialmethod(self, callable: Callable, /) -> functools.partial:
        "This method creates a functools.partialmethod object."
        return functools.partialmethod(
            callable,
            *self.args,
            **self.kwargs,
        )

    def toArgumentHolder(self) -> ArgumentHolder:
        "This method converts the current instance into a ArgumentHolder object."
        return self.call(ArgumentHolder)

    def toFrozenArgumentHolder(self) -> FrozenArgumentHolder:
        "This method converts the current instance into a FrozenArgumentHolder object."
        return self.call(FrozenArgumentHolder)


class ArgumentHolder(BaseArgumentHolder):

    def __eq__(self, other: Any, /) -> bool:
        "This magic method implements self==other."
        if not isinstance(other, ArgumentHolder):
            return False
        return (self.args, self.kwargs) == (other.args, other.kwargs)

    __hash__ = unhash

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        "This magic method sets up the current instance."
        self._args = list(args)
        self._kwargs = dict(kwargs)

    @makeprop(delete=())
    def args(self, value: Iterable) -> None:
        "This property holds the positional arguments."
        value = list(value)
        self._args.clear()
        self._args.extend(value)
        return self._args

    @makeprop(delete=())
    def kwargs(self, value: Any) -> None:
        "This property holds the keyword arguments."
        value = dict(value)
        self._kwargs.clear()
        self._kwargs.update(value)
        return self._kwargs


class FrozenArgumentHolder(BaseArgumentHolder):

    def __eq__(self, other: Any, /) -> bool:
        "This magic method implements self==other."
        if not isinstance(other, FrozenArgumentHolder):
            return False
        return (self.args, self.kwargs) == (other.args, other.kwargs)

    def __hash__(self) -> int:
        "This magic method implements hash(self)."
        return (self.args, self.kwargs).__hash__()

    def __init__(self, *args: Any, **kwargs: Any) -> None:
        "This magic method sets up the current instance."
        self._args = tuple(args)
        self._kwargs = frozendict(kwargs)

    @property
    def args(self) -> tuple:
        "This property holds the positional arguments."
        return self._args

    @property
    def kwargs(self) -> frozendict:
        "This property holds the keyword arguments."
        return self._kwargs
