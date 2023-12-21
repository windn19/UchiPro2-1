class Deque:
    def __init__(self):
        self.items = []

    def push_back(self, item):
        self.items.append(item)

    def push_front(self, item):
        self.items.insert(item, 0)

    def pop_back(self):
        if self.items:
            print(self.items.pop())
        else:
            print('error')

    def pop_front(self):
        if self.items:
            print(self.items.pop(0))
        else:
            print('error')

    def size(self):
        print(len(self.items))


eval(input())
# [deque := Deque(), deque.pop_back(), deque.push_back(1), deque.push_back(2), deque.push_back(3), deque.push_front(0), deque.pop_back(), deque.pop_front(), deque.size()]
# [deque := Deque(), deque.push_back(1), deque.push_back(2), deque.push_back(3), deque.pop_front(), deque.pop_front(), deque.pop_front(), deque.pop_front()]
