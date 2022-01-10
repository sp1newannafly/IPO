class ekz():
    def __init__(self, disc, students, hours):
        self.disc= disc
        self.students = students
        self.hours = hours
    def quality(self):
        Q = self.students/self.hours
        return Q
    def getInfo (self):
        print ("Дисциплина:",self.disc)
        print ("Число студентов на экзамене", self.students)
        print ("Продолжительность экзамена", self.hours)
class ekz():
    def __init__(self, disc, students, hours, dva, QP):
        self.disc = disc
        self.students = students
        self.hours = hours
        self.dva = dva
    def getInfo2 (self):
        QP = self.students/self.hours*(100-self.dva)/100
        print ("Дисциплина:",self.disc)
        print ("Число студентов", self.students)
        print ("Продолжительность экзамена", self.hours)
        print ("Процент двоек", self.dva)
        print ("Количество двоек", QP)
res2 = ekz ("Русский", 800, 4, 20, 2)
print (res2.getInfo2())
