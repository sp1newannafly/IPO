class dog:
    def __init__(self, name, age , breed):
       self.name = name
       self.age = age
       self.breed= breed
    def messange(self):
        print("Кличка моей собаки", self.name, ",", "ей" , self.age, "ее порода", self.breed)
st1=dog("Даник", "3", "Такса")
st1.messange()
st2=dog("Илья", "8", "ЛАБрадор")
st2.messange()
st3=dog("Макс", "10", "Пудель")
st3.messange()