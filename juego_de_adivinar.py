import random

guessesTaken = 0
minNumero = 0
maxNumero = 20

print('hola! cual es tu nombre?: ')
username = input()

number = random.randint(minNumero, maxNumero)
print('bueno, ' + username + '. Estoy pensando en un numero entre ' + str(minNumero) + ' y ' + str(maxNumero))

#Este es un bucle del juego que ejecuta 
while guessesTaken < 6:
    print('adivina el numero: ')
    guess = input()
    guess = int(guess)

    guessesTaken = guessesTaken + 1

    if guess < number:
        print('el numero es demasiado bajo.')
    if guess > number:
        print('El numero es demasiado alto.')
    if guess == number:
        break
 
if guess == number:
    guessesTaken = str(guessesTaken)
    print('Felicicidades!!. ' + username + '! acertaste el numero en ' +  guessesTaken  + ' intentos!!')

