from weak1.Task2 import massive1


def massive_summarize(massive1, massive2): # функция прибавляет к листу в первом аргументе или элемент или другой список
    if type(massive2) == list: #проверка на то является ли второй аргумент списком
        massive1.extend(massive2) #если да - используется метод для суммирования списков
    else:
        massive1.append(massive2) #если нет - используется метод для суммирования списка с одиночным элементом

    return massive1


a1 = [1, 2, "end1"]
a2 = ['begin2',3, 4, 5]
a3 = 46
print(type(a1))
print(massive_summarize(a1, a2))
print(massive_summarize(a2, a3))
