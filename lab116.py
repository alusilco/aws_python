import random

print("Welcome to Guess the Number!")
print("The rules are simple. I will think of a number, and you will try to guess it.")

number = random.randint(1,10)
isGuessRight = False


while isGuessRight != True:
    guess = input("Guess a number between 1 and 10: ")
    if int(guess) == number:
        print("You guessed {}. That is correct! You win!".format(guess))
        isGuessRight = True
    else:
        print("You guessed {}. Sorry, that isn’t it. Try again.".format(guess))


        # Definir la respuesta correcta
respuesta_correcta = "respuesta"

# Iniciar el bucle while
while True:
    # Pedir al usuario que haga una suposición
    suposicion = input("Adivina la respuesta: ")

    # Verificar si la suposición es correcta
    if suposicion == respuesta_correcta:
        # Informar al usuario que adivinó correctamente
        print("¡Felicidades! Has adivinado la respuesta.")
        # Salir del bucle
        break
    else:
        # Informar al usuario que la suposición fue incorrecta
        print("Lo siento, esa no es la respuesta correcta. Intenta de nuevo.")

# Fin del bucle


