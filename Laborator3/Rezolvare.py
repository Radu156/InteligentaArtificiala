from GA import GA
import networkx as nx
import scipy as sp
import matplotlib.pyplot as plt
def readData(filename):
    G = nx.read_gml(filename,label='id')

    net2 = {}
    net2['noNodes'] = G.number_of_nodes()
    net2['mat'] = nx.adjacency_matrix(G).todense()
    net2['noEdges'] = G.number_of_edges()
    net2['degrees'] = [val for (node, val) in G.degree()]
    net2['graph'] = G
    return net2



def modularity(communities, param):
    noNodes = param['noNodes']
    mat = param['mat']
    degrees = param['degrees']
    noEdges = param['noEdges']
    M = 2 * noEdges
    Q = 0.0
    for i in range(0, noNodes):
        for j in range(0, noNodes):
            if (communities[i] == communities[j]):
                Q += (mat.item(i,j) - degrees[i] * degrees[j] / M)
    return Q * 1 / M

net2 = readData('karate.gml')
gaParam = {"popSize": 100, "noGen": 200, "pc": 0.8, "pm": 0.1,"network":net2}

# # for a representation where len(chromosome) =  len(target)
# problParam = {'function' : fcEval, 'noDiffChars' : len(target), 'noChars' : 26}

# for a representation where  len(chromosome) =  len(set(target))
problParam = {'function': modularity, 'noDiffChars':net2['noNodes'] , 'noChars':net2['noNodes']-1,'net':net2}
def decode1(x):
    comunities=[]
    for i in range(0,problParam['noChars']+1):
        comunities.append([])
    for i in range(0,net2['noNodes']):
        comunities[x[i]].append(i+1)
    j=0
    while j < len(comunities):
        if comunities[j] == []:
            comunities.pop(j)
        else:
            j+=1
    return comunities

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
        bestChromo.fitness)) + " " + 'Numar comunitati:' + str(len(decode1(bestChromo.repres)))


