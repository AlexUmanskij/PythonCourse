def lambda_ciferki(number):
    ciferki = [1, 15, 6, 19, 20]
    return list(filter(lambda x: x % number == 0, ciferki))


print(lambda_ciferki(5))