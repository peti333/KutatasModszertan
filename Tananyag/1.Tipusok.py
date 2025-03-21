# Típusok & változók
szam = 5
szo = "asd"
igazVagyHamis = True

# print, képernyőre iratás
print(szam)
print(szo)
print(igazVagyHamis)
print(4 == 5)

a = 4
b = 5
print(a + b)

# listák
lista = [1,2,3,5,7]
lista2 = ["Hello", "World", "!"]

# indexelés
print(lista[0])
print(lista2[1])
print(lista2[-1])

#listahoz adás
lista.append(100)
print(lista)

#törlés

del lista[0]
print(lista)

lista3 = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]

print(lista3[1:8:2])

# lista3[honnan:hova:lépésköz]
nagylista = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19]
print("Lista = " + str(nagylista))
print("Második indextől = " + str(nagylista[2:]))
print("Negyedik indexig" + str(nagylista[:4]))
print("Második indextől negyedik indexig = " + str(nagylista[2:4]))
print("2 indexenként" + str(nagylista[::2]))
print("Első indextől tizedik index 2 indexenként" + str(nagylista[1:10:2]))


# Lista generátor
huszlista = [x for x in range(20)]
print("Lista 0-19 ig: " + str(huszlista))
negyvenlista = [x for x in range(40)]
print("Lista 0-39g ig: " + str(negyvenlista))
hatvanHaromLista = [x for x in range(63)]
print("Lista 0-62 ig:" + str(hatvanHaromLista))