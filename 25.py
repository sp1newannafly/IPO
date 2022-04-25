import numpy as np
mass = np.random.randint(-100,100,20)
print("Массив:\n ", mass)
s=0
for i in range(len(mass)):
    if mass[i]%2==0 and mass[i]>0:
        s +=mass[i]
print("Результат сложения положительных четных элементов: ",s)