
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
