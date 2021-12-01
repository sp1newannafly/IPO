import random
f =[[random.randint(1,10) for j in range(3)] for i in range(4)]
for i in range(4):
    for j in range(3):
        print("%4d" % (f[i][j]), end="")
    print(end='\n')

print([min(f[i][j] for i in range(4)) for j in range(3)])
