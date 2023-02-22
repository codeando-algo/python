import time
import os

print("ingrese un numero para el contador")
numero=int(input())
for i in range(numero):
    print(numero)
    time.sleep(1)
    os.system("cls")
    numero-=1
    if (numero==0):
        print(numero)
        print("tucson")
        input("presine ENTER para cerrar..")
