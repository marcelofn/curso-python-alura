import forca
import adivinhacao


def escolha_jogo():
    print("********************************")
    print("*******Escolha seu jogo*********")
    print("********************************")

    print("Escolha: (1) Forca (2) Adivinhação")

    jogo = int(input("Escolha o jogo: "))

    if jogo == 1:
        print("Você escolheu o jogo da forca")
        forca.jogo()
    elif jogo == 2:
        print("Você escolheu o jogo de advinhação")
        adivinhacao.jogo()
    else:
        print("Você precisa escolher um jogo!")


if __name__ == "__main__":
    escolha_jogo()
