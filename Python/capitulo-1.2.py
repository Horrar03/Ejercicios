from math import sqrt, gcd
from typing import TypeVar
import os, msvcrt

A = TypeVar('A')
B = TypeVar('B')


# Capitulo 1; Definiciones elementales de funciones
# 1.2 Definiciones con condicionales, guardas o patrones
# En esta relación se presentan ejercicios con definiciones elementales
# (no recursivas) de funciones que usan condicionales, guardas o patrones.



while True:

    os.system('cls')
    problemas = {
        print("\n·Escribe 0 para salir" \
        "\n·Ejercicio 1: Division segura" \
        "\n·Ejercicio 2: Tabla XOR" \
        "\n·Ejercicio 3: Mayor de 2 rectangulos" \
        "\n·Ejercicio 4: Intercambiar valores" \
        "\n·Ejercicio 5: Distancia entre puntos" \
        "\n·Ejercicio 6: Mover elementos -1 en una tupla" \
        "\n·Ejercicio 7: Mayor numero formable de 2 enteros" \
        "\n·Ejercicio 8: Cantidad de raíces" \
        "\n·Ejercicio 9: Raices realesde una ecuación" \
        "\n·Ejercicio 10: Formula de heron" \
        "\n·Ejercicio 11: Intersecciones" \
        "\n·Ejercicio 12: Numeros racionales" \
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

    elif opc == 5:
        # Ejercicio 5. Definir la función
        # distancia : (tuple[float, float], tuple[float, float]) -> float
        # tal que distancia(p1, p2) es la distancia entre los puntos p1 y
        # p2. Por ejemplo,
        # distancia((1, 2), (4, 6)) == 5.0
        #
        # Comprobar con Hypothesis que se verifica la propiedad triangular de
        # la distancia; es decir, dados tres puntos p1, p2 y p3, la distancia
        # de p1 a p3 es menor o igual que la suma de la distancia de p1 a p2 y
        # la de p2 a p3.
        def distancia(p1, p2):
            (x1, y1) = p1
            (x2, y2) = p2
            return sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        
        print("Ejercicio 5.1: ", distancia((1, 2), (4, 6)))
        print("Ejercicio 5.2: ", distancia((3, 10), (9, 4)))
        msvcrt.getch()

    elif opc == 6:
        # Ejercicio 6. Definir una función
        # ciclo : (list[A]) -> list[A]
        # tal que ciclo(xs) es la lista obtenida permutando cíclicamente los
        # elementos de la lista xs, pasando el último elemento al principio de
        # la lista. Por ejemplo,
        # ciclo([2, 5, 7, 9]) == [9, 2, 5, 7]
        # ciclo([]) == []
        # ciclo([2]) == [2]
        #
        # Comprobar que la longitud es un invariante de la función ciclo; es
        # decir, la longitud de (ciclo xs) es la misma que la de xs.
        def ciclo(xs):
            if len(xs) == 0:
                return []
            else:
                return [xs[-1]]+xs[:-1]
        
        print("Ejercicio 6.1: ", ciclo([2, 5, 7, 9]))
        print("Ejercicio 6.2: ", ciclo([]))
        print("Ejercicio 6.3: ", ciclo([2]))
        print("Ejercicio 6.4: ", ciclo([1, 2, 3, 4, 5]))
        print("Ejercicio 6.5: ", ciclo(['a', 'b', 'c']))
        msvcrt.getch()

    elif opc == 7:
        # Ejercicio 7. Definir la función
        # numeroMayor : (int, int) -> int
        # tal que numeroMayor(x, y) es el mayor número de dos cifras que puede
        # construirse con los dígitos x e y. Por ejemplo,
        # numeroMayor(2, 5) == 52
        # numeroMayor(5, 2) == 52
        def numeromayor(x, y):
            if x >= y:
                return x * 10 + y
            else:
                return y * 10 + x
            
        print("Ejercicio 7.1: ", numeromayor(2, 5))
        print("Ejercicio 7.2: ", numeromayor(5, 2))
        print("Ejercicio 7.3: ", numeromayor(4, 1))
        print("Ejercicio 7.4: ", numeromayor(9, 9))
        print("Ejercicio 7.5: ", numeromayor(0, 7))
        print("Ejercicio 7.6: ", numeromayor(1, 4))
        msvcrt.getch()

    elif opc == 8:
        # Ejercicio 8. Definir la función
        # numeroDeRaices : (float, float, float) -> float
        # tal que numeroDeRaices(a, b, c) es el número de raíces reales de la
        # ecuación a*x^2 + b*x + c = 0. Por ejemplo,
        # numeroDeRaices(2, 0, 3) == 0
        # numeroDeRaices(4, 4, 1) == 1
        # numeroDeRaices(5, 23, 12) == 2
        def nuumeroDeRaices(a, b, c):
            i = b ** 2 - 4 * a * c
            if i < 0:
                return 0
            elif i == 0:
                return 1
            else:
                return 2
            
        print("Ejercicio 8.1: ", nuumeroDeRaices(2, 0, 3))
        print("Ejercicio 8.2: ", nuumeroDeRaices(4, 4, 1))
        print("Ejercicio 8.3: ", nuumeroDeRaices(5, 23, 12))
        print("Ejercicio 8.4: ", nuumeroDeRaices(1, -2, 1))
        print("Ejercicio 8.5: ", nuumeroDeRaices(1, 0, 1))
        msvcrt.getch()

    elif opc == 9:
        # Ejercicio 9. Definir la función
        # raices : (float, float, float) -> list[float]
        # tal que raices(a, b, c) es la lista de las raíces reales de la
        # ecuación ax^2 + bx + c = 0. Por ejemplo,
        # raices(1, 3, 2) == [-1.0,-2.0]
        # raices(1, (-2), 1) == [1.0,1.0]
        # raices(1, 0, 1) == []
        # Comprobar con Hypothesis que la suma de las raíces de la ecuación
        # ax^2 + bx + c = 0 (con a no nulo) es -b/a y su producto es c/a.
        def raices(a, b, c):
            i = b ** 2 - 4 * a * c
            if i < 0: 
                return []
            elif i == 0:
                return [(-b) / 2 * a, (-b) / 2 * a]
            else:
                r1 = ((-b) + sqrt(i)) / (2 * a)
                r2 = ((-b) - sqrt(i)) / (2 * a)
                return [r1, r2]
        
        print("Ejercicio 9.1: ", raices(1, 3, 2))
        print("Ejercicio 9.2: ", raices(1, -2, 1))
        print("Ejercicio 9.3: ", raices(1, 0, 1))
        print("Ejercicio 9.4: ", raices(2, 4, 2))
        print("Ejercicio 9.5: ", raices(1, -3, 2))
        msvcrt.getch()

    elif opc == 10:
        # Ejercicio 10. La fórmula de Herón, descubierta por Herón de
        # Alejandría, dice que el área de un triángulo cuyo lados miden a, b y c
        # es la raíz cuadrada de s(s-a)(s-b)(s-c) donde s es el semiperímetro
        # s = (a+b+c)/2
        #
        # Definir la función
        # area : (float, float, float) -> float
        # tal que area(a, b, c) es el área del triángulo de lados a, b y c. Por
        # ejemplo,
        # area(3, 4, 5) == 6.0

        def area(a, b, c):
            s = (a + b + c) / 2
            return sqrt(s*(s - a) * (s - b) * (s - c))
        
        print("Ejercicio 10.1: ", area(3, 4, 5))
        print("Ejercicio 10.2: ", area(5, 12, 13))
        print("Ejercicio 10.3: ", area(7, 24, 25))
        msvcrt.getch()

    elif opc == 11:
        # Ejercicio 11. Los intervalos cerrados se pueden representar mediante
        # una lista de dos números (el primero es el extremo inferior del
        # intervalo y el segundo el superior).
        #
        # Definir la función
        # interseccion : (list[float], list[float]) -> list[float]
        # tal que interseccion(i1, i2) es la intersección de los intervalos i1 e
        # i2. Por ejemplo,
        # interseccion([], [3, 5]) == []
        # interseccion([3, 5], []) == []
        # interseccion([2, 4], [6, 9]) == []
        # interseccion([2, 6], [6, 9]) == [6, 6]
        # interseccion([2, 6], [0, 9]) == [2, 6]
        # interseccion([2, 6], [0, 4]) == [2, 4]
        # interseccion([4, 6], [0, 4]) == [4, 4]
        # interseccion([5, 6], [0, 4]) == []
        #
        # Comprobar con Hypothesis que la intersección de intervalos es
        # conmutativa.

        def interseccion(i1, i2):
            if len(i1) == 0 or len(i2) == 0:
                return []
            a = max(i1[0], i2[0])
            b = min(i1[1], i2[1])
            if a > b:
                return []
            else:
                return [a, b]
        
        print("Ejercicio 11.1: ", interseccion([], [3, 5]))
        print("Ejercicio 11.2: ", interseccion([3, 5], []))
        print("Ejercicio 11.3: ", interseccion([2, 4], [6, 9]))
        print("Ejercicio 11.4: ", interseccion([2, 6], [6, 9]))
        print("Ejercicio 11.5: ", interseccion([2, 6], [0, 9]))
        print("Ejercicio 11.6: ", interseccion([2, 6], [0, 4]))
        print("Ejercicio 11.7: ", interseccion([4, 6], [0, 4]))
        print("Ejercicio 11.8: ", interseccion([5, 6], [0, 4]))
        msvcrt.getch()

    elif opc == 12:
        while True:
            os.system('cls')
            opc =  int(input("Problemas de numeros racionales: " \
                            "\n·Escribe 0 para salir" \
                            "\n·Escribe 1 para forma reducida" \
                            "\n·Escribe 2 para suma de racionales" \
                            "\n·Escribe 3 para producto de racionales" \
                            "\n·Escribe 4 para igualdad de racionales" \
                            "\n·Escribe la opcion: "))
            if opc == 0:
                break

            elif opc == 1:
            
                # Ejercicio 12.1 Los números racionales pueden representarse mediante
                # pares de números enteros. Por ejemplo, el número 2/5 puede
                # representarse mediante el par (2,5).
                #
                # El tipo de los racionales se define por
                # Racional = tuple[int, int]
                #
                # Definir la función
                # formaReducida : (Racional) -> Racional
                # tal que formaReducida(x) es la forma reducida del número racional
                # x. Por ejemplo,
                # formaReducida((4, 10)) == (2, 5)
                # formaReducida((0, 5)) == (0, 1)
                def formaReducida(x):
                    (i , j ) = x
                    if i == 0:
                        return (0, 1)
                    else:
                        m = gcd(i, j)
                        return (i//m , j//m)
                    
                print("Ejercicio 12.1: ", formaReducida((4, 10)))
                print("Ejercicio 12.2: ", formaReducida((0, 5)))
                print("Ejercicio 12.3: ", formaReducida((15, 35)))
                msvcrt.getch()

            elif opc == 2:
                # Ejercicio 12.2. Definir la función
                # sumaRacional : (Racional, Racional) -> Racional
                # tal que sumaRacional(x, y) es la suma de los números racionales x e y,
                # expresada en forma reducida. Por ejemplo,
                # sumaRacional((2, 3), (5, 6)) == (3, 2)
                # sumaRacional((3, 5), (-3, 5)) == (0, 1)
                def sumaRacional(x, y):
                    (a, b) = x
                    (c, d) = y
                    num = a * d + b * c
                    den = b * d
                    if num == 0:
                        return (0, 1)
                    else:
                        m = gcd(num, den)
                        return (num//m, den//m)
                
                print("Ejercicio 12.1: ", sumaRacional((2, 3), (5, 6)))
                print("Ejercicio 12.2: ", sumaRacional((3, 5), (-3, 5)))
                print("Ejercicio 12.3: ", sumaRacional((1, 4), (1, 4)))
                msvcrt.getch()

            elif opc == 3:
                # Ejercicio 12.3. Definir la función
                # productoRacional : (Racional, Racional) -> Racional
                # tal que productoRacional(x, y) es el producto de los números
                # racionales x e y, expresada en forma reducida. Por ejemplo,
                # productoRacional((2, 3), (5, 6)) == (5, 9)

                def productoRacional(x, y):
                    (i, j) = x
                    (m, n) = y
                    num = i * m
                    den = j * n
                    if num == 0:
                        return (0, 1)
                    else:
                        mc = gcd(num, den)
                        return (num//mc, den//mc)
                    
                print("Ejercicio 12.1: ", productoRacional((2, 3), (5, 6)))
                print("Ejercicio 12.2: ", productoRacional((3, 5), (10, 9)))
                print("Ejercicio 12.3: ", productoRacional((0, 5), (4, 7)))
                msvcrt.getch()

            elif opc == 4:
                # Ejercicio 12.4. Definir la función
                # igualdadRacional : (Racional, Racional) -> bool
                # tal que igualdadRacional(x, y) se verifica si los números racionales x
                # e y son iguales. Por ejemplo,
                # igualdadRacional((6, 9), (10, 15)) == True
                # igualdadRacional((6, 9), (11, 15)) == False
                # igualdadRacional((0, 2), (0, -5)) == True
                def igualdadRacional(x, y):
                    (i, j) = x
                    (m, n) = y
                    return i * n == j * m
                print("Ejercicio 12.1: ", igualdadRacional((6, 9), (10, 15)))
                print("Ejercicio 12.2: ", igualdadRacional((6, 9), (11, 15)))
                print("Ejercicio 12.3: ", igualdadRacional((0, 2), (0, -5)))
                msvcrt.getch()
