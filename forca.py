def jogar():
    ## Jogo de Adivinhacao
    print("------------------------------------------")
    print("             Jogo de Forca                ")
    print("------------------------------------------")
    print("              Bem vindx !                 ")
    print("------------------------------------------")
    print("    Níveis:                               ")
    print("           Fácil   - 1                    ")
    print("           Médio   - 2                    ")
    print("           Dificil - 3                    ")
    print("------------------------------------------")

    while (1):
        dificuldade = input("Digite o número corespendente ao nível: ")
        dificuldade = int(dificuldade)
        if (dificuldade <= 3 and dificuldade >= 1):
            break

    pontos = 1500
    numero_secreto = random.randrange(1, 101)

    numero_do_palpite = 1
    numero_maximo_palpites = 20 - 5 * dificuldade


if (__name__ == "__main__"):
    jogar()
