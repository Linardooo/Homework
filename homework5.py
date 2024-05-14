"""Homework5
Murahsko Maksim Yurevich
Course Python authomatic tester"""

# Заменить символ “#” на символ “/” в строке 'www.my_site.com#about'
A = "www.my_site.com#about"
print(A.replace("#", "/"))

# Напишите программу, которая добавляет ‘ing’ к словам
S = ""
while S == "":
    S = input()
print(S + "ing")

# В строке “Ivanou Ivan” поменяйте естами слова => "Ivan Ivanou"
NAME_STR = "Ivanou Ivan"
NAME_LIST = NAME_STR.split(" ")
print(NAME_LIST[1], NAME_LIST[0])

# Напишите программу которая удаляет пробел в начале, в конце строки
TEXT = " multiple statements found "
print(TEXT.strip())

# Имена собственные всегда начинаются с заглавной буквы,
# за которой следуют строчные буквы. Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
NAME = "vasya petya kolya dima maksim anton makar"
print(NAME.title())

