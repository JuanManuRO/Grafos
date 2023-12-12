import copy

class sudoku:

    def __init__(self, matriz):
        self.matriz = matriz
        self.tamano = len(matriz)

    def __str__(self):
        for i in range(self.tamano):
            print(self.matriz[i])
        return ""

    def completo(self):
        for i in range(self.tamano):
            if 0 in self.matriz[i]:
                return False
        return True

    def ver_filas(self):
        for i in range(self.tamano):
            for j in range(self.tamano):
                aux = [x for x in self.matriz[i]]
                aux.pop(j)
                aux1 = self.matriz[i][j]
                if (aux1 != 0) and (aux1 in aux):
                    return False
        return True

    def ver_columnas(self):
        for i in range(self.tamano):
            aux = []
            for j in range(self.tamano):
                aux.append(self.matriz[j][i])
            for k in range(self.tamano):
                aux2 = aux.copy()
                aux2.pop(k)
                aux1 = self.matriz[k][i]
                if (aux1 != 0) and (aux1 in aux2):
                    return False
        return True

    def ver_seccion(self):
        for i in range(int((self.tamano)**0.5)):
            for j in range(int((self.tamano)**0.5)):
                aux = []
                for k in range(int((self.tamano)**0.5)):
                    for l in range(int((self.tamano)**0.5)):
                        aux.append(self.matriz[int((self.tamano)**0.5)*i+k][int((self.tamano)**0.5)*j+l])
                for m in range(self.tamano):
                    aux2 = aux.copy()
                    aux2.pop(m)
                    aux1 = aux[m]
                    if (aux1 != 0) and (aux1 in aux2):
                        return False
        return True

    def valido(self):
        if self.ver_columnas():
            if self.ver_filas():
                if self.ver_seccion():
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    def generar(self):
        for i in range(self.tamano):
            vecinos = []
            if 0 in self.matriz[i]:
                posicion = (self.matriz[i]).index(0)
                for j in range(self.tamano):
                    aux = (copy.deepcopy(self.matriz))
                    aux[i][posicion] = j + 1
                    vecinos.append(aux)
                return vecinos




class grafo:

    def __init__(self, V, E):
        self.V = V
        self.E = E

    def vecinos(self, v):
        tableros = (self.V[v]).generar()
        existentes = len(self.V)
        vecis = []
        for i in range(len(tableros)):
            valor = i + existentes + 1
            self.V[str(valor)] = sudoku(tableros[i])
            self.E.append(v + "," + str(valor))
            vecis.append(str(valor))
        return vecis

    def backtracking(self,v):
        revisar = self.vecinos(v)
        for i in revisar:
            comp = self.V[i].completo()
            val = self.V[i].valido()
            if (not comp) and val:
                self.backtracking(i)
            elif comp and val:
                print("Solucion:")
                sol = self.V[i]
                print(self.V[i])
                return sol



muy_facil = [
    [0,0,0, 0,3,0, 5,0,6],
    [0,0,2, 0,0,0, 3,8,7],
    [0,6,0, 5,0,0, 0,2,9],

    [0,7,0, 0,8,4, 2,3,5],
    [4,0,0, 2,5,7, 0,0,1],
    [0,2,0, 0,6,0, 4,0,8],

    [0,8,6, 7,4,0, 9,5,3],
    [0,0,0, 0,0,0, 7,6,0],
    [7,4,5, 6,0,0, 0,1,2]
]

mf = sudoku(muy_facil)
gmf = grafo({"1": mf}, [])
# test = mf.generar()
# for i in range(9):
#      print(not sudoku(test[i]).completo())
gmf.backtracking("1")

extremo = [
    [1,0,0, 0,0,0, 0,9,0],
    [0,6,5, 0,0,9, 0,0,0],
    [0,0,0, 6,3,0, 0,0,2],

    [2,0,6, 0,4,7, 0,0,5],
    [0,0,8, 3,5,0, 0,2,0],
    [0,0,0, 0,0,0, 0,0,4],

    [0,0,9, 0,0,0, 1,0,8],
    [0,0,0, 9,0,0, 0,0,0],
    [7,5,0, 0,0,0, 4,0,0]
]

ext = sudoku(extremo)
gext = grafo({"1":ext}, [])
gext.backtracking("1")

cuatro = [
    [0,0, 0,0],
    [0,0, 0,0],

    [0,0, 0,0],
    [0,0, 0,0]
]
cuat = sudoku(cuatro)
gcuat = grafo({"1": cuat}, [])
gcuat.backtracking("1")