'''lambda-функции'''

# def f(x):
#     return x*x
# print(f(5))

# def f(x):
#     return x*x
# print(type(f))

# def f(x):
#     return x*x
# a = f
# print(type(f))

# def f(x):
#     return x*x
# a = f
# print(a(5))
# print(f(5))

# def calc1(a):
#     return a*a

# def calc2(a):
#     return a*a

# def math(op, x):
#     print(op(x))
    
# math(calc2, 5)

# def calc1(a, b):
#     return a + b

# def calc2(a, b):
#     return a * b

# def math(op, x, y):
#     print(op(x, y))
    
# math(calc1, 5, 10)

# def math(op, a, b):
#     print(op(a, b))
 
# math(lambda a,b: a + b, 5, 45)

# задача
# 1. В списке хранятся числа. Нужно выбрать только чётные числа и составить список пар
# (число; квадрат числа).
# Пример: 1 2 3 5 8 15 23 38
# Получить: [(2, 4), (8, 64), (38, 1444)]
# Решение:
# data = [1, 2, 3, 5, 8, 15, 23, 38]
# out = []
# for i in data :
#     if i % 2 == 0:
#         out.append((i, i ** 2))
# print(out)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = list()
# for i in data:
#     if i % 2 == 0:
#         res.append((i, i ** 2))
# print(res)       

    
# def select(f, col):
#     return [f(x) for x in col]
# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = select(int, data)
# res = where(lambda x: x % 2 == 0, res)
# # print(res) # [2, 8, 38]
# res = list(select(lambda x: (x, x ** 2), res))
# print(res)

'''Функция map'''

# list_1 = [x for x in range (1,20)]
# print(list_1)

# list_1 = list(map(lambda x: x + 10, list_1 ))
# print(list_1)

# Задача: C клавиатуры вводится некий набор чисел, в качестве разделителя используется
# пробел. Этот набор чисел будет считан в качестве строки. Как превратить list строк в list чисел?

# data = '1 2 3 5 8 15 23 38'
# print(data)

# data = '1 2 3 5 8 15 23 38'.split()
# print(data) # ['1', '2', '3', '5', '8', '15', '23', '38']

# data = '1 2 3 5 8 15 23 38'
# data = list(map(int, data.split()))
# print(data)

# def where(f, col):
#     return [x for x in col if f(x)]

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = where(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

'''Функция filter'''

# data = [15, 65, 9, 36, 175]
# res = list(filter(lambda x: x % 10 == 5, data))
# print(res)

# data = [1, 2, 3, 5, 8, 15, 23, 38]
# res = map(int, data)
# res = filter(lambda x: x % 2 == 0, res)
# res = list(map(lambda x: (x, x ** 2), res))
# print(res)

'''Функция zip'''

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# data = list(zip(users, ids))
# print(data) # [('user1', 4), ('user2', 5), ('user3', 9), ('user4', 14), ('user5', 7)]

# users = ['user1', 'user2', 'user3', 'user4', 'user5']
# ids = [4, 5, 9, 14, 7]
# salary = [111, 222, 333]
# data = list(zip(users, ids, salary))
# print(data) # [('user1', 4, 111), ('user2', 5, 222), ('user3', 333)]

'''Функция enumerate'''

# users = ['user1', 'user2', 'user3']
# data = list(enumerate(users)
# print(data) # [(0, 'user1'), (1, 'user2'), (2, 'user3))]

'''файлы'''
# - a – открытие для добавления данных.
# Позволяет дописывать что-то в имеющийся файл.
# Если вы попробуете дописать что-то в несуществующий файл, то файл будет создан
# и в него начнется запись.
# - r – открытие для чтения данных.
# Позволяет читать данные из файла.
# Если вы попробуете считать данные из файла, которого не существует, программа
# выдаст ошибку.
# - w – открытие для записи данных.
# Позволяет записывать данные и создавать файл, если его не существует.

'''Миксованные режимы:'''
# 1. w+
# Позволяет открывать файл для записи и читать из него.
# Если файла не существует, он будет создан.
# 2. r+
# Позволяет открывать файл для чтения и дописывать в него.
# Если файла не существует, программа выдаст ошибку

# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'a') # здесь указываем режим, в котором будем работать
# data.writelines(colors) # разделителей не будет
# data.close()

'''Ещё один способ записи данных в файл:'''
# with open('file.txt', 'w') as data:
#     data.write('line 1\n')
#     data.write('line 2\n')

'''Чтение данных из файла:'''
# path = 'file.txt'
# data = open('file.txt', 'r')
# for line in data:
#     print(line)
# data.close()

'''Режим w'''
# colors = ['red', 'green', 'blue']
# data = open('file.txt', 'w')
# data.writelines(colors) # разделителей не будет
# data.close()

'''Модуль os'''
# os.chdir(path) - смена текущей директории.
# import os
# os.chdir('C:/Users/79190/PycharmProjects/GB')

# os.getcwd() - текущая рабочая директория
# import os
# print(os.getcwd()) # 'C:\Users\79190\PycharmProjects\webproject'    

# os.path.basename(path) - базовое имя пути
# import os
# print(os.path.basename('C:/Users/79190/PycharmProjects/webproject/main.py')) #'main.py'

# os.path.abspath(path) - возвращает нормализованный абсолютный путь.
# import os
# print(os.path.abspath('main.py')) # 'C:/Users/79190/PycharmProjects/webproject/main.py'

'''Модуль shutil'''
# shutil.copyfile(src, dst) - копирует содержимое (но не метаданные) файла src в файл dst.
# shutil.copy(src, dst) - копирует содержимое файла src в файл или папку dst.
# shutil.rmtree(path) - Удаляет текущую директорию и все поддиректории; path должен указывать на
# директорию, а не на символическую ссылку.
