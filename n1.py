import random
while(True):
    print ('piedra, papel o tijera?')
    cadena=raw_input()
    n=int(random.randrange(2))
    #creando el valor de la pc
    if n==0:
        cadena2='piedra'
    elif n==1:
        cadena2='tijera'
    else:
        cadena3='papel'
    print 'La pc elige %s '%cadena2
    #comparando valor de la pc con el usuario
    if cadena == 'piedra' and cadena2=='tijera':
        print "El ganador es usted"
    elif cadena == 'papel' and cadena2=='piedra':
        print "El ganador es usted"
    elif cadena == 'tijera' and cadena2=='papel':
        print "El ganador es usted"
    if cadena == 'piedra' and cadena2=='piedra':
        print "Empate"
    elif cadena == 'papel' and cadena2=='papel':
        print "Empate"
    elif cadena == 'tijera' and cadena2=='tijera':
        print "Empate"
    else:
        print "La computadora gano"
    print ('********************************')

