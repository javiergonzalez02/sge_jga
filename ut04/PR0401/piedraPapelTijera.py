from random import *

posiblesTiradas = ['piedra', 'papel', 'tijeras', 'lagarto', 'spock']

ganaPiedra = ['lagarto', 'spock', 'tijeras']
ganaPapel = ['spock', 'piedra']
ganaTijeras = ['lagarto', 'papel']
ganaLagarto = ['spock', 'papel']
ganaSpock = ['tijeras', 'piedra']

puntosIA = 0
puntosJugador = 0

while (puntosIA < 5 and puntosJugador < 5):
    indiceAl = randint(0, len(posiblesTiradas)-1)
    tiradaAI = posiblesTiradas[indiceAl]
    tiradaUsuario = input('Escoge una opción (piedra, papel, tijeras, lagarto, spock): ')

    while (tiradaUsuario not in posiblesTiradas):
        tiradaUsuario = input('Opción no válida. Escoge una opción (piedra, papel, tijeras, lagarto, spock): ')
    
    print(tiradaAI)

    if (tiradaUsuario == 'piedra'):
        if (tiradaAI not in ganaPiedra):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1
    
    if (tiradaUsuario == 'papel'):
        if (tiradaAI not in ganaPapel):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    if (tiradaUsuario == 'tijeras'):
        if (tiradaAI not in ganaTijeras):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    if (tiradaUsuario == 'lagarto'):
        if (tiradaAI not in ganaLagarto):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    if (tiradaUsuario == 'spock'):
        if (tiradaAI not in ganaSpock):
            puntosIA = puntosIA + 1
        else:
            puntosJugador = puntosJugador + 1

    print('Puntos IA: ' + str(puntosIA) + ' Puntos Jugador: '+ str(puntosJugador))

if (puntosIA == 5):
    print('Has perdido :(')
else:
    print('Has ganado :)')