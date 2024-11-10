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