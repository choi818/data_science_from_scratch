# zip
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
zip_list = zip(list1, list2)
print(next(zip_list))

# unpacking
pairs = [('a', 1), ('b', 2), ('c', 3)]
letters, numbers = zip(*pairs)          # same as zip(('a', 1), ('b', 2), ('c', 3))

def add(a, b): return a + b
print(add(*[1,2]))
