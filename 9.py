# 9. Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
# Вывести на экран это число и сумму его цифр.

from random import randint
list_rnd = []
list_sums = []
item_amount = 0

for i in range(10):
    rnd_data = randint(0, 5)                        # Такой рандом сделан для больших вариаций
    if rnd_data == 0:                               # по разрядности самих чисел
        list_rnd.append(str(randint(0, 10)))
    elif rnd_data == 1:
        list_rnd.append(str(randint(10, 100)))
    elif rnd_data == 2:
        list_rnd.append(str(randint(100, 1000)))
    elif rnd_data == 3:
        list_rnd.append(str(randint(1000, 10000)))
    elif rnd_data == 4:
        list_rnd.append(str(randint(10000, 100000)))
    elif rnd_data == 5:
        list_rnd.append(str(randint(100000, 1000000)))

    for y in range(len(list_rnd[i])):
        item_amount = int(list_rnd[i][y]) + item_amount
    list_sums.append(item_amount)
    item_amount = 0

print('Список рандомных чисел\n', list_rnd)
print('\nСписок сумм цифр этих чисел\n', list_sums)
print('\nМаксимальная сумма цифр', max(list_sums), 'для числа', list_rnd[list_sums.index(max(list_sums))])

