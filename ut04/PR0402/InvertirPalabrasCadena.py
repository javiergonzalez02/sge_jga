def invertirCadena (cadena):
    invertida = ""
    for i in cadena.split(" "): invertida = i + " " + invertida
    print(invertida)

invertirCadena(input('Introduce una cadena: '))