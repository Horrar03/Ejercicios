def fibonacci (n):
    i, j = 0, 1
    serie = []
    pares, impares = 0, 0

    while i <= n:
        serie.append(i)
        if i % 2 == 0:
            pares += 1
        else:
            impares += 1
        i, j = j, i + j

    print(f"De los numeros hasta {n}, hay {pares} numeros pares y {impares} numeros impares.")
    print("Serie de fibonacci:", serie)


fibonacci (n = int(input("Escriba un numero mayor a 0 para mostrar su serie fibonacci: ")))
