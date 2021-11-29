import forca
import adivinhacao

def escolhe_jogo():
    print("------------------------------------------")
    print("              Bem vindx !                 ")
    print("------------------------------------------")
    print("     Escolha o jogo que deseja jogar      ")
    print("------------------------------------------")
    print("         Jogo da Forca               - 1  ")
    print("         Adivinhe o numero secreto   - 2  ")
    print("------------------------------------------")

    jogo_escolhido = input(" Digite o numero corresspondente ao jogo: ")

    jogo_escolhido = int(jogo_escolhido)

    if (jogo_escolhido == 1):
        print("Jogando jogo da Forca")
        forca.jogar()
    elif(jogo_escolhido == 2):
        print("Jogando jogo Adivinhaçao")
        adivinhacao.jogar()

if (__name__ == "__main__"):
    escolhe_jogo()
