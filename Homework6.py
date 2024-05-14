"""Homework 6
Murashko Maksim Yurevich
Python automatic tester course"""

# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
a = "Robin Singh"
lista = a.split()
print(type(lista))
print(lista)

# "I love arrays they are my favorite" => ["I", "love", "arrays", "they", "are", "my", "favorite"]
text = "I love arrays they are my favorite"
listb = text.split()
print(type(listb))
print(listb)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
x = "Привет, {} {}! Добро пожаловать в {} {}"
Onelist = ["Ivan", "Ivanou"]
town = "Minsk"
Country = "Belarus"
print(f"Привет, {Onelist[0]} {Onelist[1]}! Добро пожаловать в {town} {Country}")

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
New_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(New_list))

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
Nature = ["Derevo", "More", "Listok", "Trava", "Cveti", "Nebo", "Gribi", "Kusti", "Gori", "Tuchi"]
Nature[3] = "Solnce"
Nature.pop(6)
print(Nature)
