from cryptography.fernet import Fernet

with open("chave.key", "rb") as chave_arquivo:
    chave = chave_arquivo.read()

fernet = Fernet(chave)

nome_arquivo = "test_files/file1.txt"
with open(nome_arquivo, "rb") as arquivo_criptografado:
    conteudo_criptografado = arquivo_criptografado.read()
    conteudo_descriptografado = fernet.decrypt(conteudo_criptografado)

nome_arquivo_descriptografado = "test_files/file1_descriptografado.txt"  # Substitua pelo nome do arquivo desejado
with open(nome_arquivo_descriptografado, "wb") as arquivo_descriptografado:
    arquivo_descriptografado.write(conteudo_descriptografado)
