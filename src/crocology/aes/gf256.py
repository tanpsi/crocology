from __future__ import annotations


def gmul(a: int, b: int) -> int:
    """Multiply in GF(2^8)."""
    p: int = 0

    for _ in range(8):
        if b & 1:
            p ^= a

        hi: int = a & 0x80
        a = (a << 1) & 0xFF

        if hi:
            a ^= 0x1B

        b >>= 1

    return p
