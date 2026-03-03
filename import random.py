import random

numero_secreto = random.randint(1, 100)

while True:
    chute = int(input("Adivinhe o número (1 a 100): "))

    if chute == numero_secreto:
        print("Acertou! 🎉")
        break
    elif chute > numero_secreto:
        print("Muito alto! Tente de novo.")
    else:
        print("Muito baixo! Tente de novo.")