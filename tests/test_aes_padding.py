from crocology.aes.padding import pkcs7_pad, pkcs7_unpad


def test_pkcs7_pad() -> None:

    data = b"hello"

    padded = pkcs7_pad(data)

    assert len(padded) % 16 == 0


def test_pkcs7_roundtrip() -> None:

    msg = b"some test message"

    padded = pkcs7_pad(msg)
    unpadded = pkcs7_unpad(padded)

    assert unpadded == msg
