"""Homework 6 14.05.2024
Murashko Maksim Yurevich
Python automatic tester course"""

# Перевести строку в список "Robin Singh" => ["Robin”, “Singh"]
A = "Robin Singh"
lista = A.split()
print(type(lista))
print(lista)

# "I love arrays they are my favorite" => 
# ["I", "love", "arrays", "they", "are", "my", "favorite"]
TEXT = "I love arrays they are my favorite"
listb = TEXT.split()
print(type(listb))
print(listb)

# Дан список: [Ivan, Ivanou], и 2 строки: Minsk, Belarus
# Напечатайте текст: “Привет, Ivan Ivanou! Добро пожаловать в Minsk Belarus”
X = "Привет, {} {}! Добро пожаловать в {} {}"
Onelist = ["Ivan", "Ivanou"]
TOWN = "Minsk"
COUNTRY = "Belarus"
print(f"Привет, {Onelist[0]} {Onelist[1]}! Добро пожаловать в {TOWN} {COUNTRY}"
     )

# Дан список ["I", "love", "arrays", "they", "are", "my", "favorite"]
# сделайте из него строку => "I love arrays they are my favorite"
New_list = ["I", "love", "arrays", "they", "are", "my", "favorite"]
print(' '.join(New_list))

# Создайте список из 10 элементов, вставьте на 3-ю позицию новое значение,
# удалите элемент из списка под индексом 6
NATURE = ["Derevo", "More", "Listok", "Trava", "Cveti", 
          "Nebo", "Gribi", "Kusti", "Gori", "Tuchi"]
NATURE[3] = "Solnce"
NATURE.pop(6)
print(NATURE)
