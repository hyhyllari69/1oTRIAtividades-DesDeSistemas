import random
palavras = ["rocket raccoon", "yondu", "gamora", "mantis", "groot"]
palavra = random.choice(palavras)
palavra = palavra.upper()

letras_acertadas = []
for letra in palavra
    letras_acertadas.append("_")
acertou = False
enforcou = False
limite_tentativas = len(palavra) + 6
tentativa = 1

def mostrar_letras_acertadas():
    for letra in letras_acertadas:
        print(letra, end=" ")

print("Duvido você adivinhar a palavra secreta >:)")
while(not acertou and not enforcou):
    # mostar as letras acertadas
    mostrar_letras_acertadas()

    print("")
    chute = input("Digite uma letra: ")
    indice = 0
    for letra in palavra:
        if chute.upper() == letra:
            letras_acertadas[indice] = letra
        indice = indice + 1

    if tentativa == limite_tentativas:
        print("Você perdeu :( kkkkk\nA palavra era:", palavra)
        enforcou = True

    if letras_acertadas.count("_") == 0:
        print("Parabéns!!! Você acertou a palavra :))")
        mostrar_letras_acertadas()
        acertou = True

    tentativa = tentativa + 1