print("<------------tuple--------->")
g = (1, 2, 3, "afsef", 2, [1, 2, 3]) #не изменяется но быстрее
print(type(g))
print(g)
g[5].append([2,4,6])
print(g)
if 3 in g:
    print("3 in g")
if 6 in g:
    print("6 in g")

f = ("wadw", "awd", "fsef")
print(f + g)
print("---------------------")
print(any(f))
print("---------------------")
print(len(f))
print("---------------------")
print(g.count(3))
print("---------------------")
print(sorted(f))
print("<------------dict--------->")





print("<------------set---------->")


