# 5. В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию в массиве.

from random import randint
rnd_array = []

for i in range(5):
    rnd_array.append(randint(1, 100) * - 1)

print('Исходный массив:', rnd_array)
print('Максимальный отрицательный элемент', min(rnd_array), 'его позиция', rnd_array.index(min(rnd_array)))
