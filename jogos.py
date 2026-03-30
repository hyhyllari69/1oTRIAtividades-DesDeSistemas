import adivinhacao
import forca
print("1 - Adivinhação")
print("2 - Forca")


opcao = int(input("Digite a opção desejada:"))

if opcao == 1:
    adivinhacao.jogar()
elif opcao == 2:
    forca.jogar()
else:
    print("Opção inválida")