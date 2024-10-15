# Password Manager

This is a basic password manager that allows you to securely store and retrieve passwords using symmetric encryption with the `cryptography` library. The passwords are encrypted and stored in a file, and a key is used to encrypt and decrypt the passwords.

## Features

- **Add Passwords**: Add new account names and passwords to be securely stored.
- **View Passwords**: View your stored passwords (decrypted).
- **Encryption**: Uses `Fernet` encryption to ensure that passwords are stored securely.

## Requirements

- Python 3.x
- `cryptography` library

To install the required library:

```bash
pip3 install cryptography