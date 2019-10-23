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
