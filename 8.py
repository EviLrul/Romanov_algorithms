# 8. Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
# Программа должна вычислять сумму введенных элементов каждой строки и записывать ее в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.
from random import randint

a = []
for i in range(4):
    b = []
    for j in range(5):
        if j == 4:
            b.append(sum(b))
            print('%4d' % b[j], end='')
        else:
            n = int(randint(1, 9))
            b.append(n)
            print('%4d' % n, end='')
    print()
    a.append(b)
print()
