from __future__ import annotations

from .core import (
    add_round_key,
    inv_mix_columns,
    inv_shift_rows,
    inv_sub_bytes,
    mix_columns,
    shift_rows,
    sub_bytes,
)
from .key_schedule import expand_key
from .types import State
from .utils import bytes_to_state, state_to_bytes


class AES:
    def __init__(self, key: bytes) -> None:

        if len(key) not in (16, 24, 32):
            raise ValueError("AES key must be 16/24/32 bytes")

        self.round_keys: list[State] = expand_key(key)
        self.nr: int = len(self.round_keys) - 1

    def encrypt_block(self, block: bytes) -> bytes:

        state: State = bytes_to_state(block)

        add_round_key(state, self.round_keys[0])

        for i in range(1, self.nr):
            sub_bytes(state)
            shift_rows(state)
            mix_columns(state)
            add_round_key(state, self.round_keys[i])

        sub_bytes(state)
        shift_rows(state)
        add_round_key(state, self.round_keys[self.nr])

        return state_to_bytes(state)

    def decrypt_block(self, block: bytes) -> bytes:

        state = bytes_to_state(block)

        add_round_key(state, self.round_keys[self.nr])

        for i in range(self.nr - 1, 0, -1):
            inv_shift_rows(state)
            inv_sub_bytes(state)
            add_round_key(state, self.round_keys[i])
            inv_mix_columns(state)

        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, self.round_keys[0])

        return state_to_bytes(state)
