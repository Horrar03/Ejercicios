"""def prueba(i, xs):
    return xs[:i]+xs[-i:]

#print(prueba(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]))
print(prueba(3, [2, 6, 7, 1, 2, 4, 5, 8, 9, 2, 3]) == [2, 6, 7, 9, 2, 3])
"""

def contador(i = 1):
    if i > 100:
        return
    print(i)
    contador(i+1)

contador()