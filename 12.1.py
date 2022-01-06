class Shar():
    def sum(self):
        v = int(input("Введите объем шара: "))
        pi=3.14
        r=int(input("Введите радиус шара: "))
        rezl=(4/3)*pi*(r*r*r)
        print("Объем шара: ", rezl)
    def kub(self):
        p=3.14
        rr=int(input("Ввдеите радиус шара: "))
        s=4*p*(rr*rr)
        print("Площадь боковой поверхности шара: ", s)
rezl=Shar()
rezl.sum()
s=Shar()
s.kub()