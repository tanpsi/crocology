from __future__ import annotations

BLOCK_SIZE: int = 16


def pkcs7_pad(data: bytes) -> bytes:
    pad_len: int = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    return data + bytes([pad_len] * pad_len)


def pkcs7_unpad(data: bytes) -> bytes:
    if not data:
        raise ValueError("empty data")

    pad_len: int = data[-1]

    if pad_len < 1 or pad_len > BLOCK_SIZE:
        raise ValueError("invalid padding")

    return data[:-pad_len]
