###exercice1 echiquier
noire = "# # # # # # # #"
blanche = ""
print("")
print(" \"")
for i in range(0, 8):
    if i%2 == 0:
        print("   {}{}".format(noire, blanche))
    else:
        print("    {}{}".format(blanche, noire))
print(" \"")
print("")


###exercice2
liste = [0,0,0,0]
a = 0
b = 0
c = 0
d = 0
e = "----------"
for i in range(0, 4):
    liste[i] = 1
    a = liste[0]
    b = liste[1]
    c = liste[2]
    d = liste[3]
    print("{}\n{}\n{}\n{}\n{}".format(a, b, c, d, e))
    liste[i] = 0


#####exercice3

a = int(input("entrer un nombre"))
if a%2 == 0 :
    print (bool(a))
else:
    a %2 != 0
    print("false")


####exercice4
while True:
    try:
        N = int(input("saisir un nombre entier positf"))
        if N >0 :
            ft=1
            for i in range(2, N+1 ):
                ft*=i
            print(N, ft)
            break
    except ValueError:
        continue
    print (N)


####exercice5

def remplace_tirets_par_des_underscores(user):
    return user.replace('-', '_')
print(remplace_tirets_par_des_underscores(input("salam alikoum entrez quelque chose: ")))


#####exercice6

liste = ["tomate", "salade", "oignons", "mais", "fromages"]
print("acheter les",liste[0],"en premier")
print("acheter les",liste[-1],"en deuxième")
print(liste[2])


#####exercice7

liste1 = [["hammiche", "kamel", "47", "1972"], ["macron", "emmanuelle", "42", "1977"]]

def information(liste1):
    for i in range(len(liste1)):
        for j in range(len(liste1[i])):

            print(liste1[i][j])

information(liste1)


####exercice8

liste = [14, 78, 417, 59, 36]
print(max(liste))







####exercice9


words = " "
taches = list()
while words != "fin":
    taches.append(words)
    words =input("entrer taches a realiser")
taches.pop(0)
print(taches)



#### exercice7 pour aller plus loin



liste = [['horlein', 'bruno', 40, 1979],  ['gossart', 'thomas', 29, 1981], ['hammiche', 'camelia', 5, 2014],  ['hammiche', 'lila', 7, 2012]]
def tableau(liste):
    for i in range (len(liste)):
        for j in range(len(liste[i])):
            print(liste[i] [j])
tableau(liste)























































######exercice9
