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

def jogar_forca():
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
        letras_acertadas.append("_")
    
    acertou = False
    erros = 0          
    max_erros = 6     
    
    while not acertou and erros < max_erros:
        mostrar_letras_acertadas(letras_acertadas)
        chute = input("Digite uma letra: ")
        chute = chute.upper()
        
        acertou_letra = False
        indice = 0
        for letra in palavra:
            if chute == letra:
                letras_acertadas[indice] = letra
                acertou_letra = True
            indice = indice + 1
        
        if not acertou_letra:
            erros = erros + 1
            print("Letra errada!")
        
        if "_" not in letras_acertadas:
            acertou = True
    
    mostrar_letras_acertadas(letras_acertadas)
    if acertou:
        print("Parabéns, você acertou a palavra!")
    else:
        print("Você perdeu :(")
        print("A palavra era: ", palavra)

def jogar_adivinhacao():
    print("\n=== ESCOLHA O TEMA ===")
    print("1 - Guardiões da Galáxia")
    print("2 - League of Legends")
    print("3 - Sanrio")
    tema = int(input("Digite o número do tema: "))
    
    palavras = carregar_palavras(tema)
    if not palavras:
        return
    
    palavra = random.choice(palavras).upper()
    print("Tente adivinhar a palavra secreta!")
    
    tentativas = 1
    limite = 3
    while tentativas <= limite:
        chute = input(f"Tentativa {tentativas}/{limite} - Digite a palavra: ")
        chute = chute.upper()
        if chute == palavra:
            print("Parabéns, você acertou a palavra secreta!")
            return
        else:
            print("Errado!")
        tentativas = tentativas + 1
    
    print("Você perdeu :(")
    print("A palavra era: ", palavra)

print("Bem-vindo ao jogo!")
while True:
    print("\n=== MENU DE JOGOS ===")
    print("1 - Jogar Forca")
    print("2 - Jogar Adivinhação")
    print("3 - Sair")
    opcao = input("Escolha uma opção: ")
    
    if opcao == "1":
        jogar_forca()
    elif opcao == "2":
        jogar_adivinhacao()
    elif opcao == "3":
        print("Até logo! Obrigado por jogar :)")
        break
    else:
        print("Opção inválida, tente novamente.")