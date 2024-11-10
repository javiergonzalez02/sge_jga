# 1. Bucle hasta recibir un numero

n = input("Introduce un número válido: ")

while (not n.isdigit()):
    n = input("No has introducido un número válido, inténtalo otra vez: ")

print("Has introducido un numero!")