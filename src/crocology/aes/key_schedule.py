from __future__ import annotations

from .constants import RCON, S_BOX
from .types import State, Word


def sub_word(word: Word) -> Word:
    return [S_BOX[b] for b in word]


def rot_word(word: Word) -> Word:
    return word[1:] + word[:1]


def words_to_state(words: list[Word]) -> State:
    """Convert 4 AES words (columns) to a State matrix."""
    return [
        [words[0][0], words[1][0], words[2][0], words[3][0]],
        [words[0][1], words[1][1], words[2][1], words[3][1]],
        [words[0][2], words[1][2], words[2][2], words[3][2]],
        [words[0][3], words[1][3], words[2][3], words[3][3]],
    ]


def expand_key(key: bytes) -> list[State]:

    nk = len(key) // 4
    nr = {4: 10, 6: 12, 8: 14}[nk]

    w: list[Word] = [list(key[i : i + 4]) for i in range(0, len(key), 4)]

    for i in range(nk, 4 * (nr + 1)):
        temp = w[i - 1].copy()

        if i % nk == 0:
            temp = sub_word(rot_word(temp))
            temp[0] ^= RCON[(i // nk) - 1]

        elif nk > 6 and i % nk == 4:
            temp = sub_word(temp)

        w.append([a ^ b for a, b in zip(w[i - nk], temp, strict=True)])

    round_keys: list[State] = []

    for i in range(nr + 1):
        words = w[4 * i : 4 * (i + 1)]
        round_keys.append(words_to_state(words))

    return round_keys
