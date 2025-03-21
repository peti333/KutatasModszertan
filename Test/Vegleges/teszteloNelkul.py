# Old meg a következő 10 feladatot a feladat leírása alapján
# 30 perced van rá!
# Sok sikert!

# -----------------------------------------------------------------------------------
# Első feladat
# Írd ki a kijelzőre, hogy "Szia Világ!"!

answ_1 = print(...)

# -----------------------------------------------------------------------------------
# Második feladat
# Mit kell a print statement-be írni hogy a "Szia András!" legyen a kimenet?
# Használd az a és b változókat!
a = "Szia"
b = "András"

answ_2 = print(...)
# -----------------------------------------------------------------------------------
# Harmadik feladat
#Egészítsd ki, hogy kiírja a Python a képernyőre a barackot
lista = ['alma', 'körte', 'barack']
answ_3 = print(lista[...]) 
# -----------------------------------------------------------------------------------
# Negyedik feladat
# Add meg egy négyzetszámnak a gyökét
szam = 81
answ_4 = print(...)

# -----------------------------------------------------------------------------------
# Ötödik feladat
#   Valósítsd meg a logikai táblázatot
#

#|        |  a = I |  a = H |
#| b = I  |   I    |   I    |
#| b = H  |   I    |   H    |
#
def Solution(a,b):
    return not a and not b #Ezt módosítsd

print(str(Solution(True,True)))

# -----------------------------------------------------------------------------------
# Hatodik feladat
#Írj olyan számokat a listába, amivel a print a fenti kommentben lévő eredményt ad.
'''
[4, 9]
[9]
'''
test_list = []
lista = []
for _ in lista:
    del lista[0]
    test_list.append(list(lista))

print(test_list)

# -----------------------------------------------------------------------------------
# Hetedik feladat
# Írj egy ciklust ami generálja a következő tömböt:
# [1,1,2,3,5,8,13,21,34,55]
result = []
a = ...
b = ...
for i in range(10):
    result.append(a)
    

print(result)


# -----------------------------------------------------------------------------------
# Nyolcadik feladat
# Írd ki az "a" változó értékét fordítva a kijelzőre!
a = "Hello World"
answ_8 = print(...)

# -----------------------------------------------------------------------------------
# Kilencedik feladatű
# Egészítsd ki a kódot hogy a második legnagyobbat szám is meglegyen
array = [1,5,11,9,4,2,8,3,1,6,6]

length = len(array)

max = array[0]
secondMax = array[0]

for i in range(length):
    if(max < array[i]):
        max = array[i]
    


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