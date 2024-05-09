import random
import pygame
import time

#to do
#music on or off

again = "n"
values = []
difficulty = 1

pygame.mixer.init()
bad_sound = pygame.mixer.Sound(file= "fx/lofi eff bad.mp3")
good_sound = pygame.mixer.Sound(file= "fx/lofi eff good.mp3")

back_music = pygame.mixer.music.load("fx/lofi.mp3")
pygame.mixer.music.set_volume(0.7)

pygame.mixer.music.play(-1, 0.0, 3000)

def reset():
    global again, difficulty
    again = input("Do you want to try again? (y/n)    ")
    difficulty = int(input("""Choose a difficulty level:
        1. Easy
        2. Medium
        3. Hard
        >"""))
    return again, difficulty

def welcome():
    print("Welcome to Cops and Robbers!")
    print("You have only 10 chances to guess a safe 5-digits lockcode before cops arrive.")
    play()

def play():
    global difficulty
    difficulty = int(input("""Choose a difficulty level:
1. Easy
2. Medium
3. Hard
>"""))
    while True:

        numberFin = [1, 2, 3, 4, 5]

        if difficulty == 1:
            numero_intentos = 10
        elif difficulty == 2:
            numero_intentos = 7
        elif difficulty == 3:
            numero_intentos = 5
        else:
            numero_intentos = 10
        win = False

        values.clear()  # Limpiar la lista de valores para cada nuevo juego

        for i in range(5):
            randy = random.randint(0, 9)
            values.append(randy)
            correcto = "".join(map(str, values))
            correcto_num = int(correcto)

        while not win and correcto_num != numberFin and numero_intentos > 0:
            number = int(input(f"""Hurry up! Guess the 5 digits safe lockcode in less than {numero_intentos} attempts: 
            
>"""))
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
                pygame.mixer.Sound.play(good_sound)
                print("""
                                        ⠀⠀⠀⣀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⢯⠙⠩⠀⡇⠊⠽⢖⠆⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠱⣠⠀⢁⣄⠔⠁⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠀⣷⣶⣾⣾⠀⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⠀⢀⡔⠙⠈⢱⡟⣧⠀⠀⠀⠀⠀⠀⠀
                                ⠀⠀⠀⠀⠀⡠⠊⠀⠀⣀⡀⠀⠘⠕⢄⠀⠀⠀⠀⠀
                                ⠀⠀⠀⢀⠞⠀⠀⢀⣠⣿⣧⣀⠀⠀⢄⠱⡀⠀⠀⠀
                                ⠀⠀⡰⠃⠀⠀⢠⣿⠿⣿⡟⢿⣷⡄⠀⠑⢜⢆⠀⠀
                                ⠀⢰⠁⠀⠀⠀⠸⣿⣦⣿⡇⠀⠛⠋⠀⠨⡐⢍⢆⠀
                                ⠀⡇⠀⠀⠀⠀⠀⠙⠻⣿⣿⣿⣦⡀⠀⢀⠨⡒⠙⡄
                                ⢠⠁⡀⠀⠀⠀⣤⡀⠀⣿⡇⢈⣿⡷⠀⠠⢕⠢⠁⡇
                                ⠸⠀⡕⠀⠀⠀⢻⣿⣶⣿⣷⣾⡿⠁⠀⠨⣐⠨⢀⠃
                                ⠀⠣⣩⠘⠀⠀⠀⠈⠙⣿⡏⠁⠀⢀⠠⢁⡂⢉⠎⠀
                                ⠀⠀⠈⠓⠬⢀⣀⠀⠀⠈⠀⠀⠀⢐⣬⠴⠒⠁⠀⠀
                                ⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠀⠀⠀⠀⠀⠀⠀    
                        Gratz fellow robber! You guessed it!""")
                reset()
                break  # Salir del bucle interno si el jugador adivina el número
            elif number >= 99999:
                print("Don't be a cheater! The code you're looking for is between 00000 y 99999")
                numero_intentos -= 1
            else:
                numero_intentos -= 1
                if numero_intentos == 0:
                    print("""
                                              ▒▒▒▒▒▒                                        
                                          ▒▒▒▒▒▒▒▒▒▒                                    
                                  ██████████▒▒▒▒▒▒▒▒████                                
                                ░░░░██████████▒▒▒▒▒▒██████                              
                                ░░░░░░██████████████████████                            
                              ░░░░░░░░████████████████████████                          
                            ░░░░░░░░██████░░░░░░██░░░░░░░░████                          
                  ░░░░░░░░░░░░░░░░██████░░░░░░░░██░░░░░░░░████                          
                ░░░░░░░░░░░░░░░░██████░░░░░░░░░░██░░░░░░░░████░░                        
                ░░░░░░░░░░░░░░████████████████████████████████░░░░                      
              ██░░░░░░░░░░░░░░░░██████████░░██░░░░██░░████████░░░░░░                    
              ████░░░░░░░░░░░░░░░░██████░░░░░░░░░░░░░░░░██████░░░░░░░░                  
              ████████░░░░▒▒▒▒░░░░██████░░░░░░░░░░░░░░░░████░░░░░░░░░░░░                
                ████████▒▒▒▒▒▒▒▒░░████████░░░░░░░░░░░░████▒▒▒▒▒▒▒▒░░░░░░                
                  ████▒▒▒▒░░░░▒▒▒▒████████████████████████▒▒░░░░▒▒░░░░                  
                      ▒▒▒▒░░░░▒▒▒▒                ██████▒▒▒▒░░░░▒▒▒▒                    
                      ▒▒▒▒▒▒▒▒▒▒▒▒                      ▒▒▒▒▒▒▒▒▒▒▒▒                    
                        ▒▒▒▒▒▒▒▒                          ▒▒▒▒▒▒▒▒                      
                                       
                Cops have arrived before you were able to get the money :(
                        """)
                    pygame.mixer.Sound.play(bad_sound)
                    time.sleep(2)
                    pygame.mixer.Sound.play(bad_sound)
                    print("The correct lockcode was ", correcto_num)
                    print(f"You were {correcto_num - number} numbers away from the correct code.")
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
                print("You can hear some sounds coming from the lock. Your intuition says the lockcode could be greater, fellow robber.")
            elif correcto_num < number:
                print("You can hear some sounds coming from the lock. Your intuition says the code could be lesser, fellow robber.")
            print(f"You have {numero_intentos} attempts left.")

        if again == "n":
            break  # Salir del bucle externo si el jugador no quiere jugar otra vez

    print("Thanks for playing!")

welcome()
