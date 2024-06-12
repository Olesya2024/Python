# ; Задача 1
# ; Монетки

# ; На столе лежат n монеток. Некоторые из монеток лежат вверх решкой, а некоторые – гербом. 
# ; Ваша задача - определить минимальное количество монеток, которые нужно перевернуть, 
# ; чтобы все монетки лежали одной и той же стороной вверх.


# Создаем список монет, где 0 означает, что монета лежит гербом вверх, а 1 означает, что монета лежит решкой вверх
coins = [1, 1, 1, 1, 0]

# Инициализируем два счетчика:
count_zero = 0  # для подсчета монет, лежащих гербом вверх
count_one = 0  # для подсчета монет, лежащих решкой вверх

for coin in coins:  # Проходим по всем монетам в списке coins.
    if coin == 0:  # Если монета лежит гербом вверх,
        count_zero += 1  # увеличиваем count_zero
    else:  # Иначе монета лежит решкой вверх (coin != 0),
        count_one += 1  # увеличиваем count_one

# Сравниваем количество монет, лежащих решкой вверх, и количество монет, лежащих гербом вверх.
# Чтобы все монеты лежали одной стороной вверх, нужно перевернуть минимальное количество монет.
# Если монет, лежащих решкой вверх, больше, чем монет, лежащих гербом вверх,
# нужно перевернуть все монеты, лежащие гербом вверх, и вывести count_zero.
if count_one > count_zero:
    print(count_zero)
# В противном случае, нужно перевернуть все монеты, лежащие решкой вверх, и вывести count_one.
else:
    print(count_one)
