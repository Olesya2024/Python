# def f(x):
#     return x
# print(f(5))

# def f(x):
#     return x
# print(f(5))

# f1 = lambda x: x # lambda функция не вызывается то есть скобки не открываем
# print(f1(5))
# print((lambda x:x)(5)) 

# num = '1 2 3 4 5'.split()
# print(num)

# num = '1 2 3 4 5'.split()
# num1 = list(map(int,num))
# print(num1)

# num = '1 2 3 4 5'.split()
# num1 = list(map(lambda x:int(x),num))
# print(num1)

# num1 = list(map(lambda x: x*2,num1))
# print(num1)

# num1 =list(filter(lambda x: x%5==0,num1))
# print(num1)

# num1 =list(filter(lambda x: 100,num1))
# print(num1)

# num1 =list(filter(int,num1))
# print(num1)

# Задача №47. Решение в группах
# У вас есть код, который вы не можете менять (так часто бывает, когда код в глубине
# программы используется множество раз и вы не хотите ничего сломать):
# transformation = <???>
# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29] # или любой другой список
# transormed_values = list(map(transformation, values))
# Единственный способ вашего взаимодействия с этим кодом - посредством задания
# функции transformation.
# Однако вы поняли, что для вашей текущей задачи вам не нужно никак преобразовывать
# список значений, а нужно получить его как есть.
# Напишите такое лямбда-выражение transformation, чтобы transformed_values получился
# копией values.

# Ввод:
# values = [1, 23, 42, ‘asdfg’]
# transformed_values = list(map(trasformation, values))
# if values == transformed_values:
#  print(‘ok’)
# else:
#  print(‘fail’)
# Вывод:
# ok

# values = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
# transformation = lambda x: x
# values = [1, 23, 42, 'asdfg']

# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')
    
# Задача №49. Решение в группах
# Планеты вращаются вокруг звезд по эллиптическим орбитам.
# Назовем самой далекой планетой ту, орбита которой имеет
# самую большую площадь. Напишите функцию
# find_farthest_orbit(list_of_orbits), которая среди списка орбит
# планет найдет ту, по которой вращается самая далекая
# планета. Круговые орбиты не учитывайте: вы знаете, что у
# вашей звезды таких планет нет, зато искусственные спутники
# были были запущены на круговые орбиты. Результатом
# функции должен быть кортеж, содержащий длины полуосей
# эллипса орбиты самой далекой планеты. Каждая орбита
# представляет из себя кортеж из пары чисел - полуосей ее
# эллипса. Площадь эллипса вычисляется по формуле S = pi*a*b,
# где a и b - длины полуосей эллипса. При решении задачи
# используйте списочные выражения. Подсказка: проще всего
# будет найти эллипс в два шага: сначала вычислить самую
# большую площадь эллипса, а затем найти и сам эллипс,
# имеющий такую площадь. Гарантируется, что самая далекая
# планета ровно одна
# Ввод:
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))
# Вывод:
# 2.5 10

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# sqare = [(i[0]*i[1]) for i in orbits if i[0]!=i[1]]
# max_orbits = [(i[0], i[1]) for i in orbits if i[0]==max(sqare)/i[1]]

# print(*max_orbits)

# import math

# find_farthest_orbit = lambda orbits: max((orbit for orbit in orbits if orbit[0] != orbit[1]), key=lambda ab: math.pi * ab[0] * ab[1])

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# print(*find_farthest_orbit(orbits))

# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
## #print(*max([orbit for orbit in orbits if orbit[0] != orbit[1]], key=lambda x: x[0] * x[1]))
# print(*max(orbits, key=lambda x: x[0] * x[1]*(x[0] != x[1])))


# Задача 36: Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6),
# которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и
# столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы,
# которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте,
# почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой
# ровно два аргумента, как, например, у операции умножения.
# Ввод: 
# print_operation_table(lambda x, y: x * y)

# вывод:
# 1  2  3  4  5  6
# 2  4  6  8 10 12
# 3  6  9 12 15 18
# 4  8 12 16 20 24
# 5 10 15 20 25 30
# 6 12 18 24 30 36 

# def print_operation_table(operation, num_rows=6, num_columns=6):
#     for i in range(1, num_rows + 1):
#         print(" ".join(f"{operation(i, j):3}" for j in range(1, num_columns + 1)))

# print_operation_table(lambda x, y: x * y)

# def print_operation_table(operation, num_rows=9, num_columns=9):
#     if num_rows < 2 or num_columns < 2:
#         print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#         return
    
#     for i in range(1, num_rows + 1):
#         row = []
#         for j in range(1, num_columns + 1):
#             row.append(str(operation(i, j)))
#         print(" ".join(row))

# print_operation_table(lambda x, y: x * y, 2, 2)      
# print_operation_table(lambda x, y: x + y, 4, 4)
# print_operation_table(lambda x, y: x - y, 5, 5)
# print_operation_table(lambda x, y: x * y, 1, 2)
# print_operation_table(lambda x, y: x / y, 4, 4)
# print_operation_table(lambda x, y: x * y, 3, 3)

        

# Винни-Пух попросил Вас посмотреть, есть ли в его стихах ритм. Поскольку разобраться в его кричалках не настолько просто, насколько легко он их придумывает, Вам стоит написать программу.

# Винни-Пух считает, что ритм есть, если число слогов (т.е. число гласных букв) в каждой фразе стихотворения одинаковое.
# Фраза может состоять из одного слова, если во фразе несколько слов, то они разделяются дефисами.
# Фразы отделяются друг от друга пробелами.

# Стихотворение  Винни-Пух передаст вам автоматически в переменную stroka в виде строки. В ответе напишите Парам пам-пам, если с ритмом все в порядке и Пам парам, если с ритмом все не в порядке.
# Если фраза только одна, то ритм определить не получится и необходимо вывести: Количество фраз должно быть больше одной!.

# Пример
# На входе:

# stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'
# # На выходе:
# # Парам пам-пам

# stroka = 'Пух'
# # # stroka = 'по-русски говорят'
# # stroka = 'мо-локо и мёд'
# # # stroka = 'как ве-тер сме-ёт лис-ти'
# # # stroka = 'за-гад-ка-ра-свет-ка-ра-газ-да-не-на-ма-ли-ва-ла'
# # # stroka = 'со-лнце-гре-ет ве-сной'
# # # stroka = 'Пух'
# # # stroka = 'пара-ра-рам рам-пам-папам па-ра-па-дам'

# def count_vowels(word):
#     vowels = "аеёиоуыэюя"
#     return sum(1 for char in word if char in vowels)

# def check_rhythm(stroka):
#     phrases = stroka.split()
    
#     if len(phrases) < 2:
#         return "Количество фраз должно быть больше одной!"
    
#     syllables_count = [sum(count_vowels(word) for word in phrase.split('-')) for phrase in phrases]
    
#     if all(count == syllables_count[0] for count in syllables_count):
#         return "Парам пам-пам"
#     else:
#         return "Пам парам"

# print(check_rhythm(stroka))

