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

from rusty_whipsnake.option import Nothing, Option, Some


def get_user_entry_from_etc_passwd(username: str) -> Option[str]:
    with open("/etc/passwd") as passwd_file:
        for line in passwd_file:
            parts: list[str] = line.split(":")
            if parts[0] == username:
                return Some(line.strip())
        return Nothing()


user = "root"
match get_user_entry_from_etc_passwd(user):
    case Some(l):
        print(f"User '{user}' found in the '/etc/passwd' file, corresponding line: {l}")
    case Nothing():
        print(f"User '{user}' not found in the '/etc/passwd' file")


user = "anchovies"
match get_user_entry_from_etc_passwd(user):
    case Some(l):
        print(f"User '{user}' found in the '/etc/passwd' file, corresponding line: {l}")
    case Nothing():
        print(f"User '{user}' not found in the '/etc/passwd' file")
