# függvények, újra használható kód

def plus(a, b):
    return a + b


print(plus(1, 2))
print(plus(6, -2))

# konkrét függvény, legnagyobb elem kiválasztása
lista = [3, 65, -1, 10, 1]

def maximumKivalasztas(listaParameter):
    eddigiLegnagyobb = listaParameter[0]
    for i in listaParameter:
        if i > eddigiLegnagyobb:
            eddigiLegnagyobb = i

    return eddigiLegnagyobb

print('maximum: ', maximumKivalasztas(lista))