# 4. Pirámide de asteriscos

p = input("Introduce un número impar: ")

while ((int(p) % 2 == 0)):
    p = input("No has introducido un número impar, inténtalo otra vez: ")

for i in range(1,int(p)+1,2):
    espacios = ((int(p) - i )/ 2)
    print(int(espacios) * " " + "*" * i)