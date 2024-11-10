```python
# EJERCICIOS CON DICCIONARIOS
```


```python
# 1. BUSCAR VALOR EN UN DICCIONARIO
```


```python
frutas = {"manzana": 10, "banana": 20, "pera":4, "uva": 18, "naranja": 12}
fruta = input("Introduce una fruta: ")
if fruta in frutas:
    print(f"El precio es {frutas.get(fruta)}")
else: print("No existe esa fruta")
```


```python
# 2. CONTAR ELEMENTOS EN UN DICCIONARIO
```


```python
productos = {
    "Electrónica": ["Smartphone", "Laptop", "Tablet", "Auriculares", "Smartwatch"],
    "Hogar": ["Aspiradora", "Microondas", "Lámpara", "Sofá", "Cafetera"],
    "Ropa": ["Camisa", "Pantalones", "Chaqueta", "Zapatos", "Bufanda"],
    "Deportes": ["Pelota de fútbol", "Raqueta de tenis", "Bicicleta", "Pesas", "Cuerda de saltar"],
    "Juguetes": ["Muñeca", "Bloques de construcción", "Peluche", "Rompecabezas", "Coche de juguete"],
}

print(f"Hay {len(productos)} categorías")

contadorProductosTot = 0

for categoria in productos:
    contadorProductosCat = 0
    for prod in categoria:
        contadorProductosTot += 1
        contadorProductosCat += 1
    print(f"La categoria {categoria} tiene {contadorProductosCat} productos")

print(f"Hay {contadorProductosTot} productos en total")

```


```python
# 3. CONTADOR DE FRECUENCIAS DE PALABRAS
```


```python
frase = "El get() método de un diccionario de Python devuelve el valor de una clave especificada si la clave está en el diccionario."

dict = {}

for palabra in frase.split():
    if palabra not in dict:
        dict[palabra] = 1
    else:
        dict[palabra] += 1
print(dict)
```


```python
# 4. DICCIONARIO DE LISTAS
```


```python
asignaturas = {
    "Matemáticas": ["Ana", "Carlos", "Luis", "María", "Jorge"],
    "Física": ["Elena", "Luis", "Juan", "Sofía"],
    "Programación": ["Ana", "Carlos", "Sofía", "Jorge", "Pedro"],
    "Historia": ["María", "Juan", "Elena", "Ana"],
    "Inglés": ["Carlos", "Sofía", "Jorge", "María"],
}
print("Opción 1: Listar estudiantes matriculados en una asignatura, Opción 2: Matricular un estudiante en una asignatura y Opción 3: Dar de baja un estudiante de una asignatura.")
opcion = input("Introduce una opción (1,2,3): ")
if not opcion.isdigit(): 
    print("Opción no válida")
    exit()
asig = input("Introduce una asignatura: ")
if asig not in asignaturas: 
    print("Asignatura no existe")
    exit()
if opcion == 1:
    for (i in asignaturas.get)
    
```


```python
# 5. DICCIONARIO INVERTIDO
```


```python
def invertir_diccionario(diccionario):
    diccionario_invertido = {valor: clave for clave, valor in diccionario.items()}
    return diccionario_invertido
print(invertir_diccionario({'a': 1, 'b': 2, 'c': 3}))
```


```python
# 6. COMBINAR DOS DICCIONARIOS
```


```python
def combinar_diccionarios(prod1, prod2):
    combinado = prod1.copy()
    for producto, precio in prod2.items():
        if producto in combinado:
            combinado[producto] += precio
        else:
            combinado[producto] = precio
    return combinado
productos1 = {'Manzana': 1.20, 'Banana': 0.50, 'Naranja': 0.80}
productos2 = {'Banana': 0.70, 'Pera': 1.00, 'Manzana': 1.30}
print(combinar_diccionarios(productos1, productos2))
```


```python

```
