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

#эйлеров граф

def find_eulerian_tour(graph):
    stack = [];
    tour = []
 
    stack.append(graph[0][0])
 
    while len(stack) > 0:
        v = stack[len(stack) - 1]
 
        degree = get_degree(v, graph)
 
        if degree == 0:
            stack.pop()
            tour.append(v)
        else:
            index, edge = get_edge_and_index(v, graph)
            graph.pop(index)
            stack.append(edge[1] if v == edge[0] else edge[0])
    return tour
 
 
def get_degree(v, graph):
    degree = 0
    for (x, y) in graph:
        if v == x or v == y:
            degree += 1
 
    return degree
 
 
def get_edge_and_index(v, graph):
    edge = ();
    index = -1
 
    for i in range(len(graph)):
        if (v == graph[i][0] or v == graph[i][1]):
            edge, index = graph[i], i
            break
 
    return index, edge
 
 
graph = [(0, 1), (1, 5), (1, 7), (4, 5),
(4, 8), (1, 6), (3, 7), (5, 9),
(2, 4), (0, 4), (2, 5), (3, 6), (8, 9)]
 
#print((find_eulerian_tour(graph)))