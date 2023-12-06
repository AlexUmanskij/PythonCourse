#Имеются два списка состоящие из произвольных элементов.
#Напишите функцию которая возвращает пересечение списков (элементы которые встречаются в и там и там)

def compared_lists(list1, list2):
    newList = []
    for i in list1:
        if i in list2:
            newList.append(i)
    return newList


l1 = [1, 7, "21414", True, False]
l2 = [4, 'True', True, False, '21414', 1]
print(compared_lists(l1, l2))
