# 3. Triángulo de asteriscos 

k = input("Introduce k: ")

if (not k.isdigit()):
    print("No has introducido un número")

for i in range(int(k)):
    result = "*"
    for e in range(i):
        result += "*"
    print(result)