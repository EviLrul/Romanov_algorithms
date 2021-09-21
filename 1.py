# 1. Подсчитать, сколько было выделено памяти под переменные в ранее
# разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

"""
хм )))
сперва хотел использовать метод __sizeof__ для определения памяти, но...

getsizeof() вызывает метод __sizeof__ объекта и добавляет дополнительные накладные расходы
сборщика мусора, если объект управляется сборщиком мусора.
(https://coderoad.ru/449560/%D0%9A%D0%B0%D0%BA-%D0%BE%D0%BF%D1%80%D0%B5%D0%B4%D0%B5%D0%BB%D0%B8%D1%82%D1%8C-%D1%80%D0%B0%D0%B7%D0%BC%D0%B5%D1%80-%D0%BE%D0%B1%D1%8A%D0%B5%D0%BA%D1%82%D0%B0-%D0%B2-Python)

Обычно вы не вызываете __sizeof__() вы оставляете это для функции sys.getsizeof() ,
которая также добавляет служебные данные сборщика мусора.
(http://www.rupython.com/python-__sizeof-__-22020.html)

т.е. всё же, видимо, для ислледования более правильно будет использовать getsizeof()
т.к. нас будут интересовать более полные данные по занимаемой памяти
(т.е. в том числе и память на garbage collector)
"""

import sys
# 7. В одномерном массиве целых чисел определить два наименьших элемента.
# Они могут быть как равны между собой (оба являться минимальными), так и различаться.

from random import randint
rnd_array = []
print(sys.getsizeof(rnd_array), 'байт размер пустого списка')
itog_list = []
print(sys.getsizeof(itog_list), 'байт размер пустого списка')

for z in range(10):
    print(sys.getsizeof(z), 'Объём памяти счётчика(ссылки на память) z')
    print(z, '-', id(sys.getsizeof(z)))
    rnd_array.append(randint(1, 50))
    print(sys.getsizeof(rnd_array), 'байт занимает список, добавлено', z + 1, 'значение в список')
    print(rnd_array[z], '-', id(rnd_array[z]))

print('Исходный массив:', rnd_array)
itog_list = sorted(rnd_array)
print(sys.getsizeof(itog_list))
print('Два наименьших элемента из массива это', itog_list[0], 'и', itog_list[1])

"""
Листинг выдал следующее:

56 байт размер пустого списка
56 байт размер пустого списка
24 Объём памяти счётчика(ссылки на память) z
0 - 8790870460816
88 байт занимает список, добавлено 1 значение в список
21 - 8790870460720
28 Объём памяти счётчика(ссылки на память) z
1 - 8790870460944
88 байт занимает список, добавлено 2 значение в список
31 - 8790870461040
28 Объём памяти счётчика(ссылки на память) z
2 - 8790870460944
88 байт занимает список, добавлено 3 значение в список
33 - 8790870461104
28 Объём памяти счётчика(ссылки на память) z
3 - 8790870460944
88 байт занимает список, добавлено 4 значение в список
44 - 8790870461456
28 Объём памяти счётчика(ссылки на память) z
4 - 8790870460944
120 байт занимает список, добавлено 5 значение в список
45 - 8790870461488
28 Объём памяти счётчика(ссылки на память) z
5 - 8790870460944
120 байт занимает список, добавлено 6 значение в список
30 - 8790870461008
28 Объём памяти счётчика(ссылки на память) z
6 - 8790870460944
120 байт занимает список, добавлено 7 значение в список
48 - 8790870461584
28 Объём памяти счётчика(ссылки на память) z
7 - 8790870460944
120 байт занимает список, добавлено 8 значение в список
16 - 8790870460560
28 Объём памяти счётчика(ссылки на память) z
8 - 8790870460944
184 байт занимает список, добавлено 9 значение в список
43 - 8790870461424
28 Объём памяти счётчика(ссылки на память) z
9 - 8790870460944
184 байт занимает список, добавлено 10 значение в список
7 - 8790870460272
Исходный массив: [21, 31, 33, 44, 45, 30, 48, 16, 43, 7]
192
Два наименьших элемента из массива это 7 и 16
192

Итог:
сумма памияти будет складываться я считаю из
184 первичного списка rnd_array
192 итогового списка сортированного(кстати поулчается для
    сортированного списка нужно в данном случае на 8 байт больше) itog_list
28 байт для цикла(сыллок на обекты) z
--------------
CPython хранит глобальный список всех целых чисел в диапазоне [-5, 256].
Эта стратегия оптимизации имеет смысл, потому что маленькие целые числа всплывают повсюду,
и, учитывая, что каждое целое число занимает 24 байта, оно экономит много памяти для типичной программы.
Это также означает, что CPython предварительно выделяет 266 * 24 = 6384 байта для всех этих целых чисел,
даже если вы не используете большинство из них. 
https://code.tutsplus.com/ru/tutorials/understand-how-much-memory-your-python-objects-use--cms-25609
--------------
6384 для цикла, для использования самих объктов простых
    числе, что нам показывают ссылки 8 - 8790870460944, 9 - 8790870460944
    т.е. 1, 2, 3..9 всё сылается на один объект памяти, хотя...
24 байта получается нужно для объекта 0 для цикла т.к. 0 имеет другую ссылку почему-то
    0 - 8790870460816
28 * 10 байта заложим для каждого объекта лежащего в списке...
    !!! а вот тут для меня странно, по лекции я понял что Python должен сейчас ссылаться
    на блок памяти 8790870460944 т.к. в моей проге рандомятся числа от 1 до 50, что должно входить
    в промежуток [-5..255]. а они имеют все свои адреса памяти: 43 - 8790870461424, 16 - 8790870460560
    хотя здесь возможно играет роль именно рандом...
будем считать, что сортированный список тоже будет иметь объекты от первого,
поэтому для второго списка не будем закладывать память для объектов.
в общем должно получиться
184+192+28+6384+24+(28*10)=7092 байт
если ничего не упустил
"""