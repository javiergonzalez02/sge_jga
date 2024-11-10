def eliminarCharsRepes (cadena):
    nueva = ""
    for i in cadena:
        if (i not in nueva): nueva += i
    print(nueva)
eliminarCharsRepes(input('Introduce una cadena: '))