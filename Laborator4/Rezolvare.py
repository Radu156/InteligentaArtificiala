from GA import GA
from IntegerChromosome import Chromosome


def readData(filename):
    f = open(filename, "r")
    noduri = f.readline()
    nrNoduri = int(noduri)
    matrice = []
    for i in range(0, nrNoduri):
        valori = f.readline()
        numere = valori.split(",")
        lista = []
        for j in range(0, nrNoduri):
            lista.append(int(numere[j]))
        matrice.append(lista)
    # start = int(f.readline())
    # destination = int(f.readline())
    f.close()
    return [nrNoduri,matrice]



def functionFitness(param,matrice):
    suma=0.0
    #print matrice
    #print param
    for i in range(0,len(param)-1):
        if(matrice[param[i]-1][param[i+1]-1] != 0):
            suma += matrice[param[i]-1][param[i+1]-1]
        else:
            return 9999
    suma += matrice[param[len(param)-1]-1][param[0]-1]
    return suma
lista = readData("Exemplu1")
gaParam = {"popSize": 30, "noGen": 200, "pc": 0.8, "pm": 0.1,"matrice":lista[1]}

# # for a representation where len(chromosome) =  len(target)
# problParam = {'function' : fcEval, 'noDiffChars' : len(target), 'noChars' : 26}

# for a representation where  len(chromosome) =  len(set(target))
problParam = {'function': functionFitness, 'noDiffChars':lista[0] , 'noChars':lista[0]}
def decode1(x):
    return x

ga = GA(gaParam, problParam)
ga.initialisation()
ga.evaluation()

stop = False
g = -1
while (not stop and g < gaParam['noGen']):
    g += 1
    #ga.oneGeneration()
    ga.oneGenerationElitism()
    #ga.oneGenerationSteadyState()

    bestChromo = ga.bestChromosome()
    print('Best solution in generation ' + str(g) + ' is: x = ' + str(decode1(bestChromo.repres)) + ' f(x) = ' + str(
        bestChromo.fitness))

