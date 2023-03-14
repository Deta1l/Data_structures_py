'''поиск эйлерова цикла
Эйлеров цикл существует тогда 
и только тогда, когда граф связный и степени всех вершин чётны.'''

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
#алгоритм дейкстры
'''
class Graph:
    def __init__(self, edges, n):
        self.adjList = [None] * n
        
        for i in range(n):
            self.adjList[i] = []
        for (src, dest, weight) in edges:
            self.adjList[src].append((dest, weight))
'''
 
 #--------------------------------------------------------
 #гамильтонов цикл

G = {0:[1],
    1:[0, 2], 
    2:[1, 3], 
    3:[2, 4, 5], 
    4:[3, 6], 
    5:[3], 
    6:[4]
}

def hamilton(graph, start_v):
    size = len(graph)

    to_visit = [None, start_v]
    path = []
    while(to_visit):
        v = to_visit.pop()
        if v : 
            path.append(v)
            if len(path) == size:
                break
            for x in set(graph[v])-set(path):
                to_visit.append(None) # out
                to_visit.append(x) # in
        else: # if None we are comming back and pop v
            path.pop()
    return path

print(hamilton(G,6))