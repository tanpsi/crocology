from __future__ import annotations

from .aes import AES
from .padding import pkcs7_pad, pkcs7_unpad
from .utils import split_blocks, xor_bytes


def encrypt_cbc(aes: AES, data: bytes, iv: bytes) -> bytes:

    data = pkcs7_pad(data)

    out: bytes = b""
    prev: bytes = iv

    for block in split_blocks(data):
        block = xor_bytes(block, prev)
        enc = aes.encrypt_block(block)

        out += enc
        prev = enc

    return out


def decrypt_cbc(aes: AES, data: bytes, iv: bytes) -> bytes:

    out: bytes = b""
    prev: bytes = iv

    for block in split_blocks(data):
        dec = aes.decrypt_block(block)
        out += xor_bytes(dec, prev)

        prev = block

    return pkcs7_unpad(out)
