def factorial(a):
    fact = 1
    i = 1
    while i <= a:
        fact = fact*i
        i += 1
    return fact


b = 5
print(factorial(b))