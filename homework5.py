"""Заменить символ “#” на символ “/”
в строке 'www.my_site.com#about'
"""

A = "www.my_site.com#about"
print(A.replace("#", "/"))

"""Напишите программу, 
которая добавляет ‘ing’ к словам"""

S = ""
while S == "":
    S = input()
print(S + "ing")

"""В строке “Ivanou Ivan” поменяйте 
местами слова => "Ivan Ivanou" """

name_lastname = "Ivanou Ivan"
name_lastname = name_lastname.split(" ")
print(name_lastname[1], name_lastname[0])

"""Напишите программу которая 
удаляет пробел в начале, в конце строки"""

text = " multiple statements found "
print(text.lstrip().rstrip())

"""Имена собственные всегда начинаются с заглавной буквы, 
за которой следуют строчные буквы. Исправьте данное имя собственное так, 
чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris" """

name = "vasya petya kolya dima maksim anton makar"
print(name.title())
