# 2. Tabla de Multiplicar 

n = int(input("Introduce n: "))

k = int(input("Introduce k: "))

for i in range(int(k)):
    result = n * i
    print(f"{n} * {i} = {result}")