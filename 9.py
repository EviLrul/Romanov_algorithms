# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.

from random import randint

a = []
max_list = []

for i in range(4):
    b = []
    for j in range(5):
        if j == 4:
            max_list.append(max(b))
        else:
            n = int(randint(1, 99))
            b.append(n)
            print('%4d' % n, end='')
    print()
    a.append(b)
print()
print('Максимальный элемент матрицы:', max(max_list))
