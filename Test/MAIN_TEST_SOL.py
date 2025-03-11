# Old meg a következő 10 feladatot a feladat leírása alapján
# 30 perced van rá!
# Sok sikert!

# -----------------------------------------------------------------------------------
# Első feladat
# Írd ki a nevedet a kijelzőre!

print("Benedek")

# -----------------------------------------------------------------------------------
# Második feladat
# Mit kell a print statement-be írni hogy a "Szia András!" legyen a kimenet?
# Használd az a és b változókat!
a = "Szia"
b = "András"

print(a,b)
# -----------------------------------------------------------------------------------
# Harmadik feladat
#Egészítsd ki, hogy kiírja a Python a képernyőre a barackot
lista = ['alma', 'körte', 'barack']
print(lista[2]) 

# -----------------------------------------------------------------------------------
# Negyedik feladat
# Add meg egy négyzetszámnak a gyökét
a = 16

print(a**0.5)
# -----------------------------------------------------------------------------------
# Ötödik feladat
#   Valósítsd meg a logikai táblázatot
#

#|        |  a = I |  a = H |
#| b = I  |   I    |   I    |
#| b = H  |   I    |   H    |
#
def Solution(a,b):
    return a or b #Ezt módosítsd

print(str(Solution(True,True)))
# -----------------------------------------------------------------------------------
# Hatodik feladat
#Írj olyan számokat a listába, amivel a print a fenti kommentben lévő eredményt ad.
'''
[4, 9]
[9]
'''
lista = [1,4,9]
for szam in lista:
    del lista[0]
    print(lista)

# -----------------------------------------------------------------------------------
# Hetedik feladat
# Írj egy ciklust ami generálja a következő tömböt:
# [1,1,2,3,5,8,13,21,34,55]
a = 1
b = 1
for i in range(10):
    a,b = b,a+b
    print(a)

# -----------------------------------------------------------------------------------
# Nyolcadik feladat
# Írd ki az "a" változó értékét fordítva a kijelzőre!
a = "Hello World"
print(a[::-1])
# -----------------------------------------------------------------------------------
# Kilencedik feladat
array = [1,5,11,9,4,2,8,3,1,6,6]

length = len(array)

max = array[0]
secondMax = array[0]

for i in range(length):
    if(max < array[i]):
        max = array[i]
    if(secondMax < array[i] and array[i] != max):
        secondMax = array[i]

#Írd át a kódot hogy a második legnagyobbat szám is meglegyen

print( "legnagyobb: " + str(max) + "\nMásodik legnagyobb: " + str(secondMax) )

# -----------------------------------------------------------------------------------
# Tizedik feladat
# Egészítsd ki úgy a kódrészletet, hogy csak a páros, két jegyű számokat 
# írja ki a python a képernyőre!
l = [x for x in range(100)]
res = []
for x in l:
    if x % 2 == 0 and len(str(x)) == 2:
        res.append(x)

print(res)