from __future__ import annotations

from typing import TypeAlias

Byte: TypeAlias = int
Block: TypeAlias = bytes
Word: TypeAlias = list[Byte]
State: TypeAlias = list[list[Byte]]
RoundKey: TypeAlias = list[list[Byte]]
