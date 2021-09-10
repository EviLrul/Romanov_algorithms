# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
rnd_array = []
itog_list = []

for z in range(10):
    rnd_array.append(randint(1, 50))

print('Исходный массив:', rnd_array)
itog_list = sorted(rnd_array)
print('Два наименьших элемента из массива это', itog_list[0], 'и', itog_list[1])
