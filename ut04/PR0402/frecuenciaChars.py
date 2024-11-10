def frecuenciaChars (cadena):
    diccionario = {}
    for i in cadena:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    print(diccionario)


frecuenciaChars(input('Introduce una cadena: '))