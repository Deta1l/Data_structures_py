
#обход в глубину 

graph_1 = {
    1: [2, 3],
    2: [4, 5],
    3: [],
    4: [],
    5: []
}

def obhod_v_glubinu(x, f):

    visited_1 = []  
    def glubina_(x):
        if x in visited_1:  
            return
        visited_1.append(x)  
        for i in f[x]:  
            if not i in visited_1:
                glubina_(i)
    glubina_(x) 
    print(visited_1)

#obhod_v_glubinu(1, graph_1)

#--------------------------------------------------------

#обход в ширину 
def obhod_v_shirinu(x,f):
    visited_1 = [] 
    queue = []  
    otvet = []

    def shir_(x):
        if x in visited_1: 
            return
        visited_1.append(x)  
        otvet.append(x)  
        for i in f[x]: 
            if not i in visited_1:
                queue.append(i)
        while queue:
            shir_(queue.pop(0))

    shir_(x)  
    print(otvet)  

#obhod_v_shirinu(1, graph_1)

#--------------------------------------------------------

 #гамильтонов цикл

G = {
    1:[2,3,4], 
    2:[1,3,4], 
    3:[1,2,4], 
    4:[1,2,3]
}

def hamilton(G, size, pt, path=[]):
    print(pt, path)
    if pt not in set(path):
        path.append(pt)
        if len(path)==size:
            return path
        for pt_next in G.get(pt, []):
            res_path = [i for i in path]
            candidate = hamilton(G, size, pt_next, res_path)
            if candidate is not None:  
                return candidate
        print(path)
    else:
        print('pt {} already in path {}'.format(pt, path))


hamilton(G, 4, 1)

#--------------------------------------------------------
#эйлеров цикл

import networkx as nx 
import matplotlib.pyplot as plt

distances = {
    'A': {'B': 2},
    'B': {'C': 4},
    'C': {'D': 8},
    'D': {'A': 7}
}

G = nx.DiGraph()
for k,v in distances.items():
    for k2,v2 in v.items():
        G.add_edge(k, k2, dist=v2)

nx.is_eulerian(G)
#nx.draw(G, with_labels=True)

#--------------------------------------------------------

#гамильтонов цикл 2 вариант 

import networkx as nx
from networkx.algorithms import tournament
G = nx.DiGraph()

distances = {
    'A': {'B'},
    'B': {'C'},
    'C': {'A', 'A'},
    'D': {'B', 'E'},
    'E': {'A', 'D'}}

for k,v in distances.items():
    for k2 in v:
        G.add_edge(k, k2)

nx.draw(G, with_labels=True)

tournament.hamiltonian_path(G)


