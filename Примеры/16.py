array = []
array.append(1)
array.append(2)
array.append(3)
print(array)
array.insert(1, 'new')
print(array)

print(array.index(3))
print(array[2])
array.pop()
print(array)
array.pop(0)
print(array)
del array[0]
print(array)