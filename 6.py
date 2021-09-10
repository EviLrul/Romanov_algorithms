# 6. В одномерном массиве найти сумму элементов,
# находящихся между минимальным и максимальным элементами.
# Сами минимальный и максимальный элементы в сумму не включать.

from random import randint
rnd_array = []
i = 0
for z in range(10):
    rnd_array.append(randint(1, 10))

# Вариант 2 (потом стало так)
# во втором варианте выкидываются все одинаковые MAX и MIN значения из массива
# и в итоге считается сумма оставшихся элементов

max_meaning = max(rnd_array)
min_meaning = min(rnd_array)
print(rnd_array)
print('Максимальное значение:', max(rnd_array), '\nМинимальное значение:',  min(rnd_array))

while i < len(rnd_array):
    if rnd_array[i] == max_meaning:
        rnd_array.pop(i)
        i -= 1
    elif rnd_array[i] == min_meaning:
        rnd_array.pop(i)
        i -= 1
    i += 1
print('Массив без учёта MAX и MIN элементов:', rnd_array)
print('Сумма оставшихся элементов', sum(rnd_array))


# Вариант 1 (сперва было так)
# При исследовании задачи наткнулся на подвох ))
# в массиве может быть несколько одинаковых максимальных или минимальных значений
# если же не учитывать все эти элементы, то по моему мнению будет не совсем верна сумма остальных элементов
# так как в условии задачи специально не оговорён такой случай,
# то я решаю, что будут не учитываться первые максимальное и минимальные значения

# print('Исходный массив:', rnd_array)
# print('Максимальное значение', max(rnd_array))
# rnd_array.pop(rnd_array.index(max(rnd_array)))
# print('Минимальное значение', min(rnd_array))
# rnd_array.pop(rnd_array.index(min(rnd_array)))
# print('Массив без учёта MAX и MIN элементов:', rnd_array)
# print('Сумма оставшихся элементов', sum(rnd_array))


