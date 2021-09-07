# 8. Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
# Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
from random import randint

row_length = int(input('Введите длинну цифрового ряда: '))
required_digit = int(input('Введите искомую цифру в иследуемом ряду: '))
studied_series = []
counter = 0

for i in range(row_length):
    studied_series.append(randint(0, 999))      # Для первого вариант, для второго нужно поменять 999 на 9

    if len(str(studied_series[i])) == 1:                            # Вариант 1 который ищет заданную цифру
        if studied_series[i] == required_digit:                     # в любых числах 0-1000
            counter += 1                                            # Если задана к примеру 2
    else:                                                           # 2 - найдёт
        for y in range(len(str(studied_series[i]))):                # 32 - найдёт
            if str(studied_series[i])[y] == str(required_digit):    # 732 - найдёт
                counter += 1                                        #

    # if studied_series[i] == required_digit:                       # Вариант 2 который ищет заданную цифру
    #     counter += 1                                              # в числах 0-9

print('Получившийся ряд:', studied_series)
print('Число', required_digit, 'в этом ряду встречается', counter, 'раз(а)')


