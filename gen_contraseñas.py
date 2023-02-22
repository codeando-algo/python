import random
from werkzeug.security import generate_password_hash

minus = 'abcdefghijklmnopqrstuvwxyz'
mayus = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numeros = '0123456789'

base = minus+mayus+numeros
longitud = 12

for _ in range(10):
    muestra = random.sample(base,longitud)
    contraseña =''.join(muestra)
    contraseña_encriptada = generate_password_hash(contraseña)
    print("{} => {}".format(contraseña,contraseña_encriptada))

