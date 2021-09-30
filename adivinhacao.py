print("*********************************")
print("Bem vindo ao jogo de adivinhacao!")
print("*********************************")

numero_secreto = 42
total_tentativas = 3
rodada = 1;

while(rodada <= total_tentativas):
    print("tentativa", rodada, "de", total_tentativas)
    chute_str = input("Digite o seu numero: ")
    print("voce digitou ", chute_str)
    chute = int(chute_str)

    acertou = chute == numero_secreto
    maior   = chute > numero_secreto
    menor   = chute < numero_secreto

    if (acertou):
        print("Voce acertou!")
    else:
        if(maior):
            print("Você errou! O seu numero foi maior do que o numero secreto.")
        elif(menor):
            print("Você errou! O seu numero foi menor do que o numero secreto.")

    rodada = rodada + 1


print("Fim do jogo")
