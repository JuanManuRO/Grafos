# inicial = "a"
# V = ["a", "b", "c", "d", "e"]
#
# mat = [["null", 2, 3, "inf", "inf"],
#       [2, "null", "inf", 2, "inf"],
#       [3, "inf" , "null", 2, "inf"],
#       ["inf", 2, 2, "null", 1],
#       ["inf", "inf", "inf", 1, "null"]]


mat = [["null", 1, "inf", 2, 1,"inf", "inf", "inf", "inf", "inf", "inf", "inf", 2, "inf", "inf", "inf"],
       [1, "null", 2, "inf", "inf", 3, "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf"],
       ["inf", 2, "null", 1, "inf", "inf", 3, "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf"],
       [2, "inf", 1, "null", "inf", "inf", "inf", 1, "inf", "inf", "inf", "inf", "inf", "inf", "inf", 2],
       [1, "inf", "inf", "inf", "null", 2, "inf", "inf", 2, "inf", "inf", "inf", "inf", "inf", "inf", "inf"],
       ["inf", 3, "inf", "inf", 2, "null", 3, "inf", "inf", 3, "inf", "inf", "inf", "inf", "inf", "inf"],
       ["inf", "inf", 3, "inf", "inf", 3, "null", 2, "inf", "inf", 4, "inf", "inf", "inf", "inf", "inf"],
       ["inf", "inf", "inf", 1, "inf", "inf", 2, "null", "inf", "inf", "inf", 3, "inf", "inf", "inf", "inf"],
       ["inf", "inf", "inf", "inf", 2, "inf", "inf", "inf", "null", 3, "inf", "inf", 3, "inf", "inf", "inf"],
       ["inf", "inf", "inf", "inf", "inf", 3, "inf", "inf", 3, "null", 4, "inf", "inf", 4, "inf", "inf"],
       ["inf", "inf", "inf", "inf", "inf", "inf", 4, "inf", "inf", 4, "null", 3, "inf", "inf", 3, "inf"],
       ["inf", "inf", "inf", "inf", "inf", "inf", "inf", 3, "inf", "inf", 3, "null", "inf", "inf", "inf", 2],
       [2, "inf", "inf", "inf", "inf", "inf", "inf", "inf", 3, "inf", "inf", "inf", "null", 2, "inf", 2],
       ["inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", 4, "inf", "inf", 2, "null", 2, "inf"],
       ["inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", "inf", 3, "inf", "inf", 2, "null", 3],
       ["inf", "inf", "inf", 2, "inf", "inf", "inf", "inf", "inf", "inf", "inf", 2, 2, "inf", 3, "null"]
]
inicial = "m"
V = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p"]

distancias = {inicial: 0}
caminos = {inicial: inicial}

for p in V:
    if p not in distancias:
        distancias[p] = 999999999

print(distancias)
vertices = [inicial]

for v in vertices:
    for e in range(len(mat[V.index(v)])):
        if type(mat[V.index(v)][e]) != type("filtro"):
            if V[e] not in vertices:
                vertices.append(V[e])
            if distancias[v] + mat[V.index(v)][e] < distancias[V[e]]:
                distancias[V[e]] = distancias[v] + mat[V.index(v)][e]
                caminos[V[e]] = caminos[v] + V[e]



print(distancias)
print(caminos)
