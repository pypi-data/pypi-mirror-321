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

import importlib.resources

from rusty_whipsnake.result import Err, Error, Ok, Result


class ReadError(Error):
    pass


class FileNotFound(ReadError):
    pass


class FileNotReadable(ReadError):
    pass


class FileEmpty(ReadError):
    pass


def read_first_line_from_file(file_name: str) -> Result[str, ReadError]:
    try:
        with open(file_name) as file:
            line = file.readline()
            if line == "":
                return Err(FileEmpty())
            return Ok(line.strip())
    except FileNotFoundError:
        return Err(FileNotFound())
    except PermissionError:
        return Err(FileNotReadable())


file_name = "/etc/passwd"
match read_first_line_from_file(file_name):
    case Ok(l):
        print(f"First line from '{file_name}': {l}")
    case Err(e):
        print(
            f"Could not read first line from '{file_name}', "
            f"error: {e.__class__.__name__}"
        )


file_name = "/file-that-most-certainly-does-not-exist.yaml"
match read_first_line_from_file(file_name):
    case Ok(l):
        print(f"First line from '{file_name}': {l}")
    case Err(e):
        print(
            f"Could not read first line from '{file_name}', "
            f"error: {e.__class__.__name__}"
        )


file_name = "/root/file.yaml"
match read_first_line_from_file(file_name):
    case Ok(l):
        print(f"First line from '{file_name}': {l}")
    case Err(e):
        print(
            f"Could not read first line from '{file_name}', "
            f"error: {e.__class__.__name__}"
        )


file_name = str(importlib.resources.files("rusty_whipsnake") / "py.typed")
match read_first_line_from_file(file_name):
    case Ok(l):
        print(f"First line from '{file_name}': {l}")
    case Err(e):
        print(
            f"Could not read first line from '{file_name}', "
            f"error: {e.__class__.__name__}"
        )
