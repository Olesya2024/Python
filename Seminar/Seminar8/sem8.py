"""Задача №51. Решение в группах
Напишите функцию same_by(characteristic, objects), которая
проверяет, все ли объекты имеют одинаковое значение
некоторой характеристики, и возвращают True, если это так.
Если значение характеристики для разных объектов
отличается - то False. Для пустого набора объектов, функция
должна возвращать True. Аргумент characteristic - это
функция, которая принимает объект и вычисляет его
характеристику.
Ввод: Вывод:
values = [0, 2, 10, 6] same
if same_by(lambda x: x % 2, values):
print(‘same’)
else:
print(‘different’)"""

# def same_by(characteristic, objects):
#     return len(list(filter(characteristic, objects)))==len(objects)
# values = [0, 2, 10, 6]
# if same_by(lambda x: x % 2==0, values):
#     print('same')
# else:
#     print('different')

"""Напишите программу, которая подсчитает и выведет сумму квадратов 
всех двузначных чисел, делящихся на 9.
При решении задачи используйте комбинацию функций filter, map, sum.

Обратите внимание: на 9 должно делиться исходное двузначное число, а не его квадрат."""

# str = '9 10 2 -3 6 9'
# print(sum(map(lambda x: int(x) ** 2, filter(lambda a: int(a) % 9 == 0, str.split()))))

# #1.напечатать строку в одну линию C:\WINDOWS\System32\drivers\ets\nst
# print(r"C:\WINDOWS\System32\drivers\ets\nst")

