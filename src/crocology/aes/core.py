from __future__ import annotations

from .constants import INV_S_BOX, S_BOX
from .gf256 import gmul
from .types import State


def sub_bytes(state: State) -> None:
    """Apply AES S-box substitution to every byte."""
    for r in range(4):
        for c in range(4):
            state[r][c] = S_BOX[state[r][c]]


def inv_sub_bytes(state: State) -> None:
    """Apply inverse AES S-box substitution."""
    for r in range(4):
        for c in range(4):
            state[r][c] = INV_S_BOX[state[r][c]]


def shift_rows(state: State) -> None:
    """Cyclically shift AES state rows left."""
    state[1] = state[1][1:] + state[1][:1]
    state[2] = state[2][2:] + state[2][:2]
    state[3] = state[3][3:] + state[3][:3]


def inv_shift_rows(state: State) -> None:
    """Cyclically shift AES state rows right."""
    state[1] = state[1][-1:] + state[1][:-1]
    state[2] = state[2][-2:] + state[2][:-2]
    state[3] = state[3][-3:] + state[3][:-3]


def mix_columns(state: State) -> None:
    """Mix columns using GF(2^8) matrix multiplication."""

    for c in range(4):
        a0: int = state[0][c]
        a1: int = state[1][c]
        a2: int = state[2][c]
        a3: int = state[3][c]

        state[0][c] = gmul(a0, 2) ^ gmul(a1, 3) ^ a2 ^ a3
        state[1][c] = a0 ^ gmul(a1, 2) ^ gmul(a2, 3) ^ a3
        state[2][c] = a0 ^ a1 ^ gmul(a2, 2) ^ gmul(a3, 3)
        state[3][c] = gmul(a0, 3) ^ a1 ^ a2 ^ gmul(a3, 2)


def inv_mix_columns(state: State) -> None:
    """Inverse MixColumns transformation."""

    for c in range(4):
        a0: int = state[0][c]
        a1: int = state[1][c]
        a2: int = state[2][c]
        a3: int = state[3][c]

        state[0][c] = gmul(a0, 14) ^ gmul(a1, 11) ^ gmul(a2, 13) ^ gmul(a3, 9)
        state[1][c] = gmul(a0, 9) ^ gmul(a1, 14) ^ gmul(a2, 11) ^ gmul(a3, 13)
        state[2][c] = gmul(a0, 13) ^ gmul(a1, 9) ^ gmul(a2, 14) ^ gmul(a3, 11)
        state[3][c] = gmul(a0, 11) ^ gmul(a1, 13) ^ gmul(a2, 9) ^ gmul(a3, 14)


def add_round_key(state: State, round_key: State) -> None:
    """XOR the state with the round key."""
    for r in range(4):
        for c in range(4):
            state[r][c] ^= round_key[r][c]
