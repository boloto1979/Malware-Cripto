import os
from cryptography.fernet import Fernet

key = Fernet.generate_key()

with open("chave.key", "wb") as chave:
    chave.write(key)

test_directory = "test_files"

files = [file for file in os.listdir(test_directory) if file not in ["test.py", "chave.key"]]

for file in files:
    with open(os.path.join(test_directory, file), "rb") as input_file:
        content = input_file.read()
    encrypted_content = Fernet(key).encrypt(content)
    with open(os.path.join(test_directory, file), "wb") as output_file:
        output_file.write(encrypted_content)
