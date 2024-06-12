# def function_name(x):
# # body line 1
# # ...
# # body line n
# # optional return

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i       
#     print(summa)
         
# sumNumbers(5)

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa

# print(sumNumbers(n)) # 15

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sumNumbers(5)
# print(a) # 15

# def sumNumbers(n):
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sumNumbers(5, (str:'dddf')) #Функция sumNumbers ожидает только один аргумент/синтаксически неверный и не имеет смысла в контексте Python.
# print(a)

# def sumNumbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sumNumbers(5) 
# print(a)
  
# def sumNumbers(n, y = 'Hello'):
#     print(y)
#     summa = 0
#     for i in range(1, n + 1):
#         summa += i
#     return summa
# a = sumNumbers(5, 'qwert' ) 
# print(a) 

# def sum_str(*args):
#     res = ''
#     for i in args:
#         res += i # res += str(i)  # Преобразование i в строку перед конкатенацией
#     return res
    
# # print(sum_str('q','e','l'))
# # print(sum_str('q','e','l','r','f'))
# # print(sum_str(1, 8, 9)) # не будет работать целые числа не строковые
# print(sum_str('1', '8', '9'))

# будем импортировать модуль

# import modul1
# print(modul1.max1(5, 9))

# # или другой способ
# from modul1 import max1
# print(max1(10, 9))

# from modul1 import *
# print(max1(11, 9))

# import modul1 as m1
# print(m1.max1(10, 9))


# Рекурсия

# # фибоначи
# def fib(n):
#     if n in [1,2]: # базис обязательно
#         return 1
#     return fib(n-1) + fib(n-2)

# list_1 = []
# for i in range(1, 10):
#     list_1.append(fib(i))
# print(list_1)

# Алгоритмы

# def quick_sort(array): #quick_sort функция сортировки
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot] 
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([14,5,9,6,3,58,7,5,2,7]))

# def quick_sort(array): #quick_sort функция сортировки
#     if len(array) <= 1:
#         return array
#     else:
#         pivot = array[0]
#     less = [i for i in array[1:] if i <= pivot]
#     greater = [i for i in array[1:] if i > pivot] 
#     return quick_sort(less) + [pivot] + quick_sort(greater)

# print(quick_sort([10, 5, 2]))

# ● 1-е повторение рекурсии:
# ○ array = [10, 5, 2]
# ○ pivot = 10
# ○ less = [5, 2]
# ○ greater = []
# ○ return quicksort([5, 2]) + [10] + quicksort([])
# ● 2-е повторение рекурсии:
# ○ array = [5, 2]
# ○ pivot = 5
# ○ less = [2]
# ○ greater = []
# ○ return quicksort([2]) + [5] + quicksort([]) # Важно! Не забывайте, что
# здесь помимо вызова рекурсии добавляется список [10]
# ● 3-е повторение рекурсии:
# ○ array = [2]
# ○ return [2] # Сработал базовый случай рекурсии
# На этом работа рекурсии завершилась и итоговый список будет выглядеть таким
# образом: [2] + [5] + [10] = [2, 5, 10]

# сортировка слияния
def merge_sort(nums):
    if len(nums) > 1:
        mid = len(nums) // 2
        left = nums[:mid]
        right = nums[mid:]
        merge_sort(left)
        merge_sort(right)
        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                nums[k] = left[i]
                i += 1
            else:
                nums[k] = right[j]
                j += 1
            k += 1
        
        while i < len(left):
            nums[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            nums[k] = right[j]
            j += 1
            k += 1
list1 = [1,5,6,9,8,7,2,1,55,2,4]

merge_sort(list1)
print(list1)