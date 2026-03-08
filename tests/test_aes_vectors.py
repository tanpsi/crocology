import pytest

from crocology.aes import AES


def test_aes128_encrypt_block() -> None:
    """
    NIST AES Known Answer Test
    """

    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f")

    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")

    expected_cipher = bytes.fromhex("69c4e0d86a7b0430d8cdb78070b4c55a")

    aes = AES(key)

    result = aes.encrypt_block(plaintext)

    assert result == expected_cipher


def test_aes192_encrypt_block() -> None:

    key = bytes.fromhex("000102030405060708090a0b0c0d0e0f1011121314151617")

    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")

    expected_cipher = bytes.fromhex("dda97ca4864cdfe06eaf70a0ec0d7191")

    aes = AES(key)

    result = aes.encrypt_block(plaintext)

    assert result == expected_cipher


def test_aes256_encrypt_block() -> None:

    key = bytes.fromhex(
        "000102030405060708090a0b0c0d0e0f101112131415161718191a1b1c1d1e1f"
    )

    plaintext = bytes.fromhex("00112233445566778899aabbccddeeff")

    expected_cipher = bytes.fromhex("8ea2b7ca516745bfeafc49904b496089")

    aes = AES(key)

    result = aes.encrypt_block(plaintext)

    assert result == expected_cipher


def test_invalid_key_length() -> None:

    with pytest.raises(ValueError):
        AES(b"bad")
