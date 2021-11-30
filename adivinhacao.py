import random

def jogar():
    ## Jogo de Adivinhacao

    print("------------------------------------------")
    print("          Jogo de Adivinhação             ")
    print("------------------------------------------")
    print("    Níveis:                               ")
    print("           Fácil   - 1                    ")
    print("           Médio   - 2                    ")
    print("           Dificil - 3                    ")
    print("------------------------------------------")

    while(1):
        dificuldade = input("Digite o número corespendente ao nível: ")
        dificuldade = int(dificuldade)
        if (dificuldade <= 3 and dificuldade >= 1):
            break

    pontos = 1500
    numero_secreto = random.randrange(1,101)

    numero_do_palpite = 1
    numero_maximo_palpites = 20 - 5 * dificuldade

    while (numero_do_palpite <= numero_maximo_palpites):

        print("Tentativa {} de {}".format(numero_do_palpite, numero_maximo_palpites))
        palpite = input("Digite seu palpite entre 1 e 100: ")

        ## Por padrao input retorna uma Str - Python3 -
        ## Precisamos converter para Int para poder comparar

        palpite = int(palpite)

        if palpite > 100 or palpite < 1:
            print("Número inválido tente novamente")
            continue

        ultimo_palpite = numero_do_palpite == numero_maximo_palpites

        acertou = palpite == numero_secreto
        maior = palpite > numero_secreto


        if (acertou):
            print("Você acertou! :)")
            print(f"Pontuação: {pontos}")
            break
        else:
            print("Você errou :/ ")

            pontos_perdidos = abs(numero_secreto - palpite)
            pontos = pontos - pontos_perdidos

            if(ultimo_palpite):
                print(f"O numero era {numero_secreto}")
            else:
                if(maior):
                    print("O Número digitado é Maior do que Número Secreto")
                else:
                    print("O Número digitado é Menor do que Número Secreto")

        print("------------------------------------------")

        numero_do_palpite += 1

    print("Fim do jogo")

if (__name__ == "__main__"):
    jogar()
