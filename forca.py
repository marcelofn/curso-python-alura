def jogo():
    print("********************************")
    print("Bem vindo ao jogo de forca!")
    print("********************************")
    palavra_secreta = "banana"
    letras_acertadas = ["_", "_", "_", "_", "_", "_"]
    enforcou = False
    acertou = False

    while not acertou and not enforcou:
        chute = input("Qual a letra?")
        chute = chute.strip()

        index = 0

        for letra in palavra_secreta:
            if letra.upper() == chute.upper():
                letras_acertadas[index] = letra

            index = index + 1
            letras_faltando = str(letras_acertadas.count("_"))
        print(letras_acertadas)
        print("Ainda faltam acertar {}".format(letras_faltando))


if __name__ == "__main__":
    jogo()