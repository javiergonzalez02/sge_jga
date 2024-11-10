from random import *
numero = randint(1,1000)
entrada = int(input('Introduce un numero: '))
while entrada != numero:
    if numero > entrada: entrada = int(input('Introduce un numero más alto: '))
    if numero < entrada: entrada = int(input('Introduce un numero más bajo: '))
if entrada == numero: print('Lo lograste!')