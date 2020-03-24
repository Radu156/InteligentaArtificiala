from random import randint, seed, uniform, sample

from Utils import firstGen


def generateNewValue(lim1, lim2):
    return randint(lim1, lim2)


# integer representation
class Chromosome:
    def __init__(self, problParam=None):
        self.__problParam = problParam
        # # random values, without constraints
        #self.__repres = [generateNewValue(0,problParam['noChars']) for _ in range(problParam['noDiffChars'])]
        self.__repres = firstGen(self.__problParam['noDiffChars'])
        # random values with constraints
       # indexes = [i for i in range(problParam['noChars'])]
        #self.__repres = sample(indexes, problParam['noDiffChars'])
       # self.__fitness = 0.0

    @property
    def repres(self):
        return self.__repres

    @property
    def fitness(self):
        return self.__fitness

    @repres.setter
    def repres(self, l=[]):
        self.__repres = l

    @fitness.setter
    def fitness(self, fit=0.0):
        self.__fitness = fit

    def crossover(self, c):
        # order XO
        pos1 = randint(-1, self.__problParam['noDiffChars'] - 1)
        pos2 = randint(-1, self.__problParam['noDiffChars'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        k = 0
        newrepres = self.__repres[pos1: pos2]
        for el in c.__repres[pos2:] + c.__repres[:pos2]:
            if (el not in newrepres):
                if (len(newrepres) < self.__problParam['noDiffChars'] - pos1):
                    newrepres.append(el)
                else:
                    newrepres.insert(k, el)
                    k += 1
        for i in range(0,len(newrepres)):
            if(newrepres[i] == 1):
                newrepres[i] = newrepres[0]
                newrepres[0] = 1
                break
        offspring = Chromosome(self.__problParam)
        offspring.repres = newrepres
        return offspring

    def mutation(self):
        # insert mutation
        pos1 = randint(1, self.__problParam['noDiffChars'] - 1)
        pos2 = randint(1, self.__problParam['noDiffChars'] - 1)
        if (pos2 < pos1):
            pos1, pos2 = pos2, pos1
        el = self.__repres[pos2]
        del self.__repres[pos2]
        self.__repres.insert(pos1 + 1, el)

    def __str__(self):
        return "\nChromo: " + str(self.__repres)

    def __repr__(self):
        return self.__str__()

    def __eq__(self, c):
        return self.__repres == c.__repres and self.__fitness == c.__fitness