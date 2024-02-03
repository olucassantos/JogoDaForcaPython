import random
import os

lista_palavras = [
    "PITANGA",
    "SALSICHA",
    "COTOVELO",
    "MOTOR",
    "CELULA",
    "TAMARINDO",
    "RODINHA",
    "SIRENE"
]

lista_letras_corretas = []

# Sistema sorteia uma palavra e define as chances
palavra_sorteada = random.choice(lista_palavras)
quantidade_chances = len(palavra_sorteada) + 2

# Sistema mostra regras do jogo
print("Bem-vindo ao jogo da forca!")
print("Você tem", quantidade_chances, "chances para acertar a palavra.")
print("Você pode chutar uma letra ou a palavra inteira.")
print("Caso erre a palavra, você perde o jogo!")
print("Boa sorte!")

input("Pressione ENTER para começar...")

# Sistema limpa a tela
os.system("cls")

while quantidade_chances > 0:
    os.system("cls")
    # Sistema desenha a forca
    print("Tentativas restantes:", quantidade_chances)

    falta_letras = False

    for letra in palavra_sorteada:
        if letra in lista_letras_corretas:
            print(letra, end=" ")
        else:
            print("_", end=" ")
            falta_letras = True

    # Quebra a linha
    print("\n")

    if not falta_letras:
        quantidade_chances = 0
        perdeu = False
        break

    # Usuário chuta uma palavra ou letra
    palpite = input("Digite uma letra ou a palavra: ").upper()

    if len(palpite) > 1:
        # é uma palavra
        if not palpite == palavra_sorteada:
            quantidade_chances = 0
            perdeu = True
        else:
            quantidade_chances = 0
            perdeu = False
    else:
        # é uma letra
        acertou = False
        for letra in palavra_sorteada:
            if letra == palpite:
                acertou = True
                lista_letras_corretas.append(letra)

        if not acertou:
            quantidade_chances -= 1
            perdeu = True

if not perdeu:
    print("Parabéns! Você acertou a palavra!")
else:
    print("Que pena! Você perdeu! A palavra era", palavra_sorteada)