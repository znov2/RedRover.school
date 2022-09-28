        # HomeWork 4

# +
#  4.1. Напишите функцию square, принимающую 1 аргумент — сторону квадрата, и возвращающую
#  3 значения (с помощью кортежа): периметр квадрата, площадь квадрата и диагональ квадрата.
#
# import math
#
# a = int(input("сторона квадрата?"))
# def square(a):
#     P = 4 * a
#     S = a ** 2
#     Diag = a * math.sqrt(2)
#     return (P, S, Diag)
#
# print("Perimeter: {:.2f}\nSquare: {:.2f}\nDiadonal: {:.2f}".format(*square(a)))



#????????????????????
#  4.2. Напишите фукнцию, которая принимает произвольное количество именнованных аргументов и выводит их построчно
# в формате аргумент: значение. Например:
# name: John
# last_name: Smith
# age: 35
# position: web developer

# def worker(name, last_name, age, position):
#     name = input("What is your name?")
#     last_name = input("What is your last_name?")
#     age = int(input("How ald are you?"))
#     position = input("What do ypu have job?")
#     return (worker(name, last_name, age, position))
# print("f'name: {name}\nlast_name: {last_name}\nage: {age}\nposition: {position}".format(worker('name, last_name, age, position')))



#+
# 4.3. Используя лямбда-выражение, из списка my_list = [20, -3, 15, 2, -1, -21] создайте новый список, содержащий только
# положительные числа
# my_list = [20, -3, 15, 2, -1, -21]
# new_list = list(filter(lambda x: (x > 1), my_list))
# print(new_list)


#+
# 4.4. Используя лямбда выражение, получите результат перемножения значений в предыдущем списке
# import math
#
# my_list = [20, -3, 15, 2, -1, -21]
# print(math.prod(my_list))


# import functools
# my_list = [20, -3, 15, 2, -1, -21]
# res = functools.reduce(lambda x,y: x*y, func)
# print(res)


# 4.5. Создайте файл my_calc.py и пропишите в нем минимум 4 функции, выполняющие базовые арифметические вычисления.
# Примените эти функции в качестве методов в другом файле.