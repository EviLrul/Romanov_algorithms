# 4. Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
# Количество элементов (n) вводится с клавиатуры.

n = int(input('Сейчас найдем сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...\n Введи n: '))
number = 1
final_list = [1]

for i in range(n-1):
    number /= 2
    if i % 2 != 0:
        final_list.append(number)
    else:
        final_list.append(number * (-1))
print('\nИтоговый ряд чисел:\n', final_list)
print('\nСумма этого ряда:\n', sum(final_list))
