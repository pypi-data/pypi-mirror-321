# `rusty-whipsnake` - basic components of Rust's type system magic
# Copyright (C) 2025 Artur Ciesielski <artur.ciesielski@gmail.com>

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from __future__ import annotations

from collections.abc import Callable
from dataclasses import dataclass
from typing import NoReturn, Protocol, final


class NothingUnwrappedError(Exception):
    pass


class OptionProto[T](Protocol):
    def is_some(self) -> bool: ...

    def is_nothing(self) -> bool: ...

    def unwrap(self) -> T: ...

    def map[V](self, fn: Callable[[T], V]) -> Option[V]: ...

    def map_or[V](self, default: V, fn: Callable[[T], V]) -> V: ...

    def map_or_else[V](self, default: Callable[[], V], fn: Callable[[T], V]) -> V: ...


@final
@dataclass(eq=True, frozen=True)
class Some[T](OptionProto[T]):
    v: T

    def is_some(self) -> bool:
        return True

    def is_nothing(self) -> bool:
        return False

    def unwrap(self) -> T:
        return self.v

    def map[V](self, fn: Callable[[T], V]) -> Option[V]:
        return Some(fn(self.v))

    def map_or[V](self, default: V, fn: Callable[[T], V]) -> V:
        return fn(self.v)

    def map_or_else[V](self, default: Callable[[], V], fn: Callable[[T], V]) -> V:
        return fn(self.v)


@final
@dataclass(eq=True, frozen=True)
class Nothing[T](OptionProto[T]):
    def is_some(self) -> bool:
        return False

    def is_nothing(self) -> bool:
        return True

    def unwrap(self) -> NoReturn:
        raise NothingUnwrappedError()

    def map[V](self, fn: Callable[[T], V]) -> Option[V]:
        return Nothing()

    def map_or[V](self, default: V, fn: Callable[[T], V]) -> V:
        return default

    def map_or_else[V](self, default: Callable[[], V], fn: Callable[[T], V]) -> V:
        return default()


type Option[T] = Some[T] | Nothing[T]
