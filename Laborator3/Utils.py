from random import randint


def generateNewValue2(lim1, lim2):
    return randint(lim1, lim2)

def firstGen(net):
    repres = [generateNewValue2(0, net['noNodes']-1) for _ in range(net['noNodes'])]
    for i in range(0,len(repres)/5):
        for j in range(0,len(repres)):
            if net['mat'].item(i,j) == 1:
                repres[j] = repres[i]
    return repres