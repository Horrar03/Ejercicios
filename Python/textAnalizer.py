import os
os.system('cls')
def textAnalizer(texto):
    letras, palabras, espacios = 0, 1, 0
    for i in texto:
        if i != ' ':
            letras +=1
        else:
            espacios += 1
            palabras += 1
    print(f"El texto tiene {letras} caracteres."\
          f"\nTiene {espacios} espacios" \
          f"\nY {palabras} palabras")

textAnalizer(input("Escribe un texto que quieras analizar: "))
