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


class Error(Exception):
    pass


class ResultProto[T, E: Error](Protocol):
    def is_ok(self) -> bool: ...

    def is_err(self) -> bool: ...

    def unwrap(self) -> T: ...

    def map[V](self, fn: Callable[[T], V]) -> Result[V, E]: ...

    def map_err[R: Error](self, fn: Callable[[E], R]) -> Result[T, R]: ...

    def map_or[V](self, default: V, fn: Callable[[T], V]) -> V: ...

    def map_or_else[V](self, default: Callable[[], V], fn: Callable[[T], V]) -> V: ...


@final
@dataclass(eq=True, frozen=True)
class Ok[T, E: Error](ResultProto[T, E]):
    v: T

    def is_ok(self) -> bool:
        return True

    def is_err(self) -> bool:
        return False

    def unwrap(self) -> T:
        return self.v

    def map[V](self, fn: Callable[[T], V]) -> Result[V, E]:
        return Ok(fn(self.v))

    def map_err[R: Error](self, fn: Callable[[E], R]) -> Result[T, R]:
        return Ok(self.v)

    def map_or[V](self, default: V, fn: Callable[[T], V]) -> V:
        return fn(self.v)

    def map_or_else[V](self, default: Callable[[], V], fn: Callable[[T], V]) -> V:
        return fn(self.v)


@final
@dataclass(eq=True, frozen=True)
class Err[T, E: Error](ResultProto[T, E]):
    e: E

    def is_ok(self) -> bool:
        return False

    def is_err(self) -> bool:
        return True

    def unwrap(self) -> NoReturn:
        raise self.e

    def map[V](self, fn: Callable[[T], V]) -> Result[V, E]:
        return Err(self.e)

    def map_err[R: Error](self, fn: Callable[[E], R]) -> Result[T, R]:
        return Err(fn(self.e))

    def map_or[V](self, default: V, fn: Callable[[T], V]) -> V:
        return default

    def map_or_else[V](self, default: Callable[[], V], fn: Callable[[T], V]) -> V:
        return default()


type Result[T, E: Error] = Ok[T, E] | Err[T, E]
