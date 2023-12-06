import math


def currency(fn):
    def wrapper(check):

        try:
            print(fn(check))
        except ValueError:
            print('Меньше 0. Введите новое значение')
            wrapper(input())
    return wrapper

@currency
def square(n):
    print(f'Корень {n}: ')
    return math.sqrt(float(n))
@currency
def log(n):
    print(f'Десятичный логарифм от {n}: ')
    return math.log10(float(n))

square(input())
log(input())

