def esAnagrama(cadena1, cadena2):
    if(sorted(cadena1.lower()) == sorted(cadena2.lower())):print("Es un anagrama :)")
    else: print("No es un anagrama :(")
esAnagrama(input('Introduce una cadena: '), input('Introduce una cadena: '))