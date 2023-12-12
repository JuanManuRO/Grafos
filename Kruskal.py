class Graph:

    def __init__(self, V, E, W):
        self.V = V
        self.E = E
        self.W = W

    def setVertex(self, newV):
        self.V.append(newV)

    def setEdge(self, newE):
        self.E.append(newE)

    def removeEdge(self, notE):
        self.E.remove(notE)

    def setWeight(self, newW):
        for k in newW:
            self.W[k] = newW[k]

    def ciclo(self, v, Evisited, objective):
        path = []
        Eaux = self.E.copy()

        for n in range(len(Evisited)):
            if Evisited[n] in Eaux:
                Eaux.remove(Evisited[n])

        for i in range(len(Eaux)):
            if Eaux[i].find(v) != -1:
                path.append(Eaux[i])
        possiblePath = path.copy()

        for k in range(len(path)):
            possiblePath[k] = possiblePath[k].replace(v,'')

        if objective in possiblePath:
            return True
        else:
            veracity = False
            for i in range(len(possiblePath)):
                Evisited.append(path[i])
                veracity = veracity or self.ciclo(possiblePath[i], Evisited, objective)
        return veracity

    def conexo(self):
        pathList = []
        Vaux = self.V.copy()
        for i in self.V:
            if i in Vaux:
                Vaux.remove(i)
            for k in range(len(Vaux)):
                pathList.append(i+Vaux[k])

        for n in pathList:
            if self.ciclo(n[0],[],n[1]) == False:
                return False
            else:
                if n in pathList:
                    pathList.remove(n)
                continue
        return True


    def AdjencyMatrix(self):
        listOfLists = []
        for i in self.V:
            listE = []
            for j in self.V:
                vertex = i+j
                vertex2 = j+i
                if vertex in self.E:
                    listE.append(1)
                elif vertex2 in self.E:
                    listE.append(1)
                else:
                    listE.append(0)
            listOfLists.append(listE)
        return listOfLists





def Kruskal(A,T):
    pesosG = list(A.W.values())
    pesosG.sort()
    ciclo = False

    while not(T.conexo()) and not(ciclo):
        if pesosG == []:
            print('El Grafo no tiene pesos validos')
            break
        else:
            minimumW = pesosG[0]

        for key in A.E:
            if A.W[key] == minimumW:
                T.E.append(key)
                ciclops = False
                ciclops = T.ciclo(key[0], [], key[0]) and T.ciclo(key[1], [], key[1])
                if ciclops == True:
                    if key in T.E:
                        T.E.remove(key)
        pesosG.remove(pesosG[0])
        for i in T.V:
            ciclo = T.ciclo(i, [], i)










# # PRUEBA SENCILLA
# V = ['a','b','c','d']
# E = ['ab','ac','bd','cd']
# Weight = {
#     'ab' : 4 ,
#     'ac' : 1 ,
#     'bd' : 3 ,
#     'cd' : 2
# }
#
# T = Graph(V,[],{})
# A = Graph(V,E,Weight)
#
# Kruskal(A,T)
#
# COUNT = 0
# for k in list(A.W.keys()):
#     if k in T.E:
#         T.W[k] = list(A.W.values())[COUNT]
#     COUNT += 1
#
# T.E.sort()
# print(T.E)
# print(T.W)
# print(A.AdjencyMatrix())







#PRUEBA DOS DEL EJEMPLO RANDOM
# V = ['a','b','c','d','e','f','g','h']
# E = [
#     'ab',
#     'bc',
#     'cd','ce',
#     'de','df',
#     'ef',
#     'fg','fh'
# ]

# Weight = {
#     'ab':2,
#     'bc':3,
#     'cd':5,'ce':2,
#     'de':1, 'df':4 ,
#     'ef':2,
#     'fg':3,'fh':1
# }

# T = Graph(V,[],{})
# A = Graph(V,E,Weight)

# Kruskal(A,T)

# COUNT = 0
# for k in list(A.W.keys()):
#     if k in T.E:
#         T.W[k] = list(A.W.values())[COUNT]
#     COUNT += 1

# T.E.sort()
# print(T.E)
# print(T.W)
# print(A.AdjencyMatrix())







# # PRUEBA FINAL DEL EJEMPLO DE LA CLASE
V = ['a','b','c','d','e','f','g','h','i','j','k','l']
E = [
    'ab','ae',
    'bc','bf',
    'cd','cg',
    'dh',
    'ef','ei',
    'fg','fj',
    'gh','gk',
    'hl',
    'ij',
    'jk',
    'kl'
]
Weight = {
    'ab':2,'ae':2,
    'bc':3,'bf':1,
    'cd':1,'cg':2,
    'dh':5,
    'ef':1,'ei':4,
    'fg':3,'fj':2,
    'gh':3,'gk':4,
    'hl':3,
    'ij':3,
    'jk':3,
    'kl':1
}

T = Graph(V,[],{})
A = Graph(V,E,Weight)

Kruskal(A,T)

COUNT = 0
for k in list(A.W.keys()):
    if k in T.E:
        T.W[k] = list(A.W.values())[COUNT]
    COUNT += 1

T.E.sort()
print(T.E)
print(T.W)
print(T.AdjencyMatrix())