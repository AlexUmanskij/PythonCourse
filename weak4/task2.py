import numpy as np
import random

size1 = 8
size2 = 8

massive = np.zeros((size1, size2),int)
print(massive)
k = 1
for i in range(0,size1):
    for j in range(0,size2):
        if massive[i,j-1] == 0 and massive[i-1,j] ==0:
            massive[i,j] = 1

print(massive)