def abbreviation(line1):
    try:
        type(line1) != str

        annogram = ''
        marker = 1

        for i in line1:
            if marker == 1:
                annogram += i
            marker = 0
            if i == ' ':
                marker = 1

        print(annogram)
    except:
        print("Неверный тип данных")

testLine1 = '123 321 421 dfe'
testLine2 = [1,2,4]
abbreviation(testLine1)
abbreviation(testLine2)
