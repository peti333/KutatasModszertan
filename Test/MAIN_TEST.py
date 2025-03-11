import builtins
from colored import Fore, Back, Style

old_print = builtins.print

def print_new(string):
    old_print(string)
    return string

builtins.print = print_new
#___________________________________________________________________________________

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

answ_2 = print()
# -----------------------------------------------------------------------------------
# Harmadik feladat
#Egészítsd ki, hogy kiírja a Python a képernyőre a barackot
lista = ['alma', 'körte', 'barack']
answ_3 = print(...) 
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
    return not a and b #Ezt módosítsd

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
for szam in lista:
    del lista[0]
    test_list.append(print(lista))

# -----------------------------------------------------------------------------------
# Hetedik feladat
# Írj egy ciklust ami generálja a következő tömböt:
# [1,1,2,3,5,8,13,21,34,55]
result = []


# -----------------------------------------------------------------------------------
# Nyolcadik feladat
# Írd ki az "a" változó értékét fordítva a kijelzőre!
a = "Hello World"
answ_8 = print(...)

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


#Testing
#------------------------------------------------------------------------------------
try:
    assert answ_1 == "Szia Világ!"
    old_print(f'{Fore.white}{Back.green}Első feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Első feladat: Helyetelen!{Style.reset}')

try:
    assert answ_2 == "Szia Világ!"
    old_print(f'{Fore.white}{Back.green}Második feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Második feladat: Helyetelen!{Style.reset}')

try:
    assert answ_3 == "barack"
    old_print(f'{Fore.white}{Back.green}Harmadik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Harmadik feladat: Helyetelen!{Style.reset}')

try:
    assert (answ_4**(0.5)) == (szam**(0.5))
    old_print(f'{Fore.white}{Back.green}Negyedik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Negyedik feladat: Helyetelen!{Style.reset}')

try:
    assert Solution(True, True) == True
    assert Solution(True, False) == True
    assert Solution(False, True) == True
    assert Solution(False, False) == False
    old_print(f'{Fore.white}{Back.green}Ötödik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Ötödik feladat: Helyetelen!{Style.reset}')

try:
    assert test_list[0] == "[4,9]"
    assert test_list[1] == "[9]"
    old_print(f'{Fore.white}{Back.green}Hatodik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Hatodik feladat: Helyetelen!{Style.reset}')

try:
    assert result == [1,1,2,3,5,8,13,21,34,55]
    old_print(f'{Fore.white}{Back.green}Hetedik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Hetedik feladat: Helyetelen!{Style.reset}')

try:
    assert answ_8 == a[::-1]
    old_print(f'{Fore.white}{Back.green}Nyolcadik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Nyolcadik feladat: Helyetelen!{Style.reset}')

try:
    assert secondMax == "9"
    old_print(f'{Fore.white}{Back.green}Kilencedik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Kilencedik feladat: Helyetelen!{Style.reset}')

try:
    assert res == [x for x in range(2,100,2) if len(str(x)) == 2]
    old_print(f'{Fore.white}{Back.green}Tizedik feladat: Helyes!{Style.reset}')
except AssertionError:
    old_print(f'{Fore.white}{Back.red}Tizedik feladat: Helyetelen!{Style.reset}')
