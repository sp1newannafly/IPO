import random
f =[[random.randint(1,40) for j in range(5)] for i in range(5)]
for i in range(5):
    for j in range(5):
        print("%4d" % (f[i][j]), end="")
    print(end='\n')
print (f[0][0],f[1][1],f[2][2],f[3][3],f[4][4])