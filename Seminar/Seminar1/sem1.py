# введите два числа и определите большее
# firstn = input('first")
# secn = int(input('sec'))
# print(type(firstn),type(secn))

# firstn = 5
# secn = 5
# print(type(firstn),type(secn))

# firstn = input('first")
# secn = int(input('sec'))
# print(max(first, secn))

# firstn = 5
# secn = 5
# if firstn > secn:
#     print(firstn)
# else:
#     print(secn)
    
# firstn = 5
# secn = 5    
# print(firstn > secn)
#  if True:
#     print(firstn)
# else:
#     print(secn)   
 
# firstn = 500
# secn = 5000000      
# print(firstn > secn)
#  if 555:
#     print(firstn)
# else:
#     print(secn)      
   
# firstn = 500
# secn = 5000000      
# print(100+(30>8))
# print(firstn > secn)

#  if firstn > secn:
#     print(firstn)
# else:
#     print(secn)  

# firstn = 500
# secn = 5000000      

# if firstn > secn:
#     print(firstn)
# else:
#     print(secn)  
# if firstn == secn:
#         print("=")


# это правильно
# firstn = 500
# secn = 500   
# if firstn == secn:
#         print("=")
# elif firstn > secn:
#     print(firstn)
# else:
#     print(secn)  


# print(18/8)

# 18               15
#         // 8
# 2                2
# ответ 2 (выбирает меньшее число)

# 10               15
#         // -5
# 2                -3
# ответ -3 (выбирает меньшее число)

# кратность число ответ 0, если не равен 0 тогда кратно
# print(32 % 8) 
# print(24 % 8) 

# print(3 % 9)  целочисленное число меньшее слева всегда и будет ответ 

# Задача 1
# За день машина проезжает n километров. Сколько
# дней нужно, чтобы проехать маршрут длиной m
# километров? При решении этой задачи нельзя
# пользоваться условной инструкцией if и циклами.

# Input:
# n = 700
# m = 750
# Output:
# 2

# n = 700
# m = 750
# правильно
# days = (m + n -1) // n  
# print(days)

# другой вариант решения
# # days = abs(-m // n)  
# # print(days)

# Задача 2
# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.
# Input: 20 21 22(ввод чисел НЕ в одну строку)
# Output: 32

# правильное решение
# a = int(input('Введите первое число: '))
# b = int(input('Введите второе число: '))
# c = int(input('Введите третье число: '))

# s1=((a+1)//2)
# s2=(b//2+(b%2!=0))
# s3=abs(-c//2)
# print(s1+s2+s3)

# другое решение
# a, b, c = 20, 21, 22
# students = a + b + c
# print(-(-students//2))