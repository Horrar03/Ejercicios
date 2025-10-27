from math import sqrt, gcd
from typing import TypeVar
import os, msvcrt

A = TypeVar('A')
B = TypeVar('B')

while True:

    os.system('cls')
    problemas = {
        print("\n·Escribe 0 para salir" \
        "\n·Ejercicio 1: Division segura" \
        "\n·Ejercicio 2: Tabla XOR" \
        "\n·Ejercicio 3: Mayor de 2 rectangulos" \
        "\n·Ejercicio 4: Intercambiar valores" \
        "\n·Ejercicio 5: " \
        "")
    }

    opc = int(input("Escribe la opcion a revisar: "))

    if opc == 0:
        break
    
    elif opc == 1:
        # Ejercicio 1. Definir la función
        # divisionSegura : (float, float) -> float
        # tal que divisionSegura(x, y) es x/y si y no es cero y 9999 en caso
        # contrario. Por ejemplo,
        # divisionSegura(7, 2) == 3.5
        # divisionSegura(7, 0) == 9999.0
        def divisionSegura(i, j):
            if j == 0:
                return 9999.0
            else:
                 return i / j
            
        print("Problema 1.1: ", divisionSegura(7, 2))
        print("Problema 1.2: ", divisionSegura(7, 0))
        msvcrt.getch()
        
    elif opc == 2:
        # Ejercicio 2. La disyunción excluyente de dos fórmulas se verifica si
        # una es verdadera y la otra es falsa. Su tabla de verdad es
        # x | y | xor x y
        # ------+-------+---------
        # True | True | False
        # True | False | True
        # False | True | True
        # False | False | False
        #
        # Definir la función
        # xor : (bool, bool) -> bool
        # tal que xor(x, y) es la disyunción excluyente de x e y. Por ejemplo,
        # xor(True, True) == False
        # xor(True, False) == True
        # xor(False, True) == True
        # xor(False, False) == False
        def xor(x, y):
            if x == True and y == True or x == False and y == False:
                return False
            if x == True:
                return True
            elif y == True:
                return True
            
        print("Ejercicio 2.1: ", xor(True, True))
        print("Ejercicio 2.2: ", xor(True, False))
        print("Ejercicio 2.1: ", xor(False, True))
        print("Ejercicio 2.1: ", xor(False, False))
        msvcrt.getch()
        
    elif opc == 3:
        #Ejercicio 3. Las dimensiones de los rectángulos puede representarse
        # por pares; por ejemplo, (5,3) representa a un rectángulo de base 5 y
        # altura 3.
        # Definir la función
        # mayorRectangulo : (tuple[float, float], tuple[float, float])
        # -> tuple[float, float]
        # tal que mayorRectangulo(r1, r2) es el rectángulo de mayor área entre
        # r1 y r2. Por ejemplo,
        # mayorRectangulo((4, 6), (3, 7)) == (4, 6)
        # mayorRectangulo((4, 6), (3, 8)) == (4, 6)
        # mayorRectangulo((4, 6), (3, 9)) == (3, 9)
        def mayorRectangulo(rect1, rect2):
            area1 = rect1[0] * rect1[1]
            area2 = rect2[0] * rect2[1]

            if area1 == area2:
                return "Mismo area"
            return rect1 if area1 > area2 else rect2
            
        print("Ejercicio 3.1: ", mayorRectangulo((4, 6), (3, 7)))
        print("Ejercicio 3.2: ", mayorRectangulo((4, 6), (3, 8)))
        print("Ejercicio 3.3: ", mayorRectangulo((4, 6), (3, 9)))
        msvcrt.getch()

    elif opc == 4:
        # Ejercicio 4. Definir la función
        # intercambia : (tuple[A, B]) -> tuple[B, A]
        # tal que intercambia(p) es el punto obtenido intercambiando las
        # coordenadas del punto p. Por ejemplo,
        # intercambia((2,5)) == (5,2)
        # intercambia((5,2)) == (2,5)
        #
        # Comprobar con Hypothesis que la función intercambia esidempotente; es
        # decir, si se aplica dos veces es lo mismo que no aplicarla ninguna.
        def intercambiar(s):
            (i ,j) = s
            return j, i
        
        print("Ejercicio 4.1: ", intercambiar((2, 5)))
        print("Ejercicio 4.2: ", intercambiar((5, 2)))
        print("Ejercicio 4.3: ", intercambiar((2, 2)))
        msvcrt.getch()
