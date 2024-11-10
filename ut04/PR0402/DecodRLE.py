def decodificarRLE(cadena):
    resultado = ""
    cont = 0
    for char in cadena:
        if (char.isdigit()):
            resultado += cadena[cont - 1] * int(char)
        cont += 1
    print(resultado)
decodificarRLE(input('Introduce una cadena: '))