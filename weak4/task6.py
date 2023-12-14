# 6.	Постройте класс для анализа файла с данными:
#    a.	Класс принимает путь к файлу при инициализации
#    b.	Создайте метод для чтения файла - метод считывает массив из файла и сохраняет в атрибут класса.
#    Файл состоит из строк с произвольным текстом, элементами массива должны быть строки.
#    c.	Создайте метод поиска по тексту. Метод принимает паттерн поиска и возвращает список всех найденных совпадений.
import re


class Reader:
    def __init__(self, filename):
        with open(filename, "r") as file:
            self.contents = file.readlines()

    def printer(self):
        print(self.contents)

    def search(self, name):
        fiendMassive = []
        for i in self.contents:
            a = re.search(r"{}".format(name), i)
            if a != None:
                fiendMassive.append(i)
        return fiendMassive

a = Reader('Task6Text.txt')
a.printer()
print(a.search("14"))

