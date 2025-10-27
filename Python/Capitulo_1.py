import math, msvcrt, os
from typing import TypeVar

pi = math.pi

while True:

        os.system('cls')
        problemas = {
        print("\n·Escribe 0 para salir" \
        "\n ·Ejercicio 1: 3 variables dentro de una funcion" \
        "\n ·Ejercicio 2: Suma de monedas" \
        "\n ·Ejercicio 3: Volumen esfera" \
        "\n ·Ejercicio 4: Area Corona Circular" \
        "\n ·Ejercicio 5: Ultimo digito" \
        "\n ·Ejercicio 6: Maximo de 3" \
        "\n ·Ejercicio 7: Rotar lista" \
        "\n ·Ejercicio 8: Rotar lista n cantidad de veces" \
        "\n ·Ejercicio 9: Rango de una lista de numeros" \
        "\n ·Ejercicio 10: Comprobar si una lista es palindromo" \
        "\n ·Ejercicio 11: Numeros interiores" \
        "\n ·Ejercicio 12: Numeros n finales de una lista" \
        "\n ·Ejercicio 13: Numeros comprendidos entre n y m" \
        "\n ·Ejercicio 14: Devuelve los primeros n numeros y m numeros de una lista" \
        "\n ·Ejercicio 15: Devuelve el numero medio, no el promedio" \
        "\n ·Ejercicio 16: Identifica si existen 3 numeros iguales" \
        "\n ·Ejercicio 17: Identifica si los numeros son diferentes" \
        "\n ·Ejercicio 18: Cuatro entradas iguales" \
        "")
        }
        opc = int(input("ingresa el numero de ejercicio a revisar: "))
        
        if opc == 0:
             break

        elif opc == 1:
            # Ejercicio 1. Definir la función
            # media3 : (float, float, float) -> float
            # tal que (media3 x y z) es la media aritmética de los números x, y y
            # z. Por ejemplo,
            # media3(1, 3, 8) == 4.0
            # media3(-1, 0, 7) == 2.0
            # media3(-3, 0, 3) == 0.0

            def media3(x, y, z :float):
                return (x + y + z)/3

            print("Ejercicio 1.1: ", media3(1, 3, 8))
            print("Ejercicio 2.1: ", media3(-1, 0, 7))
            print("Ejercicio 1.3: ", media3(-3, 0, 3))

            msvcrt.getch()

        # miguel.bizarro.171

            print("\n")
        elif opc == 2:
            # Ejercicio 2. Definir la función
            # sumaMonedas : (int, int, int, int, int) -> int
            # tal que sumaMonedas(a, b, c, d, e) es la suma de los euros
            # correspondientes a a monedas de 1 euro, b de 2 euros, c de 5 euros, d
            # 10 euros y e de 20 euros. Por ejemplo,
            # sumaMonedas(0, 0, 0, 0, 1) == 20
            # sumaMonedas(0, 0, 8, 0, 3) == 100
            # sumaMonedas(1, 1, 1, 1, 1) == 38

            def sumMonedas(a, b, c, d, e : int):
                return a * 1 + b * 2 + c * 5 + d * 10 + e * 20

            print("Ejercicio 2.1", sumMonedas(0, 0, 0, 0, 1))
            print("Ejercicio 2.2", sumMonedas(0, 0, 8, 0, 3))
            print("Ejercicio 2.3", sumMonedas(1, 1, 1, 1, 1))

            msvcrt.getch()


        elif opc == 3:
            # Ejercicio 3. Definir la función
            # volumenEsfera : (float) -> float
            # tal que volumenEsfera(r) es el volumen de la esfera de radio r. Por
            # ejemplo,
            # volumenEsfera(10) == 4188.790204786391
            
            def volEsfera(radio: float):
                return 4/3 * pi * radio ** 3

            print("Ejercicio 3.1: ", volEsfera(10))
            print("Ejercicio 3.2: ", volEsfera(2))
            print("Ejercicio 3.3: ", volEsfera(5))

            msvcrt.getch()

        elif opc == 4:
            #Ejercicio 4. Definir la función
            # areaDeCoronaCircular : (float, float) -> float
            # tal que areaDeCoronaCircular(r1, r2) es el área de una corona
            # circular de radio interior r1 y radio exterior r2. Por ejemplo,
            # areaDeCoronaCircular(1, 2) == 9.42477796076938
            # areaDeCoronaCircular(2, 5) == 65.97344572538566
            # areaDeCoronaCircular(3, 5) == 50.26548245743669
            def areaCoronaCircular(r1, r2):
                 return pi * (r2 ** 2 - r1 ** 2)
            
            print("Ejercicio 4.1: ", areaCoronaCircular(1, 2))
            print("Ejercicio 4.2: ", areaCoronaCircular(2, 5))
            print("Ejercicio 4.3: ", areaCoronaCircular(3, 5))

            msvcrt.getch()

        elif opc == 5:
            # Ejercicio 5. Definir la función
            # ultimoDigito : (int) -> int
            # tal que ultimoDigito(x) es el último dígito del número x. Por
            # ejemplo,
            # ultimoDigito(325) == 5

            def ultimoDigito(x):
                 return x % 10
            
            print("Ejercicio 5.1: ", ultimoDigito(325))
            print("Ejercicio 5.2: ", ultimoDigito(123214))
            print("Ejercicio 5.3: ", ultimoDigito(1))
            
            msvcrt.getch()

        elif opc == 6:
            # Ejercicio 6. Definir la función
            # maxTres : (int, int, int) -> int
            # tal que maxTres(x, y, z) es el máximo de x, y y z. Por ejemplo,
            # maxTres(6, 2, 4) == 6
            # maxTres(6, 7, 4) == 7
            # maxTres(6, 7, 9) == 9

            def maxTres(x, y, z):
                maximo = x, y, z, "maximo: ", max(x, max(y, z))
                return maximo
            
            print("Ejercicio 6.3: ", maxTres(6, 7, 9))
            print("Ejercicio 6.1: ", maxTres(6, 2, 4))
            print("Ejercicio 6.2: ", maxTres(6, 7, 4))

            msvcrt.getch()

        elif opc == 7:
            # Ejercicio 7. Definir la función
            # rota1 : (List[A]) -> List[A]
            # tal que rota1(xs) es la lista obtenida poniendo el primer elemento de
            # xs al final de la lista. Por ejemplo,
            # rota1([3, 2, 5, 7]) == [2, 5, 7, 3]
            # rota1(['a', 'b', 'c']) == ['b', 'c', 'a']
            A = TypeVar('A')
            def rota1(xs: list[A]) -> list[A]:
                if xs == []:
                     return []
                 
                return xs [1:] + [xs [0]]
            
            

            print("Ejercicio 7.1: ", rota1([3, 2, 5, 7]))
            print("Ejercicio 7.2: ", rota1(['a', 'b', 'c']))

            msvcrt.getch()

        elif opc == 8:
            #Ejercicio 8. Definir la función
            # rota : (int, List[A]) -> List[A]
            # tal que rota(n, xs) es la lista obtenida poniendo los n primeros
            # elementos de xs al final de la lista. Por ejemplo,
            # rota(1, [3, 2, 5, 7]) == [2, 5, 7, 3]
            # rota(2, [3, 2, 5, 7]) == [5, 7, 3, 2]
            # rota(3, [3, 2, 5, 7]) == [7, 3, 2, 5]
            A = TypeVar('A')
            def rota(x: int, xs: list[A]) -> list[A]:
                return xs[x:] + xs [:x]

            print("Ejercicio 8.1: ", rota(3, [3, 2, 5, 7]))
            print("Ejercicio 8.2: ", rota(2, [3, 2, 5, 7]))
            print("Ejercicio 8.3: ", rota(1, [3, 2, 5, 7]))
            msvcrt.getch()

        elif opc == 9:
            # Ejercicio 9. Definir la función
            # rango : (List[int]) -> List[int]
            # tal que rango(xs) es la lista formada por el menor y mayor elemento
            # de xs.
            # rango([3, 2, 7, 5]) == [2, 7]
            x = TypeVar('x')
            def rango(xs: list[x]) -> list[x]:
                return [min(xs), max(xs)]
            

            print("Ejercicio 9.1: ", rango([3,2,1,2,6,8,]))
            print("Ejercicio 9.2: ", rango([0.12,0.001,10]))
            print("Ejercicio 9.3: ", rango([3,-2,213]))
            msvcrt.getch()

        elif opc == 10:
            # Ejercicio 10. Definir la función
            # palindromo : (List[A]) -> bool
            # tal que palindromo(xs) se verifica si xs es un palíndromo; es decir,
            # es lo mismo leer xs de izquierda a derecha que de derecha a
            # izquierda. Por ejemplo,
            # palindromo([3, 2, 5, 2, 3]) == True
            # palindromo([3, 2, 5, 6, 2, 3]) == False
            x = TypeVar('x')
            def palindromo(xs: list[x]) -> bool:
                if xs is type(chr):
                    return "Hello Word"
                else:
                    return xs == list(reversed(xs))
            
            print("Ejercicio 10.1: ", palindromo([3, 2, 5, 2, 3]))
            print("Ejercicio 10.2: ", palindromo([3, 2, 5, 6, 2, 3]))
            print("Ejercicio 10.3: ", palindromo(['a', 'b', 'c', 'B', 'A']))
            msvcrt.getch()

        elif opc == 11:
        # Ejercicio 11. Definir la función
        # interior : (list[A]) -> list[A]
        # tal que interior(xs) es la lista obtenida eliminando los extremos de
        # la lista xs. Por ejemplo,
        # interior([2, 5, 3, 7, 3]) == [5, 3, 7]
            A = TypeVar('A')
            def numInteriores(xs: list[A]) -> list[A]:
                return xs[1:][:-1]
            
            print("Ejercicio 11.1: ", numInteriores([1,2,3,4,5]))
            print("Ejercicio 11.2: ", numInteriores([10,12,49,12]))
            print("Ejercicio 11.3: ", numInteriores([0.1]))
            msvcrt.getch()

        elif opc == 12:
            # Definir la función
            # finales : (int, list[A]) -> list[A]
            # tal que finales(n, xs) es la lista formada por los n finales
            # elementos de xs. Por ejemplo,
            # finales(3, [2, 5, 4, 7, 9, 6]) == [7, 9, 6]
            A = TypeVar('A')
            def numFinales(i: int, xs: list[A]):
                    return xs[-i:] if i < len (xs) else xs
            

            print("Ejercicio 12.1: ", numFinales(3, [2, 5, 4, 7, 9, 6]))
            print("Ejercicio 12.2: ", numFinales(6, [2, 5, 4, 7, 9, 6]))
            print("Ejercicio 12.3: ", numFinales(1, [2, 5, 4, 7, 9, 6]))

            msvcrt.getch()

        elif opc == 13:
            # Ejercicio 13. Definir la función
            # segmento : (int, int, list[A]) -> list[A]
            # tal que segmento(m, n, xs) es la lista de los elementos de xs
            # comprendidos entre las posiciones m y n. Por ejemplo,
            # segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]) == [1, 2]
            # segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]) == [1, 2, 7]
            # segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]) == []
            A = TypeVar('A')
            def segmento(i, j, xs: list[A]):
                ys = xs[:j]
                return ys[i-1:]
            
            print("Ejercicio 13.1: ", segmento(3, 4, [3, 4, 1, 2, 7, 9, 0]))
            print("Ejercicio 13.2: ", segmento(3, 5, [3, 4, 1, 2, 7, 9, 0]))
            print("Ejercicio 13.3: ", segmento(5, 3, [3, 4, 1, 2, 7, 9, 0]))
            msvcrt.getch()

        elif opc == 14:
            # Ejercicio 14. Definir la función
            # extremos : (int, list[A]) -> list[A]
            # tal que extremos(n, xs) es la lista formada por los n primeros
            # elementos de xs y los n finales elementos de xs. Por ejemplo,
            # extremos(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3]

            def extremos(i, xs):
                return xs[:i] + xs[-i:]
            
            print(extremos(3,[2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]))
            print(extremos(1,[2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]))
            print(extremos(5,[2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3, 2, 1, 4, 2]))
            msvcrt.getch()
        
        elif opc == 15:
            # Ejercicio 15. Definir la función
            # mediano : (int, int, int) -> int
            # tal que mediano(x, y, z) es el número mediano de los tres números x, y
            # y z. Por ejemplo,
            # mediano(3, 2, 5) == 3
            # mediano(2, 4, 5) == 4
            # mediano(2, 6, 5) == 5
            # mediano(2, 6, 6) == 6

            def mediano(i, j, k):
                return i + j + k - min([i, j, k]) - max([i, j ,k])
                
            print("Ejercicio 15.1: ", mediano(2, 6, 5))
            print("Ejercicio 15.2: ", mediano(2, 4, 5))
            print("Ejercicio 15.3: ", mediano(2, 6, 5))
            print("Ejercicio 15.4: ", mediano(2, 6, 6))
            msvcrt.getch()

        elif opc == 16:
            # Ejercicio 16. Definir la función
            # tresIguales : (int, int, int) -> bool
            # tal que tresIguales(x, y, z) se verifica si los elementos x, y y z son
            # iguales. Por ejemplo,
            # tresIguales(4, 4, 4) == True
            # tresIguales(4, 3, 4) == False
            def treIguales(i, j, k):
                return i == j == k
            
            print("Ejercicio 16.: ", treIguales(4, 4, 4))
            print("Ejercicio 16.: ", treIguales(4, 3, 4))
            print("Ejercicio 16.: ", treIguales(4, 4, 7))
            print("Ejercicio 16.: ", treIguales(1, 4, 3))
            msvcrt.getch()

        elif opc == 17:
            # Ejercicio 17. Definir la función
            # tresDiferentes : (int, int, int) -> bool
            # tal que tresDiferentes(x, y, z) se verifica si los elementos x, y y z
            # son distintos. Por ejemplo,
            # tresDiferentes(3, 5, 2) == True
            # tresDiferentes(3, 5, 3) == False
            def tresDiferentes(i, j, k):
                return i != j and i != k and j != k
            
            print("Ejercicio 17.1 ",tresDiferentes(3, 5, 2))
            print("Ejercicio 17.2 ",tresDiferentes(3, 5, 3))
            print("Ejercicio 17.3 ",tresDiferentes(3, 5, 5))
            print("Ejercicio 17.4 ",tresDiferentes(5, 5, 5))
            print("Ejercicio 17.4 ",tresDiferentes(1, 2, 3))
            msvcrt.getch()
        
        elif opc == 18:
            # Ejercicio 18. Definir la función
            # cuatroIguales : (int, int, int, int) -> bool
            # tal que cuatroIguales(x,y,z,u) se verifica si los elementos x, y, z y
            # u son iguales. Por ejemplo,
            # cuatroIguales(5, 5, 5, 5) == True
            # cuatroIguales(5, 5, 4, 5) == False
            def cuatroIguales(i, j, k, x):
                #return i == j and treIguales(j, k, x)
                return i == j == k == x
            
            print("Ejercicio 18.1: ", cuatroIguales(5, 5, 5, 5))
            print("Ejercicio 18.2: ", cuatroIguales(4, 5, 5, 5))
            print("Ejercicio 18.3: ", cuatroIguales(5, 4, 5, 5))
            print("Ejercicio 18.4: ", cuatroIguales(5, 5, 4, 5))
            print("Ejercicio 18.5: ", cuatroIguales(5, 5, 5, 4))
            print("Ejercicio 18.5: ", cuatroIguales('a', 'a', 'a', 'a'))
            msvcrt.getch()