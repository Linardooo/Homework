"""Заменить символ “#” на символ “/”
в строке 'www.my_site.com#about'
"""

a = "www.my_site.com#about"
print(a.replace("#", "/"))

"""Напишите программу, которая добавляет ‘ing’ к словам"""

s = ""
while s == "":
    s = input()
print(s + "ing")

"""В строке “Ivanou Ivan” поменяйте местами слова => "Ivan Ivanou" """

g = "Ivanou Ivan"
g = g.split(" ")
print(g[1], g[0])

"""Напишите программу которая удаляет пробел в начале, в конце строки"""

text = " multiple statements found "
print(text.lstrip().rstrip())

"""Имена собственные всегда начинаются с заглавной буквы, 
за которой следуют строчные буквы. Исправьте данное имя собственное так, 
чтобы оно соответствовало этому утверждению. "pARiS" >> "Paris" """

name = "vasya petya kolya dima maksim anton makar"
print(name.title())
