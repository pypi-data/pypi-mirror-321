from Crypto.Cipher import AES, ChaCha20_Poly1305, Salsa20
from Crypto.Util.Padding import pad, unpad
from Crypto.PublicKey import RSA, ECC
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Signature import pss, DSS
from Crypto.Hash import SHA256, SHA512, HMAC
from Crypto.Protocol.KDF import PBKDF2, scrypt
from base64 import b64encode, b64decode
import hashlib
import os
import json
from typing import Union, Dict, Tuple, Optional
from dataclasses import dataclass
from jwt import encode as jwt_encode, decode as jwt_decode, ExpiredSignatureError
from bcrypt import hashpw, gensalt, checkpw

class CryptoException(Exception):
    """Base exception class for cryptography operations."""
    pass

@dataclass
class EncryptedData:
    """Container for encrypted data and metadata."""
    algorithm: str
    ciphertext: bytes
    iv: Optional[bytes] = None
    tag: Optional[bytes] = None
    nonce: Optional[bytes] = None

    def to_dict(self) -> Dict:
        """Convert to dictionary format for serialization."""
        return {
            'algorithm': self.algorithm,
            'ciphertext': b64encode(self.ciphertext).decode('utf-8'),
            'iv': b64encode(self.iv).decode('utf-8') if self.iv else None,
            'tag': b64encode(self.tag).decode('utf-8') if self.tag else None,
            'nonce': b64encode(self.nonce).decode('utf-8') if self.nonce else None
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'EncryptedData':
        """Create instance from dictionary."""
        return cls(
            algorithm=data['algorithm'],
            ciphertext=b64decode(data['ciphertext']),
            iv=b64decode(data['iv']) if data.get('iv') else None,
            tag=b64decode(data['tag']) if data.get('tag') else None,
            nonce=b64decode(data['nonce']) if data.get('nonce') else None
        )

class CryptoManager:
    """Main class for cryptographic operations."""
    
    def __init__(self, default_key_size: int = 32):
        """Initialize with default key size in bytes."""
        self.default_key_size = default_key_size

    def generate_key(self, size: Optional[int] = None) -> bytes:
        """Generate a secure random key."""
        return os.urandom(size or self.default_key_size)

    def derive_key(self, password: str, salt: bytes = None, iterations: int = 100000) -> Tuple[bytes, bytes]:
        """Derive a key from a password using PBKDF2."""
        if salt is None:
            salt = os.urandom(16)
        key = PBKDF2(password.encode(), salt, dkLen=32, count=iterations)
        return key, salt

    def encrypt_aes(self, data: Union[str, bytes], key: bytes, mode: str = 'GCM') -> EncryptedData:
        """Encrypt data using AES with specified mode."""
        if isinstance(data, str):
            data = data.encode()

        if mode == 'GCM':
            cipher = AES.new(key, AES.MODE_GCM)
            ciphertext, tag = cipher.encrypt_and_digest(data)
            return EncryptedData('AES-GCM', ciphertext, nonce=cipher.nonce, tag=tag)
        elif mode == 'CBC':
            cipher = AES.new(key, AES.MODE_CBC)
            ciphertext = cipher.encrypt(pad(data, AES.block_size))
            return EncryptedData('AES-CBC', ciphertext, iv=cipher.iv)
        else:
            raise CryptoException(f"Unsupported AES mode: {mode}")

    def decrypt_aes(self, encrypted_data: EncryptedData, key: bytes) -> bytes:
        """Decrypt AES-encrypted data."""
        if encrypted_data.algorithm == 'AES-GCM':
            cipher = AES.new(key, AES.MODE_GCM, nonce=encrypted_data.nonce)
            return cipher.decrypt_and_verify(encrypted_data.ciphertext, encrypted_data.tag)
        elif encrypted_data.algorithm == 'AES-CBC':
            cipher = AES.new(key, AES.MODE_CBC, iv=encrypted_data.iv)
            return unpad(cipher.decrypt(encrypted_data.ciphertext), AES.block_size)
        else:
            raise CryptoException(f"Unsupported algorithm: {encrypted_data.algorithm}")

    def encrypt_chacha20(self, data: Union[str, bytes], key: bytes) -> EncryptedData:
        """Encrypt data using ChaCha20-Poly1305."""
        if isinstance(data, str):
            data = data.encode()
        
        cipher = ChaCha20_Poly1305.new(key=key)
        ciphertext, tag = cipher.encrypt_and_digest(data)
        return EncryptedData('CHACHA20', ciphertext, nonce=cipher.nonce, tag=tag)

    def decrypt_chacha20(self, encrypted_data: EncryptedData, key: bytes) -> bytes:
        """Decrypt ChaCha20-Poly1305 encrypted data."""
        cipher = ChaCha20_Poly1305.new(key=key, nonce=encrypted_data.nonce)
        return cipher.decrypt_and_verify(encrypted_data.ciphertext, encrypted_data.tag)

    def generate_rsa_keypair(self, key_size: int = 2048) -> Tuple[RSA.RsaKey, RSA.RsaKey]:
        """Generate RSA key pair."""
        key = RSA.generate(key_size)
        return key, key.publickey()

    def encrypt_rsa(self, data: Union[str, bytes], public_key: RSA.RsaKey) -> bytes:
        """Encrypt data using RSA."""
        if isinstance(data, str):
            data = data.encode()
        cipher = PKCS1_OAEP.new(public_key)
        return cipher.encrypt(data)

    def decrypt_rsa(self, encrypted_data: bytes, private_key: RSA.RsaKey) -> bytes:
        """Decrypt RSA-encrypted data."""
        cipher = PKCS1_OAEP.new(private_key)
        return cipher.decrypt(encrypted_data)

    def generate_ecc_keypair(self, curve: str = 'P-256') -> Tuple[ECC.EccKey, ECC.EccKey]:
        """Generate ECC key pair."""
        key = ECC.generate(curve=curve)
        return key, key.public_key()

    def sign_data(self, data: Union[str, bytes], private_key: Union[RSA.RsaKey, ECC.EccKey]) -> bytes:
        """Sign data using RSA or ECC private key."""
        if isinstance(data, str):
            data = data.encode()
        
        h = SHA256.new(data)
        if isinstance(private_key, RSA.RsaKey):
            signer = pss.new(private_key)
        else:  # ECC
            signer = DSS.new(private_key, 'fips-186-3')
        return signer.sign(h)

    def verify_signature(self, data: Union[str, bytes], signature: bytes, 
                        public_key: Union[RSA.RsaKey, ECC.EccKey]) -> bool:
        """Verify signature using RSA or ECC public key."""
        if isinstance(data, str):
            data = data.encode()
            
        h = SHA256.new(data)
        try:
            if isinstance(public_key, RSA.RsaKey):
                verifier = pss.new(public_key)
                verifier.verify(h, signature)
            else:  # ECC
                verifier = DSS.new(public_key, 'fips-186-3')
                verifier.verify(h, signature)
            return True
        except (ValueError, TypeError):
            return False

    def create_hmac(self, data: Union[str, bytes], key: bytes, hash_algo: str = 'SHA256') -> bytes:
        """Create HMAC for data authentication."""
        if isinstance(data, str):
            data = data.encode()
            
        if hash_algo == 'SHA256':
            h = HMAC.new(key, digestmod=SHA256)
        elif hash_algo == 'SHA512':
            h = HMAC.new(key, digestmod=SHA512)
        else:
            raise CryptoException(f"Unsupported hash algorithm: {hash_algo}")
            
        h.update(data)
        return h.digest()

    def verify_hmac(self, data: Union[str, bytes], hmac: bytes, key: bytes, 
                    hash_algo: str = 'SHA256') -> bool:
        """Verify HMAC."""
        calculated_hmac = self.create_hmac(data, key, hash_algo)
        return hmac == calculated_hmac

    def encrypt_file(self, file_path: str, key: bytes, algorithm: str = 'AES-GCM') -> str:
        """Encrypt a file and save the encrypted version."""
        with open(file_path, 'rb') as f:
            data = f.read()
            
        if algorithm.startswith('AES'):
            encrypted_data = self.encrypt_aes(data, key, mode=algorithm.split('-')[1])
        elif algorithm == 'CHACHA20':
            encrypted_data = self.encrypt_chacha20(data, key)
        else:
            raise CryptoException(f"Unsupported algorithm: {algorithm}")

        output_path = f"{file_path}.encrypted"
        with open(output_path, 'w') as f:
            json.dump(encrypted_data.to_dict(), f)
            
        return output_path

    def decrypt_file(self, encrypted_file_path: str, key: bytes) -> str:
        """Decrypt an encrypted file and save the decrypted version."""
        with open(encrypted_file_path, 'r') as f:
            encrypted_data = EncryptedData.from_dict(json.load(f))

        if encrypted_data.algorithm.startswith('AES'):
            decrypted_data = self.decrypt_aes(encrypted_data, key)
        elif encrypted_data.algorithm == 'CHACHA20':
            decrypted_data = self.decrypt_chacha20(encrypted_data, key)
        else:
            raise CryptoException(f"Unsupported algorithm: {encrypted_data.algorithm}")

        output_path = encrypted_file_path.replace('.encrypted', '.decrypted')
        with open(output_path, 'wb') as f:
            f.write(decrypted_data)
            
        return output_path

