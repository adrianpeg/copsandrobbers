import random

again = "n"
values = []  # Definición de la lista values

def reset():
    global again
    again = input("¿Do you want to try again? (y/n)    ")
    return again

def welcome():
    print("Welcome to Cops and Robbers!")
    print("You have only 10 chances to guess a safe 5-digits lockcode before cops arrive.")
    play()

def play():
    while True:
        numberFin = [1, 2, 3, 4, 5]
        numero_intentos = 10
        win = False

        values.clear()  # Limpiar la lista de valores para cada nuevo juego

        for i in range(5):
            randy = random.randint(0, 9)
            values.append(randy)
            correcto = "".join(map(str, values))
            correcto_num = int(correcto)

        while not win and correcto_num != numberFin and numero_intentos > 0:
            number = int(input("Hurry up! Guess the safe lockcode: "))
            # Calcula cada dígito por separado
            n1 = number // 10000
            n2 = (number % 10000) // 1000
            n3 = (number % 1000) // 100
            n4 = (number % 100) // 10
            n5 = number % 10

            n1rev = n1 == values[0]
            n2rev = n2 == values[1]
            n3rev = n3 == values[2]
            n4rev = n4 == values[3]
            n5rev = n5 == values[4]

            if correcto_num == number:
                print("Gratz fellow robber! You guessed it!")
                reset()
                break  # Salir del bucle interno si el jugador adivina el número
            elif number >= 99999:
                print("Don't be a cheater! The number you're looking for is between 00000 y 99999")
                numero_intentos -= 1
            else:
                numero_intentos -= 1
                if numero_intentos == 0:
                    print("Sadly, you exceeded the number of attempts.")
                    print("The correct lockcode was ", correcto_num)
                    print(f"You are at {correcto_num - number} from the correct number.")
                    reset()
                    break  # Salir del bucle interno si se excede el número máximo de intentos

            if not n1rev:
                n1rev = "_"
            else:
                n1rev = values[0]
                numberFin.append(values[0])
            if not n2rev:
                n2rev = "_"
            else:
                n2rev = values[1]
                numberFin.append(values[1])
            if not n3rev:
                n3rev = "_"
            else:
                n3rev = values[2]
                numberFin.append(values[2])
            if not n4rev:
                n4rev = "_"
            else:
                n4rev = values[3]
                numberFin.append(values[3])
            if not n5rev:
                n5rev = "_"
            else:
                n5rev = values[4]
                numberFin.append(values[4])

            print(f"{n1rev}   {n2rev}   {n3rev}   {n4rev}   {n5rev}")
            if correcto_num > number:
                print("You hear some sounds coming from the lock. The lockcode seems to be greater, fellow robber.")
            elif correcto_num < number:
                print("You can hear some sounds coming from the lock. The lockcode seems to be lesser, fellow robber.")
            print(f"You have {numero_intentos} attempts left.")

        if again == "n":
            break  # Salir del bucle externo si el jugador no quiere jugar otra vez

    print("Thanks for playing!")

welcome()