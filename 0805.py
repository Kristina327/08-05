class Student:
    def __init__(self, name, surname, group, gender, progress, university):
        self.name = name
        self.surname = surname
        self.group = group
        self.gender = gender
        self.progress = progress
        self.university = university

    def display(self):
        return self.name, self.surname, self.group, self.gender, self.progress, self.university

    def __del__(self):
        if self.progress == 'задолжник':
            print(f"Отчислен студент {self.name} {self.surname}, {self.progress}.")
        elif self.progress == 'отличник':
            print(f"Cтудент {self.name} {self.surname}, {self.progress} - молодец!")


S1 = Student('Виктор', 'Романенко', 'группа АНГ-191', 'пол мужской', 'отличник', 'МПГУ')
print(S1.display())
S2 = Student('Александр', 'Кубраченко', 'группа ИНФ-197', 'пол мужской', 'задолжник', 'МПГУ')
print(S2.display())
S3 = Student('Валерия', 'Ольховская', 'группа ЗИ-12', 'пол женский', 'отличник', 'МПГУ')
print(S3.display())

del S2
del S1
del S3

try:
    input("Press Enter and exit")
except SyntaxError:
    exit()