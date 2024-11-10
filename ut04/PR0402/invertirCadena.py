def invertirCadena (cadena):
    invertida = ""
    for i in cadena:
        invertida = i + invertida
    print(invertida)

invertirCadena(input('Introduce una cadena: '))