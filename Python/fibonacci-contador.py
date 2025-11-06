from fibonacci import fibonacci
from watcher import temp

n = int(input("Escriba un numero positivo para su serie de Fibonacci: "))
fibonacci(n, temp_i = temp)
pares, impares = 0, 0

if temp % 2 == 0:
    pares += 1
elif temp % 2 != 0:
    impares += 1

print(f"De los numeros hasta {n}, hay {pares} numeros pares y {impares} numeros impares.")