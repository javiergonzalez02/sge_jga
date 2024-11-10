def quitarNoAlfanumericos(cadena):
    resultado = ""
    for i in cadena:
        if (i.isalnum()): resultado += i
    print(resultado)

quitarNoAlfanumericos(input('Introduce una cadena: '))