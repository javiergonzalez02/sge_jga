def formateoPlantilla(cadena, diccionario):
    indexInicio = cadena.find('{')
    clave = diccionario.keys()[0]
    if indexInicio != -1 :
        indexFinal = cadena.find('}')
        palabra = cadena[indexInicio+1:indexFinal]
        print(cadena.replace(palabra, diccionario.values()))

formateoPlantilla(input('Introduce una cadena: '), input('Introduce una cadena: '))