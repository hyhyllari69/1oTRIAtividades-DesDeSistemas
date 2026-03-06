# 1) Desenvolva a possibilidade do usuário escolher a dificuldade por meio de um menu de opções. Crie os níveis fácil, médio e difícil, configurando as variáveis conforme preferir. (1,5 pontos)

#Adicione no dicas no jogo, informando se o número sorteado é maior ou menor que o chute do usuário. (1,0 ponto)

#Valor total: 2,5 pontos
#Data de entrega: 12/03/2025






# Importação da biblioteca
import random

# Configurações do jogo
tentativas = 1
errou = True
sorteio_max = 10
tentativas_max = 3
numero = random.randint(0,sorteio_max)


while (tentativas <= tentativas_max):
    print("Tentativa:", tentativas)
    chute = int(input("Digite o seu chute (0 a 10):"))
    if chute == numero:
        print("Parabéns, você acertou <3")
        errou = False
        break
    else:
        print("Você errou </3")
    tentativas = tentativas + 1
    
if errou == True:
    print("O número sorteado era:", numero) # mostra p quem errou
print("### FIM DO JOGO ###")