from random import randint, shuffle


def generateNewValue2(lim1, lim2):
    return randint(lim1, lim2)

def firstGen(nr):
    lista = []
    for i in range(1,nr+1):
        lista.append(i)
    shuffle(lista)
    for i in range(0, nr):
        if(lista[i] == 1):
            lista[i] = lista[0]
            lista[0] = 1
            break
    return lista