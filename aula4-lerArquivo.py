palavras = []
arquivo = open("palavras.txt", "r")
for linha in arquivo:
    palavras.append(linha.strip())