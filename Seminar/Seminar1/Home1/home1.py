# Задача 1 Сумма цифр трехзначного числа
n = 123

digit1 = n // 100  
digit2 = (n // 10) % 10
digit3 = n % 10

res = digit1 + digit2 + digit3

print(res)