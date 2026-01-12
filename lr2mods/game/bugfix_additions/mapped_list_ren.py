from __future__ import annotations
import builtins
from collections.abc import Iterator

"""renpy
IF FLAG_OPT_IN_ANNOTATIONS:
    rpy python annotations
init -50 python:
"""
from typing import Callable, Generic, Protocol, TypeVar
import zlib

##################################################################
# MappedList - replace object property with function mapped item #
# Used to prevent circular object references                     #
##################################################################
def generate_identifier(value) -> int:
    if isinstance(value, (list, tuple, set)):
        hash_string = "".join(map(str, value))
    else:
        hash_string = str(value)
    return zlib.adler32(hash_string.encode("utf-8"))

class MappedTypeInfo(Protocol):
    @property
    def identifier(self) -> int:
        pass

T = TypeVar("T", bound = "MappedTypeInfo")

class MappedList(list[Generic[T]]):
    def __init__(self, list_type: type[T], list_func: Callable[[], list[T]], new_list = None):
        self.list_type = list_type
        self.list_func = list_func
        self.mapped_list: list[T] = []
        if new_list:
            if type(new_list) is type(list_type):
                self.mapped_list[:] = new_list
            elif isinstance(new_list, MappedList):
                self.mapped_list[:] = new_list.mapped_list[:]
            else:
                self.mapped_list = list(new_list)

    def __eq__(self, other):
        return self.mapped_list == self.__cast(other)

    def __cast(self, other):
        return other.mapped_list if isinstance(other, MappedList) else other

    def __getitem__(self, key) -> T:
        if isinstance(key, slice):
            #Get the start, stop, and step from the slice
            return [self[ii] for ii in range(*key.indices(builtins.len(self)))]
        if isinstance(key, int):
            if key < 0: #Handle negative indices
                key += builtins.len(self)
            if key < 0 or key >= builtins.len(self):
                raise IndexError
            return next((x for x in self.list_func() if x.identifier == self.mapped_list[key]), None)
        raise TypeError

    def __setitem__(self, key: int, item: T):
        if not isinstance(key, int):
            raise TypeError
        if isinstance(item, self.list_type):
            self.mapped_list[key] = item.identifier

    def __delitem__(self, key: int):
        if not isinstance(key, int):
            raise TypeError
        del self.mapped_list[key]

    def __repr__(self) -> str:
        return repr(self())

    def __call__(self) -> list[T]:
        return [x for x in self.list_func() if x.identifier in self.mapped_list]

    def __iter__(self) -> Iterator[T]:
        return iter(x for x in self.list_func() if x.identifier in self.mapped_list)

    def __len__(self) -> int:
        return builtins.len(self.mapped_list)

    def __contains__(self, item: T) -> bool:
        if isinstance(item, self.list_type):
            return any(x for x in self.mapped_list if x == item.identifier)
        return False

    def __add__(self, other: list[T] | set[T] | tuple[T, ...] | MappedList[T]) -> MappedList[T]:
        if isinstance(other, MappedList):
            return MappedList(self.list_type, self.list_func, self.mapped_list.copy() + other.mapped_list.copy())
        if isinstance(other, (list, tuple, set)):
            new_list = self.mapped_list.copy()
            new_list.extend(x.identifier for x in other if isinstance(x, self.list_type))
            return MappedList(self.list_type, self.list_func, new_list)
        return self

    def __sub__(self, other: list[T] | set[T] | tuple[T, ...] | MappedList[T]) -> MappedList[T]:
        if isinstance(other, MappedList):
            return MappedList(self.list_type, self.list_func, list(set(self.mapped_list.copy()) - set(other.mapped_list.copy())))
        if isinstance(other, (list, tuple, set)):
            new_list = self.mapped_list.copy()
            for item in other:
                if isinstance(item, self.list_type) and item.identifier in new_list:
                    new_list.remove(item.identifier)
            return MappedList(self.list_type, self.list_func, new_list)
        return self

    def __iadd__(self, other: T):
        self.append(other)
        return self

    def __isub__(self, other: T):
        self.remove(other)
        return self

    def append(self, item: T):
        if isinstance(item, self.list_type) and item.identifier not in self.mapped_list:
            self.mapped_list.append(item.identifier)

    def remove(self, item: T):
        if isinstance(item, self.list_type) and item.identifier in self.mapped_list:
            self.mapped_list.remove(item.identifier)

    def clear(self):
        self.mapped_list.clear()

    def extend(self, other: list[T] | set[T] | tuple[T, ...] | MappedList[T]) -> MappedList[T]:
        if isinstance(other, MappedList):
            self.mapped_list.extend(other.mapped_list)
        if isinstance(other, (list, tuple, set)):
            self.mapped_list.extend(x.identifier for x in other)

    def pop(self, index = -1) -> T:
        identifier = self.mapped_list.pop(index)
        return next((x for x in self.list_func() if x.identifier == identifier), None)

    def index(self, item: T) -> int:
        if isinstance(item, self.list_type):
            return self.mapped_list.index(item.identifier)
        raise ValueError
