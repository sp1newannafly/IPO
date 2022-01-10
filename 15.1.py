class c(object):
    def __init__(self):
        self._x=None
    @property
    def x(self):
        x = int(input("Введите радиус шара "))
        pi=3.14
        obem=(4/3)*pi*(x*x*x)
        print("Объем шара равен: ", obem)
    @x.setter
    def x(self, value):
        x = int(input("Введите радиус шара "))
        pi=3.14
        ploshd=4*pi*(x*x)
        print("Площадь шара равна: ", ploshd)
        self._shar = value
    
c= c()
c.x = 'foo'  # setter called
foo = c.x   # getter called
