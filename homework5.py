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
Name_str = "Ivanou Ivan"
Name_list = Name_str.split(" ")
print(Name_list[1], Name_list[0])

# Напишите программу которая удаляет пробел в начале, в конце строки
text = " multiple statements found "
print(text.lstrip().rstrip())

# Имена собственные всегда начинаются с заглавной буквы,
# за которой следуют строчные буквы. Исправьте данное имя собственное так,
# чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris"
name = "vasya petya kolya dima maksim anton makar"
print(name.title())
