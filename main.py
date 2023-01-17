class Point:
    x = 0
    y = 1
    width = 3

    def summ(self):
        return self.width + 1


class Point1(Point):
    def summ(self):
        return self.width - 1


a = Point()
a.width += 1
a.width = a.summ()
b = Point1()
b.width = b.summ()
print(a.width, b.width, sep='\n')
print(b.x, b.y)

