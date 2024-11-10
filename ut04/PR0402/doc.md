```python
# PR0402 - EJERCICIOS DE CADENAS EN PYTON
```


```python
# 1. CONTAR VOCALES Y CONSONANTES

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
```

```python
# 2. INVERTIR CADENA

def invertirCadena (cadena):
    invertida = ""
    for i in cadena:
        invertida = i + invertida
    print(invertida)

invertirCadena(input('Introduce una cadena: '))
```

```python
# 3. VERIFICAR PALÍNDROMO

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
```

```python
# 4. CONTAR PALABRAS

def contarPalabras(cadena): print('La cadena tiene '+ str(len(cadena.split())) + ' palabras')
contarPalabras(input('Introduce una cadena: '))
```

```python
# 5. ELIMINAR CARACTERES REPETIDOS

def eliminarCharsRepes (cadena):
    nueva = ""
    for i in cadena:
        if (i not in nueva): nueva += i
    print(nueva)
eliminarCharsRepes(input('Introduce una cadena: '))
```

```python
# 6. MAYÚSCULAS Y MINÚSCULAS

def mayusMinus(cadena):
    nueva = ""
    for i in cadena:
        if (i.islower()):
            nueva += i.upper()
        else:
            nueva += i.lower()
    print(nueva)

mayusMinus(input('Introduce una cadena: '))
```

```python
# 7. INVERTIR PALABRAS DE UNA CADENA

def invertirCadena (cadena):
    invertida = ""
    for i in cadena.split(" "): invertida = i + " " + invertida
    print(invertida)

invertirCadena(input('Introduce una cadena: '))
```

```python
# 8. ANAGRAMA

def esAnagrama(cadena1, cadena2):
    if(sorted(cadena1.lower()) == sorted(cadena2.lower())):print("Es un anagrama :)")
    else: print("No es un anagrama :(")
esAnagrama(input('Introduce una cadena: '), input('Introduce una cadena: '))
```

```python
# 9. FRECUENCIA CARACTERES

def frecuenciaChars (cadena):
    diccionario = {}
    for i in cadena:
        if i in diccionario:
            diccionario[i] += 1
        else:
            diccionario[i] = 1
    print(diccionario)


frecuenciaChars(input('Introduce una cadena: '))
```

```python
# 10. QUITAR CARACTERES NO ALFANUMÉRICOS

def quitarNoAlfanumericos(cadena):
    resultado = ""
    for i in cadena:
        if (i.isalnum()): resultado += i
    print(resultado)

quitarNoAlfanumericos(input('Introduce una cadena: '))
```

```python
# 11. TRANSFORMAR CAMELCASE

def transformarACamel(cadena):
    resultado, upper = "", False
    for i in cadena:
        if (i == "-"):
            upper = True
            continue
        if (upper == True and resultado != ""):
            resultado += i.upper()
            upper = False
            continue
        resultado += i.lower()
    print(resultado)
transformarACamel(input('Introduce una cadena: '))
```

```python
# 12. CODIFICACION RLE (RUN LENGTH ENCODING)

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
```

```python
# 13. DECODIFICACION RLE (RUN LENGTH DECODING)

def decodificarRLE(cadena):
    resultado = ""
    cont = 0
    for char in cadena:
        if (char.isdigit()):
            resultado += cadena[cont - 1] * int(char)
        cont += 1
    print(resultado)
decodificarRLE(input('Introduce una cadena: '))
```

```python
# 14. FORMATEO DE CADENAS CON PLANTILLAS

def formateoPlantilla(cadena, diccionario):
    indexInicio = cadena.find('{')
    clave = diccionario.keys()[0]
    if indexInicio != -1 :
        indexFinal = cadena.find('}')
        palabra = cadena[indexInicio+1:indexFinal]
        print(cadena.replace(palabra, diccionario.values()))

formateoPlantilla(input('Introduce una cadena: '), input('Introduce una cadena: '))
```

```python
# 15. COMPARAR CADENAS POR VALOR ASCII

def contarAscii(cadena):
    return sum([ord(char) for char in cadena])

def compararAscii(cadena1, cadena2):
    if contarAscii(cadena1) > contarAscii(cadena2):
        return cadena1 + ' tiene un valor ascii mayor: ' + str(contarAscii(cadena1)) + ' que ' + cadena2 + ', la cual tiene el siguiente valor ' + str(contarAscii(cadena2))
    else:
        return cadena2 + ' tiene un valor ascii mayor: ' + str(contarAscii(cadena2)) + ' que ' + cadena1 + ', la cual tiene el siguiente valor ' + str(contarAscii(cadena1))
print(compararAscii(input('Introduce una cadena: '), input('Introduce una cadena: ')))
```

```python
# 16. CONTAR LONGITUD DE PALABRA MÁS LARGA

def palabraMasLarga(cadena):
    arr = cadena.split(" ")
    palabraMasLarga = arr[0]
    longitudCadena = len(arr[0])
    for i in arr:
        if len(i)> longitudCadena: 
            longitudCadena = len(i)
            palabraMasLarga = i
    return 'La palabra más larga es ' + palabraMasLarga
print(palabraMasLarga(input('Introduce una cadena: ')))
```

```python
# 17. FORMATEAR NÚMERO CON SEPARADOR DE MILES

def formatearMiles (cadena):
    if cadena.isdigit():
        num = int(cadena)
        if num % 3 == 2:
            
formatearMiles(input('Introduce un numero: '))
```

```python
# 18. ROTAR CARACTERES DE UNA CADENA

def invertirCaracteres (cadena):
    invertida = ""
    for i in cadena:
        invertida = i + invertida
    print(invertida)

invertirCaracteres(input('Introduce una cadena: '))
```
