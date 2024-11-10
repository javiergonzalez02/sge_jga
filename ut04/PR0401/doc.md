```python
# PR0401 - EJERCICIOS BÁSICOS EN PYTON
```


```python
# 1. LECTURA DE UN NÚMERO VÁLIDO

n = input("Introduce un número válido: ")

while (not n.isdigit()):
    n = input("No has introducido un número válido, inténtalo otra vez: ")

print("Has introducido un numero!")
```


```python
# 2. TABLA DE MULTIPLICAR

n = int(input("Introduce n: "))

k = int(input("Introduce k: "))

for i in range(int(k)):
    result = n * i
    print(f"{n} * {i} = {result}")
```


```python
# 3. TRIÁNGULO DE ASTERÍSCOS

k = input("Introduce k: ")

if (not k.isdigit()):
    print("No has introducido un número")

for i in range(int(k)):
    result = "*"
    for e in range(i):
        result += "*"
    print(result)
```


```python
# 4. PIRÁMIDE DE ASTERÍSCOS

p = input("Introduce un número impar: ")

while ((int(p) % 2 == 0)):
    p = input("No has introducido un número impar, inténtalo otra vez: ")

for i in range(1,int(p)+1,2):
    espacios = ((int(p) - i )/ 2)
    print(int(espacios) * " " + "*" * i)
```


```python
# 5. NÚMERO MAYOR Y MENOR

numMenor, numMayor = 0, 0

for i in range (5):
    n = int(input("Introduce un numero: "))
    if i == 0: numMenor = n 
    if i == 0: numMayor = n 

    if (n > numMayor): numMayor = n 
    if (n < numMenor): numMenor = n

print(f"El número mayor es {numMayor} y el menor es {numMenor}")
```


```python
# 6. CONVERSIÓN DE UNIDADES

posiblesUds = ['mm','cm','m','km']

cantidad = int(input('Introduce la cantidad: '))
unidadOr = input('Introduce la unidad de origen: ')
unidadDest = input('Introduce la unidad de destino: ')

if ((unidadOr in posiblesUds) & (unidadDest in posiblesUds)):
    if(unidadOr == 'mm'):
        if(unidadDest == 'cm'):
            cantidad = cantidad * 0.1 
        if(unidadDest == 'm'):
            cantidad = cantidad * 0.001
        if(unidadDest == 'km'):
            cantidad = cantidad * 0.000001
    if(unidadOr == 'cm'):
        if(unidadDest == 'mm'):
            cantidad = cantidad * 10 
        if(unidadDest == 'm'):
            cantidad = cantidad * 0.01
        if(unidadDest == 'km'):
            cantidad = cantidad * 0.00001
    if(unidadOr == 'm'):
        if(unidadDest == 'mm'):
            cantidad = cantidad * 1000 
        if(unidadDest == 'cm'):
            cantidad = cantidad * 100
        if(unidadDest == 'km'):
            cantidad = cantidad * 0.0001
    if(unidadOr == 'km'):
        if(unidadDest == 'mm'):
            cantidad = cantidad * 1000000 
        if(unidadDest == 'cm'):
            cantidad = cantidad * 100000
        if(unidadDest == 'm'):
            cantidad = cantidad * 1000
    print(cantidad)
else:
    print('No has introducido una unidad válida')
```


```python
# 7. ACIERTA EL NÚMERO

from random import *
numero = randint(1,1000)
entrada = int(input('Introduce un numero: '))
while entrada != numero:
    if numero > entrada: entrada = int(input('Introduce un numero más alto: '))
    if numero < entrada: entrada = int(input('Introduce un numero más bajo: '))
if entrada == numero: print('Lo lograste!')
```


```python
# 8. PIEDRA, PAPEL O TIJERA

from random import *

posiblesTiradas = ['piedra', 'papel', 'tijeras', 'lagarto', 'spock']

ganaPiedra = ['lagarto', 'spock', 'tijeras']
ganaPapel = ['spock', 'piedra']
ganaTijeras = ['lagarto', 'papel']
ganaLagarto = ['spock', 'papel']
ganaSpock = ['tijeras', 'piedra']

puntosIA = 0
puntosJugador = 0

while (puntosIA < 5 and puntosJugador < 5):
    indiceAl = randint(0, len(posiblesTiradas)-1)
    tiradaAI = posiblesTiradas[indiceAl]
    tiradaUsuario = input('Escoge una opción (piedra, papel, tijeras, lagarto, spock): ')

    while (tiradaUsuario not in posiblesTiradas):
        tiradaUsuario = input('Opción no válida. Escoge una opción (piedra, papel, tijeras, lagarto, spock): ')
    
    print(tiradaAI)

    if (tiradaUsuario == 'piedra'):
        if (tiradaAI not in ganaPiedra):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1
    
    if (tiradaUsuario == 'papel'):
        if (tiradaAI not in ganaPapel):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    if (tiradaUsuario == 'tijeras'):
        if (tiradaAI not in ganaTijeras):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    if (tiradaUsuario == 'lagarto'):
        if (tiradaAI not in ganaLagarto):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    if (tiradaUsuario == 'spock'):
        if (tiradaAI not in ganaSpock):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    print('Puntos IA: ' + str(puntosIA) + ' Puntos Jugador: '+ str(puntosJugador))

if (puntosIA == 5):
    print('Has perdido :(')
else:
    print('Has ganado :)')
```


```python
# 9. SECUENCIA DE FIBONACCI

def generar_fibonacci(n):
    if n <= 0:
        return []
    fib = [1, 1]
    while len(fib) < n:
        fib.append(fib[-2] + fib[-1])
    return fib[:n]
    
print(generar_fibonacci(int(input("Ingrese el número de elementos de Fibonacci: "))))
```
