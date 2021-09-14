# 1. Проанализировать скорость и сложность одного любого алгоритма,
# разработанных в рамках домашнего задания первых трех уроков.
# Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.

from random import randint
import time


def solution1():                                                      # Мой код
    rnd_array = []
    itog_list = []
    for z in range(500000):
        rnd_array.append(randint(1, 20))
    # print('Исходный массив', rnd_array)
    for i in range(len(rnd_array)):
        if rnd_array[i] % 2 == 0:
            itog_list.append(i + 1)
    # print('Индексы чётных значений из исходного массива:', itog_list)


def solution2():                                                      # Ваш код
    init_list = [randint(0, 100) for _ in range(500000)]
    a = [i for i, item in enumerate(init_list) if item % 2 == 0]
    # print('\n\n', init_list, a)


start_time = time.time()
solution1()
print(time.time() - start_time)
start_time = time.time()
solution2()
print(time.time() - start_time)

"""
Решил проанализировать свой код и взятый у Вас с урока.
при малых значениях range(), иногда по времене выигрывал то мой то Ваш код
(наверное взависимости от параллельных задач компа)
При больших же значения однозначно по времени выйирывал Ваш код
к примеру при range(500000), результаты были 0.4040231704711914, 0.36802124977111816
"""