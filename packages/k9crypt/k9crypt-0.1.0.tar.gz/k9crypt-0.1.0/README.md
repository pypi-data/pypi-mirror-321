# K9Crypt

K9Crypt is a powerful Python library that provides multi-layer encryption. It securely protects your data using five different AES-256-based encryption modes.

## Features

- 5-layer AES-256 encryption (GCM, CBC, CFB, OFB, CTR)
- Strong key derivation with PBKDF2
- HMAC-SHA512 verification at each layer
- Brotli compression support
- Asynchronous (async/await) API
- Protection against timing attacks

## Installation

```bash
pip install k9crypt
```

## Usage Example

```python
from k9crypt import K9Crypt
import asyncio

async def test():
    secret_key = "VeryLongSecretKey!@#1234567890"
    encryptor = K9Crypt(secret_key)
    plaintext = "Hello, World!"

    try:
        encrypted = await encryptor.encrypt(plaintext)
        print("Encrypted data:", encrypted)

        decrypted = await encryptor.decrypt(encrypted)
        print("Decrypted data:", decrypted)
    except Exception as error:
        print("Encryption error:", str(error))

asyncio.run(test())
```

## Security Features

1. **Multi-Layer Encryption**: Each layer uses a different AES-256 mode
2. **HMAC Verification**: Integrity check at each layer
3. **Strong Key Derivation**: 600,000 iterations with PBKDF2
4. **Secure Comparison**: Protection against timing attacks
5. **Salt and Pepper**: Unique salt used for each encryption

## Requirements

- Python 3.7+
- cryptography>=41.0.7
- brotli>=1.1.0

## License

MIT License

## Contribution

1. Fork this repository
2. Create a new branch (`git checkout -b feature/new-feature`)
3. Commit your changes (`git commit -am 'Added new feature'`)
4. Push your branch (`git push origin feature/new-feature`)
5. Create a Pull Request
