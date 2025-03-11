# Old meg a következő 10 feladatot a feladat leírása alapján
# 30 perced van rá!
# Sok sikert!

# -----------------------------------------------------------------------------------
# Első feladat
# Írd ki a nevedet a kijelzőre!

print(...)

# -----------------------------------------------------------------------------------
# Második feladat
# Mit kell a print statement-be írni hogy a "Szia András!" legyen a kimenet?
# Használd az a és b változókat!
a = "Szia"
b = "András"

print()
# -----------------------------------------------------------------------------------
# Harmadik feladat
#Egészítsd ki, hogy kiírja a Python a képernyőre a barackot
lista = ['alma', 'körte', 'barack']
print(...) 

# -----------------------------------------------------------------------------------
# Negyedik feladat
# -----------------------------------------------------------------------------------
# Ötödik feladat
#   Valósítsd meg a logikai táblázatot
#

#|      |  a I |  a H |
#| b I  |   I  |   I  |
#| b H  |   I  |   H  |
#
def Solution(a,b):
    return not a and b #Ezt módosítsd

print(str(Solution(True,True)))
# -----------------------------------------------------------------------------------
# Hatodik feladat
#Írj olyan számokat a listába, amivel a print a fenti kommentben lévő eredményt ad.
'''
[4, 9]
[9]
'''
lista = []
for szam in lista:
    del lista[0]
    print(lista)

# -----------------------------------------------------------------------------------
# Hetedik feladat
# Írj egy ciklust ami generálja a következő tömböt:
# [1,1,2,3,5,8,13,21,34,55]
# -----------------------------------------------------------------------------------
# Nyolcadik feladat
# Írd ki az "a" változó értékét fordítva a kijelzőre!
a = "Hello World"
print(...)
# -----------------------------------------------------------------------------------
# Kilencedik feladat
array = [1,5,11,9,4,2,8,3,1,6,6]

length = len(array)

max = array[0]
secondMax = array[0]

for i in range(length):
    if(max < array[i]):
        max = array[i]

#Írd át a kódot hogy a második legnagyobbat szám is meglegyen

print( "legnagyobb: " + str(max) + "\nMásodik legnagyobb: " + str(secondMax) )

# -----------------------------------------------------------------------------------
# Tizedik feladat
# Egészítsd ki úgy a kódrészletet, hogy csak a páros, két jegyű számokat 
# írja ki a python a képernyőre!
l = [x for x in range(100)]
res = []
for x in l:
    if ...:
        res.append(x)

print(res)