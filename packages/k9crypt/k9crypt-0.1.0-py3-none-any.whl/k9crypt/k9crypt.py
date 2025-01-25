import os
import base64
import hmac as hmac_module
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.primitives import padding, hashes, hmac
from cryptography.hazmat.backends import default_backend
import brotli

HMAC_KEY = b"K9CryptHMAC2024!@#$%^&*()"

class K9Crypt:
    def __init__(self, key: str):
        hasher = hashes.Hash(hashes.SHA512(), backend=default_backend())
        hasher.update(key.encode())
        self.key = hasher.finalize()[:32]
    
    def _generate_iv(self) -> bytes:
        return os.urandom(16)
    
    def _pad(self, data: bytes) -> bytes:
        padder = padding.PKCS7(128).padder()
        return padder.update(data) + padder.finalize()
    
    def _unpad(self, data: bytes) -> bytes:
        unpadder = padding.PKCS7(128).unpadder()
        return unpadder.update(data) + unpadder.finalize()
    
    def _hash_data(self, data: bytes) -> bytes:
        h = hmac.HMAC(HMAC_KEY, hashes.SHA512(), backend=default_backend())
        h.update(data)
        digest = h.finalize()
        return digest
    
    def _verify_hash(self, data: bytes, expected_hash: bytes) -> bool:
        calculated_hash = self._hash_data(data)
        try:
            return hmac_module.compare_digest(calculated_hash, expected_hash)
        except Exception:
            return False
    
    def _encrypt_gcm(self, data: bytes) -> tuple[bytes, bytes]:
        iv = self._generate_iv()
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        ciphertext = encryptor.update(data) + encryptor.finalize()
        return ciphertext + encryptor.tag, iv
    
    def _decrypt_gcm(self, data: bytes, iv: bytes) -> bytes:
        tag = data[-16:]
        ciphertext = data[:-16]
        cipher = Cipher(algorithms.AES(self.key), modes.GCM(iv, tag), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(ciphertext) + decryptor.finalize()
    
    def _encrypt_cbc(self, data: bytes) -> tuple[bytes, bytes]:
        iv = self._generate_iv()
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        padded_data = self._pad(data)
        return encryptor.update(padded_data) + encryptor.finalize(), iv
    
    def _decrypt_cbc(self, data: bytes, iv: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.CBC(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        padded_data = decryptor.update(data) + decryptor.finalize()
        return self._unpad(padded_data)
    
    def _encrypt_cfb(self, data: bytes) -> tuple[bytes, bytes]:
        iv = self._generate_iv()
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize(), iv
    
    def _decrypt_cfb(self, data: bytes, iv: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.CFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()
    
    def _encrypt_ofb(self, data: bytes) -> tuple[bytes, bytes]:
        iv = self._generate_iv()
        cipher = Cipher(algorithms.AES(self.key), modes.OFB(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize(), iv
    
    def _decrypt_ofb(self, data: bytes, iv: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.OFB(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()
    
    def _encrypt_ctr(self, data: bytes) -> tuple[bytes, bytes]:
        iv = self._generate_iv()
        cipher = Cipher(algorithms.AES(self.key), modes.CTR(iv), backend=default_backend())
        encryptor = cipher.encryptor()
        return encryptor.update(data) + encryptor.finalize(), iv
    
    def _decrypt_ctr(self, data: bytes, iv: bytes) -> bytes:
        cipher = Cipher(algorithms.AES(self.key), modes.CTR(iv), backend=default_backend())
        decryptor = cipher.decryptor()
        return decryptor.update(data) + decryptor.finalize()
    
    async def _compress(self, data: bytes) -> bytes:
        try:
            return brotli.compress(data)
        except Exception as e:
            raise ValueError(f"Compression error: {str(e)}")
    
    async def _decompress(self, data: bytes) -> bytes:
        try:
            return brotli.decompress(data)
        except Exception as e:
            raise ValueError(f"Decompression error: {str(e)}")
    
    async def encrypt(self, plaintext: str) -> str:
        data = plaintext.encode()
        data = await self._compress(data)
        
        data, iv1 = self._encrypt_gcm(data)
        hash1 = self._hash_data(data)
        data = hash1 + data
        
        data, iv2 = self._encrypt_cbc(data)
        hash2 = self._hash_data(data)
        data = hash2 + data
        
        data, iv3 = self._encrypt_cfb(data)
        hash3 = self._hash_data(data)
        data = hash3 + data
        
        data, iv4 = self._encrypt_ofb(data)
        hash4 = self._hash_data(data)
        data = hash4 + data
        
        data, iv5 = self._encrypt_ctr(data)
        hash5 = self._hash_data(data)
        data = hash5 + data
        
        combined = iv1 + iv2 + iv3 + iv4 + iv5 + data
        
        return base64.b64encode(combined).decode()
    
    async def decrypt(self, ciphertext: str) -> str:
        data = base64.b64decode(ciphertext)
        
        iv1 = data[:16]
        iv2 = data[16:32]
        iv3 = data[32:48]
        iv4 = data[48:64]
        iv5 = data[64:80]
        data = data[80:]
        
        hash5 = data[:64]
        data = data[64:]
        if not self._verify_hash(data, hash5):
            raise ValueError("Layer 5 integrity check failed")
        data = self._decrypt_ctr(data, iv5)

        hash4 = data[:64]
        data = data[64:]
        if not self._verify_hash(data, hash4):
            raise ValueError("Layer 4 integrity check failed")
        data = self._decrypt_ofb(data, iv4)
        
        hash3 = data[:64]
        data = data[64:]
        if not self._verify_hash(data, hash3):
            raise ValueError("Layer 3 integrity check failed")
        data = self._decrypt_cfb(data, iv3)
        
        hash2 = data[:64]
        data = data[64:]
        if not self._verify_hash(data, hash2):
            raise ValueError("Layer 2 integrity check failed")
        data = self._decrypt_cbc(data, iv2)
        
        hash1 = data[:64]
        data = data[64:]
        if not self._verify_hash(data, hash1):
            raise ValueError("Layer 1 integrity check failed")
        data = self._decrypt_gcm(data, iv1)

        data = await self._decompress(data)
        return data.decode()