def invertirCadena (cadena):
    invertida = ""
    for i in cadena:
        invertida = i + invertida
    return invertida

def verificarPalindromo (cadena):
    if (cadena == invertirCadena(cadena)):
        print('Es palíndromo :)')
    else:
        print('No es palíndromo :(')

verificarPalindromo(input('Introduce una cadena: '))