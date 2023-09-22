# carre parfait:
import math 
def carrer_parfait(nombre):
    if nombre <0:
        return False
    racine=math.isqrt(nombre)
    return racine*racine == nombre

nombre=int(input("entre un nombre"))
if carrer_parfait(nombre):
    print(nombre,"carre parfait")
else:
    print(nombre,"pas parfait")

carrer_parfait(12)