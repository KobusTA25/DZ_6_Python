# Задача 30:  Заполните массив элементами арифметической прогрессии. 
# Её первый элемент, разность и количество элементов нужно ввести с 
# клавиатуры. Формула для получения n-го члена прогрессии: 
# an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# a1 = int(input('Введите первый элемент прогрессии: '))
# d = int(input("Введите разность прогрессии: "))
# n = int(input("Введите количество элементов массива: "))
# some_list = []
# for i in range(n):
#     an = a1 + i * d
#     some_list.append(an)
# print("Элемента арифметической прогрессии:")
# for element in some_list:
#     print(element)

# Задача 32: Определить индексы элементов массива (списка), 
# значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)
# import random
# n = int(input("Введите количество элементов списка: "))
# maxi = int(input("Введите max: "))
# mini = int(input("Введите min: "))
# random_some_list = []
# for _ in range(n):
#     random_some_list.append(random.randint(0, 100))
# print("Список:")
# print(random_some_list)
# index_list = []
# for i in range(len(random_some_list)):
#     if mini <= random_some_list[i] <= maxi:
#         index_list.append(i)
# print("Индексы элементов, значения которых находятся в диапазоне от", mini, "до", maxi, ":")
# print(index_list)