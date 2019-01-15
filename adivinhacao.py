import random


def jogo():
    print("********************************")
    print("Bem vindo ao jogo de advinhação!")
    print("********************************")

    num_secreto = round(random.randrange(0, 101))
    total_de_tentativas = 0
    rodada = 1
    pontos = 1000

    print("(1) Fácil (2) Médio (3) Difícil")
    nivel = int(input("Escolha o nível: "))

    if nivel == 1:
        total_de_tentativas = 20
    elif nivel == 2:
        total_de_tentativas = 10
    elif nivel == 3:
        total_de_tentativas = 5
    else:
        print("Por favor, escolha um nível válido!")

    # while (rodada <= total_de_tentativas):
    for rodada in range(1, total_de_tentativas + 1):
        print("Rodada {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número:")
        chute = int(chute_str)

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!")
            continue

        acertou = chute == num_secreto
        maior = chute > num_secreto
        menor = chute < num_secreto

        if acertou:
            print("Você acertou, e fez {} pontos".format(pontos))
            break
        else:
            if maior:
                print("Você errou! Tente um numero menor.")
            elif menor:
                print("Você errou! Tente um numero maior.")

    print("Final do jogo.")
    pontos_perdidos = abs(num_secreto - chute)
    pontos = pontos - pontos_perdidos


if __name__ == "__main__":
    jogo()