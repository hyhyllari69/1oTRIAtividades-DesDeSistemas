import adivinhacao
import forca

while True:
    print("\n=== MENU DE JOGOS ===")
    print("1 - Adivinhação")
    print("2 - Forca")
    print("3 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    
    if opcao == 1:
        adivinhacao.jogar()
    elif opcao == 2:
        forca.jogar()
    elif opcao == 3:
        print("Até logo! Obrigado por jogar <3")
        break
    else:
        print("Opção inválida!")