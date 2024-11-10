def codificarRLE(cadena):
    resultado, cont, charRepetido = "", 0, ""
    for i in cadena:
        if (i == charRepetido):
            cont += 1
            resultado = resultado[:-1] + str(cont)
            continue
        if (i != charRepetido):
            cont, charRepetido = 1, i
            resultado += i + str(cont)
            continue
        resultado += i.lower()
    print(resultado)
codificarRLE(input('Introduce una cadena: '))