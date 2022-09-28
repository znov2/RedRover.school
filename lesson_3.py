# 3.1. Дан список my_list = ['a', 'b', [1, 2, 3], 'd']. Распечатайте значения 1, 2, 3
# my_list = ['a', 'b', [1, 2, 3], 'd']
# print(my_list[2])


# 3.2 Дан список list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# - получите сумму всех чисел,
# - распечатайте все строки, где есть буква 'a'
## list_1 = ['Hi', 'ananas', 2, None, 75, 'pizza', 36, 100]
# list_2 = len(list_1)
# print(sum(list_2))

# 3.3. Превратите лист ['cat', 'dog', 'horse, 'cow'] в кортеж
#

# 3.4. Напишите программу, которая определяет, какая семья больше.
# 1) Программа имеет два input() - например, family_1, family_2.
# 2) Членов семьи нужно перечислить через запятую.
#     Ожидаемый результат - программа выводит семью с бОльшим составом. Если состав одинаковый, print("Equal')
## fameli_1 = input('How many people do you have in family 1? ')
# fameli_2 = input('How many people do you have in family 1? ')
# if fameli_1 > fameli_2:
#     print("Family number one has",  fameli_1, "people.")
# elif fameli_2 > fameli_1:
#     print("Family number one has",  fameli_2, "people.")
# else:
#     print("Equal")


# 3.5. Создайте словарь film c ключами title, director, year, budget, main_actor, slogan. В значения можете передать информацию
# о вашем любимом фильме.
# - распечатайте только ключи
# film = {'title':'Girls', 'director':'Yuri_Chulyukin', 'year':1962, 'budget': 1000, 'main_actor':'Nadejda_Rumyanceva', 'slogan':'Be kinder to each other'}
# for a in film:
#     print(a)

# - распечатайте только значения
# for value in film.values():
#     print(value)

# - распечатайте пары ключ - значение
# for key,value in film.items():
#     print(key, ':', value)


# 3.6. Найдите сумму всех значений в словаре my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
## my_dictionary = {'num1': 375, 'num2': 567, 'num3': -37, 'num4': 21}
# total = sum(my_dictionary.values())
# print(total)

# 3.7. Удалите повторяющиеся значения из списка [1, 2, 3, 4, 5, 3, 2, 1]
# a = [1, 2, 3, 4, 5, 3, 2, 1]
# a[:] = list(set(a))
# print(a)

# 3.8. Даны два множества: set1 = {'a', 'z', 1, 5, 9, 12, 100, 'b'}, set2 = {5, 'z', 1, 8, 9, 21, 100, 'l', 785}
# - найдите значения, которые встречаются в обоих множествах
# - найдите значения, которые не встречаются в обоих множествах
# - проверьте являются ли эти множества подмножествами друг друга