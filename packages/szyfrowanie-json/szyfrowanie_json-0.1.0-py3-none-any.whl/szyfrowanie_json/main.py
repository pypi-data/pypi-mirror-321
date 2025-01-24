import os
import json
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.hazmat.primitives import padding
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

def gen_klucza(password, salt):
    """Generuje klucz na podstawie hasła i soli."""
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,  # Klucz AES (256 bitów)
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    return kdf.derive(password.encode())

def szyfrowanie(output_file, data, password):
    """Szyfruje zawartość pliku JSON i zapisuje pod nową nazwą."""
    salt = os.urandom(16)
    iv = os.urandom(16)
    key = gen_klucza(password, salt)

    json_data = json.dumps(data).encode('utf-8')

    padder = padding.PKCS7(128).padder()
    padded_data = padder.update(json_data) + padder.finalize()

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    encryptor = cipher.encryptor()
    encrypted_data = encryptor.update(padded_data) + encryptor.finalize()

    with open(output_file, 'wb') as f:
        f.write(salt + iv + encrypted_data)
        f.flush()

def odszyfrowanie(input_file, password):
    """Odszyfrowuje zawartość zaszyfrowanego pliku"""
    with open(input_file, 'rb') as f:
        encrypted_data = f.read()

    salt = encrypted_data[:16]
    iv = encrypted_data[16:32]
    encrypted_data = encrypted_data[32:]

    key = gen_klucza(password, salt)

    cipher = Cipher(algorithms.AES(key), modes.CBC(iv), backend=default_backend())
    decryptor = cipher.decryptor()
    decrypted_data = decryptor.update(encrypted_data) + decryptor.finalize()

    unpadder = padding.PKCS7(128).unpadder()
    unpadded_data = unpadder.update(decrypted_data) + unpadder.finalize()
    data = json.loads(unpadded_data.decode('utf-8'))
    return data
