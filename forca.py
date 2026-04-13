import random

def carregar_palavras(tema):
    if tema == 1:
        arquivo = "guardioes_da_galaxia.txt"
    elif tema == 2:
        arquivo = "league_of_legends.txt"
    elif tema == 3:
        arquivo = "sanrio.txt"
    else:
        print("Tema inválido!")
        return []
    
    with open(arquivo, "r", encoding="utf-8") as f:
        palavras = [linha.strip() for linha in f if linha.strip()]
    return palavras

def mostrar_letras_acertadas(letras_acertadas):
    for letra in letras_acertadas:
        print(letra, end=" ")
    print("")

def jogar():
    print("\n=== ESCOLHA O TEMA ===")
    print("1 - Guardiões da Galáxia")
    print("2 - League of Legends")
    print("3 - Sanrio")
    tema = int(input("Digite o número do tema: "))
    
    palavras = carregar_palavras(tema)
    if not palavras:
        return
    
    palavra = random.choice(palavras).upper()
    letras_acertadas = []
    for letra in palavra:
        letras_acertadas.append("*")
    
    acertou = False
    enforcou = False
    erros = 0
    max_erros = 6
    
    while not acertou and not enforcou:
        mostrar_letras_acertadas(letras_acertadas)
        chute = input("Digite uma letra: ")
        
        acertou_letra = False
        indice = 0
        for letra in palavra:
            if chute.upper() == letra:
                letras_acertadas[indice] = letra
                acertou_letra = True
            indice = indice + 1
        
        if not acertou_letra:
            erros = erros + 1
            print("Letra errada!")
        
        if erros == max_erros:
            enforcou = True
        if letras_acertadas.count("*") == 0:
            acertou = True
    
    mostrar_letras_acertadas(letras_acertadas)
    if acertou:
        print("Parabéns, você acertou a palavra secreta! <3")
    else:
        print("Você perdeu :(")
        print("A palavra era: ", palavra)