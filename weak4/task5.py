# 5.	Создайте функцию, которая
#   a.	принимает число (количество элементов в матрице)
#   b.	Проверяет можно ли построить матрицы с размерностью из множителей принимаемого числа.
#   c.	При проверке не учитывать матрицы с множителем “1”
#   d.	постройте все возможные матрицы и выведите в консоль.
#   e.	если число нельзя разбить на множители без остатка выведите сообщение в консоль.
import numpy as np
def initialisation(n):
    k = 0;
    for i in range(2, n):
        if n % i == 0:
            k = 1
            print(np.ones((i, int(n/i))))
    if k == 0:
        print('Построить матрицы невозможно')

initialisation(20)