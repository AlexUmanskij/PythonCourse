import random


class Person:
    def __init__(self, name = None, age = None, gender = None):
        self.name = name
        self.age = age
        self.gender = gender

class educationMaterial:
    def __init__(self,*args):
        self.material = [*args]

    def __len__(self):
        return len(self.material)

class student(Person):
    def __init__(self):
        self.knowledge = []

    def __len__(self):
        return len(self.knowledge)

    def removed(self):
        num = random.randint(0, len(self.knowledge)-1)
        self.knowledge.pop(num)

class teacher(Person):
    studentNumber = 0

    def teach(self, education,*args):
        for i in args:
            teacher.studentNumber += 1
            i.knowledge += education.material



mat1 = educationMaterial("Python")
mat2 = educationMaterial("Version Control Systems")
mat3 = educationMaterial("Relational Databases")
mat4 = educationMaterial("NoSQL databases")
mat5 = educationMaterial("Message Brokers")

st1 = student()
st2 = student()
st3 = student()
st4 = student()

teacher1 = teacher()

teacher1.teach(mat1, st1, st2, st3, st4)
teacher1.name = 'V.V. Ivanov'
st1.name = 'Petrov'
print(teacher1.studentNumber)
teacher1.teach(mat2,  st2, st4)
print(teacher1.studentNumber)
teacher1.teach(mat3,  st4)
print(teacher1.studentNumber)
teacher1.teach(mat4,  st2, st1)
print(teacher1.studentNumber)
teacher1.teach(mat5,  st4, st3, st2, st1)
print(teacher1.studentNumber)

print(f'Студент 1: {st1.knowledge}')
print(f'Студент 2: {st2.knowledge}')
print(f'Студент 3: {st3.knowledge}')
print(f'Студент 4: {st4.knowledge}')

print(teacher1.name)
print(f'ФИО: {st1.name}')


print(f'Студент 4, Длина знаний: {len(st4)}')
print(f'Материал 1, Длина знаний: {len(mat1)}')

st4.removed()
print(f'Студент 4, Длина знаний: {len(st4)}')
st4.removed()
print(f'Студент 4, Длина знаний: {len(st4)}')
#print(teacher1.studentNumber)

