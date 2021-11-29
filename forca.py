import getpass

def jogar():
    ## Jogo de Forca

    print("------------------------------------------")
    print("              Jogo da Forca               ")
    print("------------------------------------------")
    print(" ")
    palavra_secreta_str = getpass.getpass(prompt='Digite sua palavra secreta: ')

    ##palavra_secreta_str = input("Digite sua palavra secreta: ")

    palavra_secreta = list(palavra_secreta_str)
    letras_acertadas = []

    index = 0
    for letra in palavra_secreta:
        if letra == " ":
            palavra_secreta[index] = "-"
            letras_acertadas.append("-")
        else:
            letras_acertadas.append("_")
        index += 1

    print(" ")
    for letra in letras_acertadas:
        print(letra, end=" ")
    print(' ')

    acertou = False
    enforcado = False

    erros_maximos = 5
    erros = 0

    while not acertou and not enforcado:
        print(" ")
        chute = input("Digite uma Letra: ")
        print(" ")
        chute = chute.strip()

        acertou_letra = 0

        index = 0
        for letra in palavra_secreta:
            if (chute.lower() == letra.lower()):
                acertou_letra = 1
                letras_acertadas[index] = letra.lower()
            index += 1

        for letra in letras_acertadas:
            print(letra, end=" ")
        print(" ")

        if not acertou_letra:
            erros += 1

            if erros == erros_maximos:
                enforcado = True
            else:
                print(' ')
                desenha_boneco(1,0,0,0)
                if erros > 1:
                    desenha_boneco(0,0,1,0)
                if erros > 2:
                    desenha_boneco(0, 0, 2, 0)
                if erros > 3:
                    desenha_boneco(0, 0, 0, 1)


        if letras_acertadas == palavra_secreta:
            acertou = True

    print(" ")
    print("Fim do jogo")

    if enforcado:
        print("Você perdeu :/")
        print("")
        desenha_boneco(2, 1, 2, 1)
        print("")
        print(f"A palavra era {palavra_secreta_str}")
    else:
        print("Parabéns! Você Ganhou! :)")
        print("")
        desenha_boneco(3, 0, 1, 1)
        print("")

def desenha_boneco(cabeca, corte, tronco, perna):

    cara_neutra = "      '-'       "
    cara_morta = "      X-X       "
    cara_feliz = "    \ ^-^ /    "
    corte_pescoco = "   --------     "
    tronco_so = "       │        "
    tronco_braco = "     / │ \      "
    duas_pernas = "      / └       "

    if cabeca == 1:
        print(cara_neutra)

    elif cabeca == 2:
        print(cara_morta)

    elif cabeca == 3:
        print(cara_feliz)

    if corte == 1:
        print(corte_pescoco)

    if tronco == 1:
        print(tronco_so)

    elif tronco == 2:
        print(tronco_braco)

    if perna == 1:
        print(duas_pernas)


if (__name__ == "__main__"):
    jogar()
