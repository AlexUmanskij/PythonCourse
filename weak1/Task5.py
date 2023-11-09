def line_check(line1, line2):
    if line1 in line2:
        print("Да")
    else:
        print("Нет")


str1 = 'test'
str2 = 'test_1'
line_check(str1, str2)
line_check(str2, str1)
