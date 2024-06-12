# БЛИЖАЙЩИЙ ЭЛЕМЕНТ В МАССИВЕ
# Требуется найти в массиве list_1 самый близкий по значению элемент к заданному числу k и вывести его.
# Считать, что такой элемент может быть только один. Если значение k совпадает с этим элементом - выведите его.
# Пример:
# list_1 = [1, 2, 3, 4, 5]
# k = 6
# 5

list_1 = [1, 2, 3, 4, 5]
k = 6

e = abs(k - list_1[0]) 
number = list_1[0]
for i in range(1, len(list_1)):
    if e > abs(list_1[i] - k): 
        e = abs(list_1[i] - k) 
        number = list_1[i] 
print(number) 


# list_1 = [1, 2, 3, 4, 5]
# k = 6
# def find_closest_element(list_1, k):
#     differences = [abs(i - k) for i in list_1]
    
#     closest_index = differences.index(min(differences))
#     return list_1[closest_index]
# closest_element = find_closest_element(list_1, k)
# print(f"{closest_element}")