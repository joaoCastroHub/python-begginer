import forca
import adivinhacao

def escolhe_jogo():
    print("*********************************")
    print("Escolha o seu jogoa!")
    print("*********************************")

    print("(1) forca (2)Adivinhacao")

    jogo = int(input("Qual jogo? "))

    if(jogo == 1):
        print("Jogando forca ...")
        forca.jogar()
    elif(jogo == 2):
        print("Jogando adivinhacao ...")
        adivinhacao.jogar()

if(__name__ == "__main__"):
    escolhe_jogo()