import os

from crocology.aes import AES
from crocology.aes.modes import decrypt_cbc, encrypt_cbc


def test_cbc_roundtrip() -> None:

    key = os.urandom(32)
    iv = os.urandom(16)

    aes = AES(key)

    message = b"pytest AES CBC mode example message"

    cipher = encrypt_cbc(aes, message, iv)
    plain = decrypt_cbc(aes, cipher, iv)

    assert plain == message
