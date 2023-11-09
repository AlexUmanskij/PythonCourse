def positive_numbers_in_list(list1):
    positive = 0
    for i in list1:
        if i > 0:
            positive += 1
    return positive


listTest = [-1, 5,-2,4,-6]
print(positive_numbers_in_list(listTest))

