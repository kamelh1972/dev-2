###exo1
a = 19
b = 89
c = 38
d = 40
if a > b and a > c and a > d :
    print(a)
elif b > a and b > c and b > d :
    print(b)
elif c > a and c > b and c > d :
    print(c)
else :
    print(d)

###exo2
import math
age = int(input("tapez votre age"))
if age >= 21:
    print("acces autorise")
if age%2 == 0 :
    print("pair")
if age < 0 :
    print("prout")
else:
    print("impair")
if int(math.sqrt(age)) == math.sqrt(age):
    print("votre age est un carre")
else:
    print("vous n'avez rien taper")

import random
nombre = 18
nombre_1 = int(input("entrer un nombre"))

if nombre == nombre_1:
    print("oulou")
elif nombre != nombre_1:
    print("heey non hahahaha")

    
