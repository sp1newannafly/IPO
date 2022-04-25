import numpy as np
z =np.random.randint(2,60, (5,5))
m=z.min()
print("Массив:\n",z)
print("Минимальный элемент массива:\n",m)
z1= z.copy()
z1[0,0] ,m=m, z1[0,0]
print(z1)