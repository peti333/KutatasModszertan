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
lista = ['alma', 'körte', 'barack']
print(...) #Egészítsd ki, hogy kiírja a Python a képernyőre a barackot

# -----------------------------------------------------------------------------------
# Negyedik feladat
# -----------------------------------------------------------------------------------
# Ötödik feladat
# -----------------------------------------------------------------------------------
# Hatodik feladat
lista = []
for szam in lista:
    del lista[0]
    print(lista)
'''
[4, 9]
[9]
'''
# -----------------------------------------------------------------------------------
# Hetedik feladat
# -----------------------------------------------------------------------------------
# Nyolcadik feladat
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