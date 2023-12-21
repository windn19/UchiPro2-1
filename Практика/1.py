# Напиши программу для нахождения номера под которым находится значение в связном списке. Необходимо считать значение
# с клавиатуры и вывести под каким номером стоит это значение в связном списке. Если такого значения в списке нет,
# то вывести -1. Нумерация элементов начинается с 1.
#
# В связном списке должны находиться следующие значения:
# grapes -> orange -> banana -> apple -> None
# Входные данные:
# Вводится строка - значение которое надо найти в связном списке.
#
# Выходные данные:
# Выводится целое число - номер значения в связном списке или -1 если его нет.
#
# Пример ввода:
# banana
#
# Пример вывода:
# 3


class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next

    def __str__(self):
        return self.value


def print_linked_list(vertex):
    while vertex:
        print(vertex, end=" -> ")
        vertex = vertex.next
    print('None')


n4 = Node('apple', None)
n3 = Node('banana', n4)
n2 = Node('orange', n3)
n1 = Node('grapes', n2)

s = input()
node = n1
index = 1

while node is not None:
    if node.value == s:
        print(index)
        break
    else:
        node = node.next
    index += 1
else:
    print(-1)

print_linked_list(n1)