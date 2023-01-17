from task3 import TestForMe


a = TestForMe()
b = TestForMe()
print(type(a))
print(id(a), id(b))
print('Одинаковые объекты' if id(a) == id(b) else 'Разные объекты')

if id(a) == id(b):
    print('Одинаковые объекты')
else:
    print('Разные объекты')