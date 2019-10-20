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

###exo4

for nombre in range(100):
    print(nombre)

###exo5
for nombre in range(0, 101, 2):
    print(nombre)

###exo6
a = 3
b = 7
c = 15
debit = 10
temps = (a*b*c)/10
print("le temps est de {}".format(temps/10))

###exo7
from math import pi

rayon = float(input("entrer le rayon d un cercle"))


perimetre = 2*pi*rayon
surface = pi*rayon**2
print ("la surface du cercle",round(surface,2))
print ("le perimetre d'un cercle",round(perimetre,2))


###exo8
def triangle (n):
    for i in range (1,n+1,1):
        print(i*"*")
triangle (5)

###exo9

n = int(input("entre nombre"))
for i in range (1, 100):
      n += i
if i%3 == 0 and i%5 ==0 :
    print("FIZZBUZZ")
elif i%3 == 0 :
    print("FIZZ")
elif i%5 == 0 :
    print ("BUZZ")
