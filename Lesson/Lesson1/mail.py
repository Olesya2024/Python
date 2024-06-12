# print('введите первое число: ')
# a = int(input())
# b = int(input('введите второе число: '))

# print(a, ' + ', b, ' = ', a + b)

# a = 5.89956
# b = 6.556551
# print(round(a*b, 3))

# iter = 2
# iter += 3 # iter = iter + 3
# iter -= 4
# iter *= 5
# iter /= 5
# iter //= 5
# iter %= 5
# iter **= 5

# a = 1 > 4
# print(a)
# a = 1 < 4 and 5 > 2
# print(a)
# a = 1 == 2
# print(a)
# a = 1 != 2  #не равно
# print(a)
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = 1 < 3 < 5 < 10
# print(a)

# if condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# else:
#     # operator n + 1
#     # operator n + 2
#     # ...
#     # operator n + m

# a = int(input(“a = “))
# b = int(input(“b = “))
# if a > b:
# print(a)
# else:
# print(b)

# if condition1:
#     # operator
# elif condition2:
#     # operator
# elif condition3:
#     # operator
# else:
#     # operator

# username = input('Введите имя: ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала Вас, Марина!')
# elif username == 'Ильнар':
#     print('Ильнар - топ)')
# else:
#     print('Привет, ', username)

# if condition1 and condition2: # выполнится, когда оба условия окажутся верными
#     # operator
# if condition3 or condition4: # выполнится, когда хотя бы одно из условий
# окажется верным
#     # operator

# n = int(input())
# if n % 2 == 0 and n % 3 == 0:
#     print('Число кратно 6')
# if n % 5 == 0 and n % 3 == 0:
#     print('Число кратно 15')

# while condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n

# n = 423
# summa = 0
# while n > 0:
#       x = n % 10
#       summa = summa + x
#       n = n // 10
# print(summa) # 9

# while condition:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# else:
#     # operator n + 1
#     # operator n + 2
#     # ...
#     # operator n + m

# i = 0
# # while i < 5:
# #     if i == 3:
# #         break
#     i = i + 1
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(i)

# n = 423
# summa = 0
# while n > 0:
#     x = n % 10
#     summa = summa + x
#     n = n // 10
# else:
#     print('Пожалуй')
#     print('хватит )')
# print(summa)
# # Пожалуй
# # хватит )
# # 9

# n = int(input())
# flag = True
# i = 2
# while flag:
#     if n % i == 0: # если остаток при делении числа n на i равен 0
#         flag = False
#         print(i)
#     elif i > n // 2: # делить числа не может превышать введенное число, деленное на 2
#         print(n)
#         flag = False
#     i += 1

# for i in enumeration:
#     # operator 1
#     # operator 2
#     # ...
#     # operator n
# for i in 1, -2, 3, 14, 5:
#     print(i)
# # 1 -2 3 15 5

# r = range(5) # 0 1 2 3 4
# r = range(2, 5) # 2 3 4
# r = range(-5, 0) # ----
# r = range(1, 10, 2) # 1 3 5 7 9
# r = range(100, 0, -20) # 100 80 60 40 20
# r = range(100, 0, -20) # range(100, 0, -20)
# for i in r:
#     print(i)
# # 100 80 60 40 20

# for i in range(5):
#     print(i)
# # 0 1 2 3 4

# for i in 'qwerty':
#     print(i)
# # q
# # w
# # e
# # r
# # t
# # y

# line = ""
# for i in range(5):
#     line = ""
#     for j in range(5):
#         line += "*"
#     print(line)

# text = 'СъЕШЬ ещё этих МяГкИх французских булок'
# print(len(text)) # 39
# print('ещё' in text) # True
# print(text.lower()) # съешь ещё этих мягких французских булок
# print(text.upper()) # СЪЕШЬ ЕЩЁ ЭТИХ МЯГКИХ ФРАНЦУЗСКИХ БУЛОК
# print(text.replace('ещё','ЕЩЁ')) # СъЕШЬ ЕЩЁ этих МяГкИх французских булок

# text = 'съешь ещё этих мягких французских булок'
# print(text[0]) # c
# print(text[1]) # ъ
# print(text[len(text)-1]) # к
# print(text[-5]) # б
# print(text[:]) # съешь ещё этих мягких французских булок
# print(text[:2]) # съ
# print(text[len(text)-2:]) # ок
# print(text[2:9]) # ешь ещё
# print(text[6:-18]) # ещё этих мягких
# print(text[0:len(text):6]) # сеикакл
# print(text[::6]) # сеикакл
# text = text[2:9] + text[-5] + text[:2] # ...
# print(text)





