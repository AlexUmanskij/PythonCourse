#Напишите функцию, которая принимает любое количество не именованных аргументов и
#возвращает кортеж состоящий из аргументов у которых тип данных str
def tupleMaker(*args, **kwargs):
    a = [*args]
    return tuple(filter(lambda x: type(x)  == str, a))



print(tupleMaker(7, 'strstr', '8', 20.0, True))
print(type(tupleMaker()))