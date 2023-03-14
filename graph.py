'''поиск эйлерова цикла
Эйлеров цикл существует тогда 
и только тогда, когда граф связный и степени всех вершин чётны.'''

#обход в глубину (пройти по всем вершинам)

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

obhod_v_glubinu(1, graph_1)

#--------------------------------------------------------

#обход в ширину 