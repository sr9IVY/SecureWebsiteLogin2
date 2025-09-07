# Author Sidart Rav
# 09/06/2025
# SDev 245 Module 2: Assignment - Encrypt/Decrypt Demo

import rsa
from cryptography.fernet import Fernet

# --- User and Role Setup ---
users = {
    "john": {"password": "password123", "role": "admin"},
    "julie": {"password": "secure456", "role": "user"}
}

def authenticate(username, password):
    user = users.get(username)
    return user if user and user["password"] == password else None

def authorize(user):
    return f"Access granted to {user['role']} resources."

# --- Symmetric Encryption (AES via Fernet) ---
symmetric_key = Fernet.generate_key()
fernet = Fernet(symmetric_key)

message = "Confidential data"
sym_encrypted = fernet.encrypt(message.encode())
sym_decrypted = fernet.decrypt(sym_encrypted).decode()

# --- Asymmetric Encryption (RSA) ---
(pub_key, priv_key) = rsa.newkeys(512)
asym_encrypted = rsa.encrypt(message.encode(), pub_key)
asym_decrypted = rsa.decrypt(asym_encrypted, priv_key).decode()

# --- Output to File ---
with open("encryption_demo.txt", "w") as f:
    f.write("=== Symmetric Encryption ===\n")
    f.write(f"Key: {symmetric_key.decode()}\n")
    f.write(f"Input: {message}\n")
    f.write(f"Encrypted: {sym_encrypted.decode()}\n")
    f.write(f"Decrypted: {sym_decrypted}\n\n")

    f.write("=== Asymmetric Encryption ===\n")
    f.write(f"Public Key: {pub_key}\n")
    f.write(f"Private Key: {priv_key}\n")
    f.write(f"Input: {message}\n")
    f.write(f"Encrypted: {asym_encrypted}\n")
    f.write(f"Decrypted: {asym_decrypted}\n")

# --- Simulate Login ---
username = input("Username: ")
password = input("Password: ")
user = authenticate(username, password)

if user:
    print(authorize(user))
else:
    print("Authentication failed.")
