```python
# PRO405: EJERCICIOS DE PROGRAMACIÓN FUNCIONAL
```


```python
# 1. FILTRADO DE UNA LISTA DE NÚMEROS

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def esPar(x):
    if (x % 2) == 0: return True
    else: return False

pares = filter(esPar, numeros)

for x in pares:
    print(x)
```


```python
# 2. MAPEO DE TEMPERATURAS

celsius = [0, 20, 37, 100]

def celsiusAFahrenheit(x):
   return x*9/5+32

print(list(map(celsiusAFahrenheit, celsius)))
```


```python
# 3. SUMA ACUMULATIVA

import functools

numeros = [1, 2, 3, 4, 5]

print(functools.reduce(lambda a, b: a+b, numeros))
```


```python
# 4. PALABRAS CON CIERTA LONGITUD

palabras = ["perro", "gato", "elefante", "oso", "jirafa"]

def esMayorCinco(x):
    if len(x) > 5: return True
    else: return False

mayorCinco = filter(esMayorCinco, palabras)

def mayusculas(x):
   return x.upper()

print(list(map(mayusculas, mayorCinco)))
```


```python
# 5. MULTIPLICACIÓN DE PARES

from functools import reduce

numeros = [1, 2, 3, 4, 5, 6]

pares = list(filter(lambda x: x % 2 == 0, numeros))

mapeados = map(lambda x: x, pares) 

suma = reduce(lambda x, y: x * y, mapeados, 1)

print(suma)
```


```python
# 6. COMBINAR OPERACIONES EN LISTAS ANIDADAS

from functools import reduce

numeros = [[-3, 2, 7], [10, -5, 3], [0, 8, -2]]

listaReducida = reduce(lambda acc, sublista: acc + sublista, numeros, [])

positivos = filter(lambda x: x > 0, listaReducida)

sumaPositivos = reduce(lambda a, b: a + b, positivos, 0)

print(sumaPositivos) 
```
