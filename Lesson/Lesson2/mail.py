# Списки
##Список - это упорядоченный конечный набор элементов. Давайте
#разбираться, по сути список - это тот же самый массив, в котором
#можно хранить элементы любых типов данных.
# list_1 = [] # Создание пустого списка
# list_2 = list() # Создание пустого списка
# list_1 = [7, 9, 11, 13, 15, 17] # есть какие то значения
# print(*list_1) # если ставить * все скобочки все запятые уходят

# list_1 = [7, 9, 11, 13, 15, 17] 
# for i in list_1:
#     print(i)

# list_1 = [1, 2, 3, 8] 
#print(len(list_1)) #узнаем размер нашего списка 4

#В списках существует нумерация, которая начинается с 0, чтобы
#вывести первый элемент списка воспользуемся следующей
#конструкцией:
#list_1 = [7, 9, 11, 13, 15, 17]
#print(list_1[0]) # 7
#print(list_1[-2]) # 15

#добавляем значения в список
#list_1 = [1, 5] 
#print (list_1)
#list_1.append(8) #в скобочках значение которое хотим добавить
#print (list_1) #[1, 5, 8]
#list_1.append(85) #в скобочках еще значение которое хотим добавить
#print (list_1) #[1, 5, 8, 85]


# list_1 = [] # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
#     list_1.append(i) # сохранение элемента в конец списка
#     print(list_1)

# list_1 = list() # создание пустого списка
# for i in range(5): # цикл выполнится 5 раз
#     n = int(input()) # пользователь вводит целое число
#     list_1.append(n) # сохранение элемента в конец списка
# # 1-я итерация цикла(повторение 1): n = 12, list_1 = [12]
# # 2-я итерация цикла(повторение 2): n = 7, list_1 = [12, 7]
# # 3-я итерация цикла(повторение 3): n = -1, list_1 = [12, 7, -1]
# # 4-я итерация цикла(повторение 4): n = 21, list_1 = [12, 7, -1, 21]
# # 5-я итерация цикла(повторение 5): n = 0, list_1 = [12, 7, -1, 21, 0]
# print(list_1) # [12, 7, -1, 21, 0]

# len(имя_списка):
# list_1 = [7, 9, 11, 13, 15, 17]
# print(len(list_1)) # 6


# for со списком:
# list_1 = [12, 7, -1, 21, 0]
# for i in list_1:
#     print(i) # вывод каждого элемента списка
# # 1-я итерация цикла(повторение 1): i = 12
# # 2-я итерация цикла(повторение 2): i = 7
# # 3-я итерация цикла(повторение 3): i = -1
# # 4-я итерация цикла(повторение 4): i = 21
# # 5-я итерация цикла(повторение 5): i = 0 

# list_1 = [12, 7, -1, 21, 0]
# for i in range(len(list_1)):
#     print(list_1[i]) # вывод каждого элемента списка
# # 1-я итерация цикла(повторение 1): list_1[0] = 12
# # 2-я итерация цикла(повторение 2): list_1[1] = 7
# # 3-я итерация цикла(повторение 3): list_1[2] = -1
# # 4-я итерация цикла(повторение 4): list_1[3] = 21
# # 5-я итерация цикла(повторение 5): list_1[4] = 0

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop()) # 0
# print(list_1) # [12, 7, -1, 21]
# print(list_1.pop()) # 21
# print(list_1) # [12, 7, -1]
# print(list_1.pop()) # -1
# print(list_1) # [12, 7]

# list_1 = [12, 7, -1, 21, 0]
# print(list_1.pop(0)) # 12
# print(list_1) # [7, -1, 21, 0]

# list_1 = [12, 7, -1, 21, 0]
# print(list1.insert(2, 11))
# print(list1) # [12, 7, 11, -1, 21, 0]

# list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[0]) # 1
# print(list_1[1]) # 2
# print(list_1[len(list_1)-1]) # 10
# print(list_1[-5]) # 6
# print(list_1[:]) # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# print(list_1[:2]) # [1, 2]
# print(list_1[len(list_1)-2:]) #[9, 10]
# print(list_1[2:9]) # [3, 4, 5, 6, 7, 8, 9]
# print(list_1[6:-18]) # []
# print(list_1[0:len(list_1):6]) # [1, 7]
# print(list_1[::6]) # [1, 7]

# Кортежи

# t = () # создание пустого кортежа
# print(type(t)) # class <'tuple'>
# t = (1,)
# print(type(t))
# t = (1)
# print(type(t))
# t = (28, 9, 1990)
# print(type(t))
# colors = ['red', 'green', 'blue']
# print(colors) # ['red', 'green', 'blue']
# t = tuple(colors)
# print(t) # ('red', 'green', 'blue')
# t = tuple(['red', 'green', 'blue'])
# print(t[0]) # red
# print(t[2]) # blue
# for e in t:
# print(e) # red green blue
# t[0] = 'black' # TypeError: 'tuple' object does not support(нельзя изменять кортеж)

# t = tuple(['red', 'green', 'blue'])
# red, green, blue = t
# print('r:{} g:{} b:{}'.format(red, green, blue)) # r:red g:green b:blue

# Словари
# dictionary = {}
# dictionary ={'up': '↑', 'left': '←', 'down': '↓', 'right': '→'}
# print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
# print(dictionary['left']) # ←
# # типы ключей могут отличаться
# print(dictionary['up']) # ↑
# # типы ключей могут отличаться
# dictionary['left'] = '⇐'
# print(dictionary['left']) # ⇐
# print(dictionary['type']) # KeyError: 'type'
# del dictionary['left'] # удаление элемента
# for item in dictionary: # for (k,v) in dictionary.items():
# print('{}: {}'.format(item, dictionary[item]))
# # up: ↑
# # down: ↓
# # right: →

# Множества
# colors = {'red', 'green', 'blue'}
# print(colors) # {'red', 'green', 'blue'}
# colors.add('red')
# print(colors) # {'red', 'green', 'blue'}
# colors.add('gray')
# print(colors) # {'red', 'green', 'blue','gray'}
# colors.remove('red')
# print(colors) # {'green', 'blue','gray'}
# colors.remove('red') # KeyError: 'red'
# colors.discard('red') # ok
# print(colors) # {'green', 'blue','gray'}
# colors.clear() # { }
# print(colors) # set()

# a = {1, 2, 3, 5, 8}
# b = {2, 5, 8, 13, 21}
# c = a.copy() # c = {1, 2, 3, 5, 8}
# u = a.union(b) # u = {1, 2, 3, 5, 8, 13,
# i = a.intersection(b) # i = {8, 2, 5}
# dl = a.difference(b) # dl = {1, 3}
# dr = b.difference(a) # dr = {13, 21}
# q=a.union(b).difference(a.intersection(b)) # {1, 21, 3, 13}

# a = {1, 2, 3, 5, 8}
# b = frozenset(a)
# print(b) # frozenset({1, 2, 3, 5, 8})

# List Comprehension
# list_1 = [exp for item in iterable]
# list_1 = [exp for item in iterable (if conditional)]

# Задача: Создать список, состоящий из четных чисел в диапазоне от 1 до 100
# list_1 = []
# for i in range(1, 101):
# list_1.append(i)
# print(list_1) # [1, 2, 3,..., 100]

# list_1 = [i for i in range(1, 101)] # [1, 2, 3,..., 100]

# 2. Добавить условие (только чётные числа)
# list_1 = [i for i in range(1, 101) if i % 2 == 0] # [2, 4, 6,..., 100]

# list_1 = [(i, i) for i in range(1, 101) if i % 2 == 0] # [(2, 2), (4, 4),...,
# (100, 100)]

# list_1 = [i * 2 for i in range(10) if i % 2 == 0]
# print(list_1) # [0, 4, 8, 12, 16]

# Профилирование и отладка
# number_first = 5
# number_second = 7
# if number_first > number_second # !!!!!
# print(number_first)
# # Отсутствие :

# number_first = 5
# number_second = 7
# if number_first > number_second:
# print(number_first) # !!!!!
# # Отсутствие отступов

# text = 'Python'
# number = 5
# print(text + number)
# # Нельзя складывать строки и числа

# number_first = 5
# number_second = 0
# print(number_first // number_second)
# # Делить на 0 нельзя

# dictionary = {1: 'Monday', 2: 'Tuesday'}
# print(dictionary[3])
# # Такого ключа не существует

# name = 'Ivan'
# print(names)
# # Переменной names не существует

# text = 'Python'
# print(int(text))
# # Нельзя символы перевести в целые значения



