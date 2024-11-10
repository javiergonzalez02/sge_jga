def mayusMinus(cadena):
    nueva = ""
    for i in cadena:
        if (i.islower()):
            nueva += i.upper()
        else:
            nueva += i.lower()
    print(nueva)

mayusMinus(input('Introduce una cadena: '))