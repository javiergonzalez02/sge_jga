numMenor, numMayor = 0, 0

for i in range (5):
    n = int(input("Introduce un numero: "))
    if i == 0: numMenor = n 
    if i == 0: numMayor = n 

    if (n > numMayor): numMayor = n 
    if (n < numMenor): numMenor = n

print(f"El número mayor es {numMayor} y el menor es {numMenor}")