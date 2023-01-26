a = []
for i in range(10):
    a.append(i)

print(a)
print(*a)

print("-----------------")
b = [i for i in a]
print(b)

print("-----------------")
c = [[1,2,3],[4,2,3]]
print(c)

print("-----------------")
for i in range(len(c)):
    print(c[i], end=" ")

print("\n-----------------")

example_array = [[1, 2], [3, 4]]
example_array.insert(0, -1)
example_array.insert(2, [-1, 13, 64])
print(example_array)

print("-----------------")

example_array1 = [1, 2, 3, 4]
example_array1.extend([5, 6])
print(example_array1)

print("-----------------")

print(example_array1.index(4))

print("-----------------")

f = [[1, 2], [3, 4]]
print(f[::-1])
print(f[1:])
print(f[0][:-1])

print("-----------------")

g = [1, 16, 'sfse', 3, 4, 'efs']
for i in g:
    if type(i) != int:
        g.pop(g.index(i))
print(g)


'''
append()	Добавляет элементы в конец списка
clear()	Удаляет все элементы в списке
copy()	Возвращает копию списка
count()	Возвращает число элементов с определенным значением
extend()	Добавляет элементы списка в конец текущего списка
index()	Возвращает индекс первого элемента с определенным значением
insert()	Добавляет элемент в определенную позицию
pop()	Удаляет элемент по индексу
remove()	Убирает элементы по значению
reverse()	Разворачивает порядок в списке
sort()	Сортирует список
'''
