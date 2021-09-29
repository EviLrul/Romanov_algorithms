# 1. Определение количества различных подстрок с использованием хэш-функции.
# Пусть дана строка S длиной N, состоящая только из маленьких латинских букв.
# Требуется найти количество различных подстрок в этой строке.

import hashlib

summ = []
phrase = input('Введите фразу: ')

for k in range(len(phrase) - 1):      # -1 чтоб не прибавлялась исходная строка как подстрока
    for i in range(len(phrase)):
        substring = phrase[i: k + i + 1]
        substring_hex = hashlib.sha1(substring.encode()).hexdigest()
        for j in range(len(phrase)):
            line = phrase[j: k + j + 1]
            line_hex = hashlib.sha1(line.encode()).hexdigest()
            if substring_hex == line_hex:
                summ.append(line)

print('Входит', len(set(summ)), 'подстрок(и) в исходную строку')

# Алгоритм конечно сыроват, но работает ))
# Старался успеть к сдаче в сроки
