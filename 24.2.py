import numpy as np
z=np.random.normal(0, 1, (3,4))
print("Матрица", z)
m=z[0,0]+z[1,1]+z[2,2]
print("Сумма главной диагонали матррицы", m)
z1=z.copy()
z1[2,3]=m
print(z1)