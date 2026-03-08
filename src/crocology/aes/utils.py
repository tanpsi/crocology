from __future__ import annotations

from collections.abc import Iterator

from .types import State


def xor_bytes(a: bytes, b: bytes) -> bytes:
    return bytes(x ^ y for x, y in zip(a, b, strict=True))


def bytes_to_state(block: bytes) -> State:
    if len(block) != 16:
        raise ValueError("AES block must be 16 bytes")

    state: State = [[0] * 4 for _ in range(4)]

    for i, byte in enumerate(block):
        row = i % 4
        col = i // 4
        state[row][col] = byte

    return state


def state_to_bytes(state: State) -> bytes:
    out = bytearray(16)

    for col in range(4):
        for row in range(4):
            out[col * 4 + row] = state[row][col]

    return bytes(out)


def split_blocks(data: bytes, size: int = 16) -> Iterator[bytes]:
    for i in range(0, len(data), size):
        yield data[i : i + size]
