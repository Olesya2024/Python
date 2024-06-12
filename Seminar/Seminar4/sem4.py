# Задача №25. Решение в группах
# Напишите программу, которая принимает на вход
# строку, и отслеживает, сколько раз каждый символ
# уже встречался. Количество повторов добавляется к
# символам с помощью постфикса формата _n.
# Input: a a a b c a a d c d d
# Output: a a_1 a_2 b c a_3 a_4 d c_1 d_1 d_2
# Для решения данной задачи используйте функцию
# .split()

# dict = {}
# string = "a a a b c a a d c d d"
# string_res = ""

# for i in string.split():
#     if i in dict:
#         string_res = string_res + i + "_" + str(dict[i]) + " "
#     else:
#         string_res = string_res + i + " "
#     dict[i] = 1 + dict.get(i, 0)
# print(string_res)


# Задача №27. Решение в группах
# Пользователь вводит текст(строка). Словом считается
# последовательность непробельных символов идущих
# подряд, слова разделены одним или большим числом
# пробелов. Определите, сколько различных слов
# содержится в этом тексте.
# Input: She sells sea shells on the sea shore The shells
# that she sells are sea shells I'm sure.So if she sells sea
# shells on the sea shore I'm sure that the shells are sea
# shore shells
# Output: 13

# text = "She sells sea shells on the sea shore The shells that she sells are sea shells I'm sure. So if she sells sea shells on the sea shore I'm sure that the shells are sea shore shells"
# text = text.upper()
# text = text.replace('.',' ')
# text = text.split()
# print(text)
# print(len(set(text)))



# Домашняя
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с
# повторениями). Выдать без повторений в порядке возрастания все те числа, которые
# встречаются в обоих наборах.
# Пользователь вводит 2 числа. n - кол-во элементов первого множества. m - кол-во
# элементов второго множества. Затем пользователь вводит сами элементы множеств.
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12


# n = int(input("Введите количество элементов в первом множестве: "))
# m = int(input("Введите количество элементов во втором множестве: "))

#     # Получаем сами элементы множеств
# set1 = set(map(int, input("Введите элементы первого множества через пробел: ").split()))
# set2 = set(map(int, input("Введите элементы второго множества через пробел: ").split()))

#     # Находим пересечение множеств
# intersection_result = sorted(set1.intersection(set2))

#     # Выводим результат
# print(*intersection_result)


   
# 11 6
# 2 4 6 8 10 12 10 8 6 4 2
# 3 6 9 12 15 18
# 6 12

# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на
# круглой грядке, причем кусты высажены только по окружности. Таким образом, у
# каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них
# выросло различное число ягод – на i-ом кусте выросло ai  ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое может
# собрать за один заход собирающий модуль, находясь перед некоторым кустом
# заданной во входном файле грядки.
# 4 -> 1 2 3 4
# 9

# def find_max_berries(bushes):
#     n = len(bushes)
#     max_berries = 0
    
#     if n < 3:
#         return sum(bushes)  # Если кустов меньше трех, собираем все ягоды.
    
#     for i in range(n):
#         # Выбираем каждый куст и два его соседа, учитывая круговую структуру.
#         harvest = bushes[i] + bushes[(i + 1) % n] + bushes[(i - 1) % n]
#         max_berries = max(max_berries, harvest)
    
#     return max_berries

# # Пример использования функции:
# bushes = [5, 8, 1, 4]
# print(find_max_berries(bushes))  # Выведет 9, что соответствует условию задачи.

# N = int(input('Введите количество кустов через запятую: '))
# a = list(map(int, input().split()))

# # Шаг 2: Создаем массив для хранения количества ягод на каждом кусте
# total_berries = [0]  *  (N + 1)

# # Шаг 3: Заполняем массив total_berries суммой ягод на каждом кусте
# for i in range(1, N + 1):
#     total_berries[i] = total_berries[i - 1] + a[i - 1]

# # Шаг 4: Находим максимальный элемент в массиве total_berries
# max_berries = max(total_berries)

# print(max_berries)

# N = int(input('Введите количество кустов через запятую: '))
# a = list(map(int, input().split()))

# total_berries = [0] * (N + 1)

# for i in range(1, N + 1):
#     total_berries[i] = total_berries[i - 1] + a[i - 1]

# max_berries = max(total_berries)
# print(max_berries)