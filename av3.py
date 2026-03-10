# 1) Desenvolva a possibilidade do usuário escolher a dificuldade por meio de um menu de opções. Crie os níveis fácil, médio e difícil, configurando as variáveis conforme preferir. (1,5 pontos)

#Adicione no dicas no jogo, informando se o número sorteado é maior ou menor que o chute do usuário. (1,0 ponto)

#Valor total: 2,5 pontos
#Data de entrega: 12/03/2025


import random

while True:
    print("1 - Fácil")
    print("2 - Médio")
    print("3 - Difícil")
    print("4 - Sair")

    opcao = int(input("Escolha a dificuldade: "))

    if opcao == 1:
        sorteio_max = 10
        tentativas_max = 3
        print("Modo Fácil selecionado")

    elif opcao == 2:
        sorteio_max = 20
        tentativas_max = 3
        print("Modo Médio selecionado")

    elif opcao == 3:
        sorteio_max = 50
        tentativas_max = 3
        print("Modo Difícil selecionado")

    elif opcao == 4:
        print("Saindooo do jogo :( ...")
        break

    else:
        print("Essa opção é inválida >:c ")
        continue

    numero = random.randint(0, sorteio_max)
    tentativas = 1

    while tentativas <= tentativas_max:
        chute = int(input(f"Digite o seu chute (0 a {sorteio_max}): "))

        if chute == numero:
            print(" Parabéns!!! Você acertou <3 ")
            break

        elif chute < numero:
            print("Dica: o número sorteado é MAIOR!!!")

        else:
            print("Dica: o número sorteado é MENOR!!!")

        tentativas += 1

    if tentativas > tentativas_max:
        print("Já era, suas tentativas acabaram.")
        print("O número era:", numero)