# 3. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

from random import randint
rnd_array = []

for i in range(10):
    rnd_array.append(randint(1, 50))

print('Максимальное значение:', max(rnd_array), 'на месте', rnd_array.index(max(rnd_array)))
print('Минимальное значение:', min(rnd_array), 'на месте', rnd_array.index(min(rnd_array)))
print('Исходный массив:', rnd_array)

meaning_max = max(rnd_array)
index_max = rnd_array.index(max(rnd_array))
meaning_min = min(rnd_array)
index_min = rnd_array.index(min(rnd_array))

rnd_array.pop(index_max)
rnd_array.insert(index_max, meaning_min)
rnd_array.pop(index_min)
rnd_array.insert(index_min, meaning_max)

print('Конечный массив:', rnd_array)
