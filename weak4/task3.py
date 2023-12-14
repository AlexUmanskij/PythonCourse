# Создайте матрицы 8x4 и 4x2 и перемножьте, результирующую матрицу выведите в консоль.
import numpy as np
import random

a = np.random.randint(-100, 100, (8, 4))
b = np.random.randint(-100, 100, (4, 2))

print(a)
print(b)

res = a.dot(b)
print(res)