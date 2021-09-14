# 2. Написать два алгоритма нахождения i-го по счёту простого числа.
# Без использования «Решета Эратосфена»;
# Используя алгоритм «Решето Эратосфена»

# Вариант исследования 2

import cProfile


def kod1():
    n = int(input("Для рения без использования «Решета Эратосфена» введи n="))
    lst = [2]
    for i in range(3, n + 1, 2):
        if (i > 10) and (i % 10 == 5):
            continue
        for j in lst:
            if j * j - 1 > i:
                lst.append(i)
                break
            if i % j == 0:
                break
        else:
            lst.append(i)


def kod2():
    n = int(input('Для решения используя алгоритм «Решето Эратосфена» введите n='))
    a = []
    for i in range(n + 1):
        a.append(i)
    a[1] = 0
    i = 2
    while i <= n:
        if a[i] != 0:
            j = i + i
            while j <= n:
                a[j] = 0
                j = j + i
        i += 1
    a = set(a)
    a.remove(0)


def main():
    kod1()
    kod2()


cProfile.run('main()')


"""
для значения n=1000000 получили следующие итоги:
   Ordered by: standard name

   ncalls  tottime  percall  cumtime  percall filename:lineno(function)
        1    0.511    0.511    2.779    2.779 2.py:23(kod2)
        1    0.007    0.007   10.025   10.025 2.py:41(main)
        1    1.400    1.400    7.240    7.240 2.py:7(kod1)
        1    0.000    0.000   10.025   10.025 <string>:1(<module>)
        2    0.000    0.000    0.000    0.000 codecs.py:319(decode)
        2    0.000    0.000    0.000    0.000 codecs.py:331(getstate)
        2    0.000    0.000    0.000    0.000 {built-in method _codecs.utf_8_decode}
        1    0.000    0.000   10.026   10.026 {built-in method builtins.exec}
        2    8.009    4.005    8.009    4.005 {built-in method builtins.input}
  1078498    0.098    0.000    0.098    0.000 {method 'append' of 'list' objects}
        1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
        1    0.000    0.000    0.000    0.000 {method 'remove' of 'set' objects}
        
cumtime – совокупное время, потраченное как в данной функции, так и наследуемых функциях.
где видно: 
на main потрачено - 10.025
на kod1 (без использования «Решета Эратосфена») потрачено - 7.240
на kod2 (используя алгоритм «Решето Эратосфена») потрачено - 2.779
"""

# Вариант исследования 1

# import time
#
# n = int(input("Для рения без использования «Решета Эратосфена» введи n="))
# start_time = time.time()
# lst = [2]
# for i in range(3, n + 1, 2):
#     if (i > 10) and (i % 10 == 5):
#         continue
#     for j in lst:
#         if j * j - 1 > i:
#             lst.append(i)
#             break
#         if i % j == 0:
#             break
#     else:
#         lst.append(i)
# print('Время выполнения', time.time() - start_time)
#
#
# n = int(input('Для решения используя алгоритм «Решето Эратосфена» введите n='))
# start_time = time.time()
# a = []
# for i in range(n + 1):
#     a.append(i)
# a[1] = 0
# i = 2
# while i <= n:
#     if a[i] != 0:
#         j = i + i
#         while j <= n:
#             a[j] = 0
#             j = j + i
#     i += 1
# a = set(a)
# a.remove(0)
# print('Время выполнения', time.time() - start_time)


"""
итоги для варианта 1 получились следующими:

Для рения без использования «Решета Эратосфена» введи n=1000000
Время выполнения 2.168123960494995

Для решения используя алгоритм «Решето Эратосфена» введите n=1000000
Время выполнения 0.7780444622039795

во втором случае значительное увеличение по времени.
"""