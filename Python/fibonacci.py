#
#Escribe un programa que imprima los 50 primeros números de la sucesión
#de Fibonacci empezando en 0.
#- La serie Fibonacci se compone por una sucesión de números en
#  la que el siguiente siempre es la suma de los dos anteriores.
#  0, 1, 1, 2, 3, 5, 8, 13...
#
def fibonacci (n, temp_i = None):
    
    i = 0
    fib = 1
    serie = []

    while i <= n:
        if temp_i:
            temp_i(i)
        print(i)
        i, fib  = fib, i + fib
        serie.append(i)
        

    return serie
    
    #i, j = 0, 1
    #cont = 0
#
    #while i <= n:
    #    print (i)
    #    i, j =j,  i + j
    #    cont +=1
    #    print(cont)

# fibonacci(50)
# fibonacci(n = int(input("Escriba un numero para su serie de Fibonacci: ")))


#def fibonacci():
#
#    fib = 0
#    i = 0
#
#    while True:
#        fib = fib + i
#        if (fib >= 50):
#            return fibonacci
#        else:
#            i=+1
#            return print(fib)
#        
#fibonacci()
#i = 0
#j = []
#fib = 0
#while i <= 50:
#    if fib >= 50:
#        break
#    else:
#        fib = j[i] + j[i-1] 
#        i = fib
#        print(fib)