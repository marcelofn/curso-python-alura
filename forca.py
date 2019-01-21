import random


def jogo():
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")

    arquivo = open('palavras.txt', 'r')
    palavras = []

    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)

    arquivo.close()
    numero = random.randrange(0, len(palavras))

    palavra_secreta = palavras[numero].upper()
    letras_acertadas = ["_" for letra in palavra_secreta]
    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while not acertou and not enforcou:
        chute = input("Qual a letra?")
        chute = chute.strip().upper()

        if chute in palavra_secreta:
            index = 0
            for letra in palavra_secreta:
                if letra == chute:
                    letras_acertadas[index] = letra
                index += 1
        else:
            erros += 1
            print("Ops você errou! Ainda restam {} tentativas".format(6 - erros))
        enforcou = erros == 6
        acertou = "_" not in letras_acertadas
        letras_faltando = str(letras_acertadas.count("_"))
        print(letras_acertadas)
        print("Ainda faltam acertar {} letras.".format(letras_faltando))
    if (acertou):
        print("Você ganhou!!, A palavra é {}".format(palavra_secreta))
    else:
        print("Você perdeu!!")
    print("Fim do jogo")


if __name__ == "__main__":
    jogo()
