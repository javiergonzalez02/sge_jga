def contarVocalesConsonantes (cadena):
    numVocales = 0
    numConsonantes = 0

    vocales = 'aeiou'
    consonantes = 'bdfghjklmnñpqrstvwxyz'

    for i in cadena.lower():
        if (i in vocales):
            numVocales = numVocales + 1
        elif (i in consonantes):
            numConsonantes = numConsonantes + 1
    
    print ('La cadena contiene ' + str(numVocales) + ' vocales y ' + str(numConsonantes) + ' consonantes.')

contarVocalesConsonantes(input('Introduce una cadena: '))