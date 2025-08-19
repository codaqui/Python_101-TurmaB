import random # Biblioteca

numero_secreto = random.randint(1, 10)
tentativas = 0

while True:
    chute = int(input("Digite um numero entre 1 e 10: "))
    tentativas += 1
    if chute == numero_secreto:
        print("Parabens, voce acertou em", tentativas, "tentativas!")
        break
    elif chute < numero_secreto:
        print("Muito Baixo, tente de novo!")
    else:
        print("Muito alto, tente de novo!")