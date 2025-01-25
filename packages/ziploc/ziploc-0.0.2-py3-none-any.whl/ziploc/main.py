from typing import Dict, Union

from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

Config = Dict[str, Union[str, "Config"]]  # Recursive type annotation for nested dicts


def encrypt_string(text, password):
    iv = get_random_bytes(16)
    key = bytes.fromhex(password)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_text = text.encode("utf-8") + (16 - len(text) % 16) * b"\x00"
    encrypted = cipher.encrypt(padded_text)
    return f"{iv.hex()}:{encrypted.hex()}"


def decrypt_string(text, password):
    iv_hex, encrypted_hex = text.split(":")
    iv = bytes.fromhex(iv_hex)
    encrypted = bytes.fromhex(encrypted_hex)
    key = bytes.fromhex(password)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted = cipher.decrypt(encrypted)
    return decrypted.rstrip(b"\x00").decode("utf-8")


def encrypt(config: Union[str, Config], password: str) -> Union[str, Config]:
    """Encrypts a nested configuration dictionary or a single string."""
    if isinstance(config, str):
        return encrypt_string(config, password)

    if isinstance(config, dict):
        return {key: encrypt(value, password) for key, value in config.items()}

    raise TypeError("Config must be either a string or a dictionary")


def decrypt(config: Union[str, Config], password: str) -> Union[str, Config]:
    """Decrypts a nested configuration dictionary or a single string."""
    if isinstance(config, str):
        return decrypt_string(config, password)

    if isinstance(config, dict):
        return {key: decrypt(value, password) for key, value in config.items()}

    raise TypeError("Config must be either a string or a dictionary")
