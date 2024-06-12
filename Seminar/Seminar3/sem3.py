# Задача №17. Решение в группах
# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# import random

# size = int(input('введите размер списка: '))
# list_1 = []
# # # for i in range(size):
# # #     num = random.randint(-2, 5)
# # #     list_1.append(num)
# # # print(list_1)
# list_1 = [random.randint(1, 5) for i in range(size)]
# # print(list_1) 

# # #1 решение
# # print(len(set(list_1)))
# # set - функция это множества - уникальные элементы не упорядочены выводит
# # len - количество элементов, длина массива

# #2 решение
# unique = []   # создаем новый пустой список
# for num in list_1:  # перебираем элементы списка, по циклу проходим по нашему списку и добавляем
#     if num not in unique:
#         unique.append(num)
# print(len(unique))
        
# # [unique.append(num) for num in list_1 if num not in unique] 

# unique_2 = [list_1[i] for i in range(len(list_1)) if list_1[i] not in list_1[i + 1:]] 
# print(len(unique_2))

# #3 решение главное
# sp = [1, 1, 2, 0, -1, 3, 4, 4]
# count = 0
# a = list()
# for c in sp:
#     a.apend(c)
# print(len(a))

# print(len(set(sp))) #множество
# st = set() #пустое множество


# Задача №19. Решение в группах
# Дана последовательность из N целых чисел и число
# K. Необходимо сдвинуть всю последовательность
# (сдвиг - циклический) на K элементов вправо, K –
# положительное число.
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# 1 решение
# # n = [1, 2, 3, 4, 5]
# n = int(input('введите количество целых чисел: '))
# numbers = [i for i in range(1, n+1)]
# print(numbers)
# k = 3
# print(numbers[k:] + numbers[:k])
 
# 2 решение оптимально
# n = [1, 2, 3, 4, 5]  
# print(n) 
# k = int(input('введите к: '))
# k = k%len(n)
# print(k)
# for i in range(k):
#     t = n.pop()
#     n.insert(0,t)
# print(n)


# Задача создать словарь из 3 элементов
# dikt1 = {[1,2]:2,(1,2):3,"serw":[1,2]}
# print(dikt1)

# dikt1 = {(1,2):3, "[1,2]":2, "serw":[1,2]}
# print(dikt1)

# dict1 = {333:2,(1,2):3,"serw":[1,2]}
# # print(dict1)
# # for i in dict1:
# #     print(i,dict1[i])
# # for i in dict1.valies():
# #     print(i)
# for i,j in dict1.items():  
#     print(i,j) 

# Задача №21. Решение в группах
# Напишите программу для печати всех уникальных
# значений в словаре.
# Input: [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII
# ":" S007 "}]
# Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# Примечание: Список словарей задан изначально.
# Пользователь его не вводит


# dict_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": "S005"}, {"V": "S009"}, {"VIII": "S007"}]
# unique_values = set()

# for d in dict_list:
#     for value in d.values():
#         unique_values.add(value)

# print(unique_values)   
    
# dict1 = {333:2,(1,2):3,"serw":[1,2]}
# # print(dict1)
# # for i in dict1:
# #     print(i,dict1[i])
# # for i in dict1.valies():
# #     print(i)
# for i,j in dict1.items():  
#     print(i,j) 


# #3 решение главное
# sp = [1, 1, 2, 0, -1, 3, 4, 4]
# count = 0
# a = list()
# for c in sp:
#     a.apend(c)
# print(len(a))

# print(len(set(sp))) #множество
# st = set() #пустое множество


# Задача №23. Решение в группах
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)

# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
# Примечание: Пользователь может вводить значения
# списка или список задан изначально.

# arr = [0, -1, 5, 2, 3]

# count = 0
# comparisons = []

# for i in range(1, len(arr)):
#     if arr[i] > arr[i-1]:
#         comparisons.insert(i, f'{arr[i-1]} < {arr[i]}')
#         count += 1
        
# print(f"{count} ({', '.join(comparisons)})")

# Задача 16: Требуется вычислить, сколько раз встречается некоторое
# число X в массиве A[1..N]. Пользователь в первой строке вводит
# натуральное число N – количество элементов в массиве. В последующих
# строках записаны N целых чисел Ai. Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 3
# -> 1

# N = int(input("Введите натуральное число N - количество элементов в массиве: "))
# list_1 = [i for i in range(1, N + 1)] 
# i = 1
# count = len(list_1)
# # count = list_1.count(i)
# print(count)  

N = int(input("Введите натуральное число N: "))
print(N)
list_1 = [i for i in range(1, N + 1)] 
print(' '.join(map(str, list_1)))
i = 1
count = len(list_1)
k = int(input("Введите элемент в массиве: "))
count = list_1.count(k)
print("->" + str(count))

  
# Задача 18: Требуется найти в массиве A[1..N] самый близкий по
# величине элемент к заданному числу X. Пользователь в первой строке
# вводит натуральное число N – количество элементов в массиве. В
# последующих строках записаны N целых чисел Ai
# .Последняя строка содержит число X

# 5
# 1 2 3 4 5
# 6
# -> 5

