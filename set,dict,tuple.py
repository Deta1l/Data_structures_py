'''
list == tuple(не изменяется)
set - разномный порядок, элементы не повторяются
словарь - ключ элемент
'''



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

d = {'dict': 1, 'dictionary': 2}
print(d)
d1 = dict(short='dict', long='dictionary')
d2 = dict([(1, 1), (2, 4)])
d3 = dict.fromkeys(['a', 'b'], 100)
print("---------------------")
print(d1, '\n', d2, '\n', d3)
d4 = {a: a ** 2 for a in range(7)}
print("---------------------")
print(d4)
d3[1] = 4 ** 2
d3['b'] = 45
print("---------------------")
print(d3)


'''
dict.clear() - очищает словарь.

dict.copy() - возвращает копию словаря.

classmethod dict.fromkeys(seq[, value]) - создает словарь с ключами из seq и значением value (по умолчанию None).

dict.get(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а возвращает default (по умолчанию None).

dict.items() - возвращает пары (ключ, значение).

dict.keys() - возвращает ключи в словаре.

dict.pop(key[, default]) - удаляет ключ и возвращает значение. Если ключа нет, возвращает default (по умолчанию бросает исключение).

dict.popitem() - удаляет и возвращает пару (ключ, значение). Если словарь пуст, бросает исключение KeyError. Помните, что словари неупорядочены.

dict.setdefault(key[, default]) - возвращает значение ключа, но если его нет, не бросает исключение, а создает ключ со значением default (по умолчанию None).

dict.update([other]) - обновляет словарь, добавляя пары (ключ, значение) из other. Существующие ключи перезаписываются. Возвращает None (не новый словарь!).

dict.values() - возвращает значения в словаре.
'''

print("<------------set---------->")

a = set('hello')
print(a)

a2 = {i ** 2 for i in range(10)} # генератор множеств
print(a2)

words = ['hello', 'daddy', 'hello', 'mum']
print(set(words))

'''
len(s) - число элементов в множестве (размер множества).
x in s - принадлежит ли x множеству s.
set.isdisjoint(other) - истина, если set и other не имеют общих элементов.
set == other - все элементы set принадлежат other, все элементы other принадлежат set.
set.issubset(other) или set <= other - все элементы set принадлежат other.
set.issuperset(other) или set >= other - аналогично.
set.union(other, ...) или set | other | ... - объединение нескольких множеств.
set.intersection(other, ...) или set & other & ... - пересечение.
set.difference(other, ...) или set - other - ... - множество из всех элементов set, не принадлежащие ни одному из other.
set.symmetric_difference(other); set ^ other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.copy() - копия множества.
------------
set.update(other, ...); set |= other | ... - объединение.
set.intersection_update(other, ...); set &= other & ... - пересечение.
set.difference_update(other, ...); set -= other | ... - вычитание.
set.symmetric_difference_update(other); set ^= other - множество из элементов, встречающихся в одном множестве, но не встречающиеся в обоих.
set.add(elem) - добавляет элемент в множество.
set.remove(elem) - удаляет элемент из множества. KeyError, если такого элемента не существует.
set.discard(elem) - удаляет элемент, если он находится в множестве.
set.pop() - удаляет первый элемент из множества. Так как множества не упорядочены, нельзя точно сказать, какой элемент будет первым.
set.clear() - очистка множества.
'''