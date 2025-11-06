import os, random
def randomNum():
    os.system('cls')
    num = random.randint(1, 100)
    intentos = 0
    while True:
        try:
            guess = int(input("Escribe un numero: "))
            if guess == num:
                intentos += 1
                print(f"¡Has acertado!\nutilizaste {intentos} intentos", )
                break
            else:
                intentos += 1
                if guess < num:
                    print("El numero es mas alto\n")
                else:
                    print("El numero es mas bajo\n")
                if intentos >= 5:
                    print(f"Has perdido, el numero era {num}")
                    break
        except ValueError:
            print("Por favor, ingresa un numero valido.\n")
            pass
randomNum()