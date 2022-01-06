class Complex:
    def __init__(self, k):
        self.k = k

    def __add__(self, c):
        return self.k + c

    def __sub__(self, c):
        return self.k - c

    def __mul__(self, c):
        return self.k * c

    def setattr (self, k, rel, img):
        print("Вызван метод setattr ()")
        self.__dict__[k] = img
        self.__dict__[k] = rel

c = Complex(complex(80))
c.i = 10
print(c.i)
x = complex(15, 8)
print (c + x)
print (c - x)
print (c * x)