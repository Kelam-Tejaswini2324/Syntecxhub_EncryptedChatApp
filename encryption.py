from cryptography.fernet import Fernet
import os

KEY_FILE = "secret.key"

# Create key only once
if not os.path.exists(KEY_FILE):
    with open(KEY_FILE, "wb") as file:
        file.write(Fernet.generate_key())

# Load the same key every time
with open(KEY_FILE, "rb") as file:
    KEY = file.read()

cipher = Fernet(KEY)

def encrypt_message(message):
    return cipher.encrypt(message.encode())

def decrypt_message(encrypted_message):
    return cipher.decrypt(encrypted_message).decode()

# Test
if __name__ == "__main__":
    message = "Hello Syntecxhub"

    encrypted = encrypt_message(message)
    print("Original :", message)
    print("Encrypted:", encrypted)

    decrypted = decrypt_message(encrypted)
    print("Decrypted:", decrypted)