# 1. Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
# заданный случайными числами на промежутке [-100; 100).
# Выведите на экран исходный и отсортированный массивы.
# Сортировка должна быть реализована в виде функции.
# По возможности доработайте алгоритм (сделайте его умнее).

import random as rnd


def bubble_sort(in_arr):
    for_loop = len(in_arr) - 1
    end_flag = True
    while end_flag:
        end_flag = False
        for i in range(1, for_loop):
            if in_arr[i - 1] < in_arr[i]:
                arr[i - 1], arr[i] = arr[i], arr[i - 1]
                end_flag = True
            if in_arr[i] < in_arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                end_flag = True
    return in_arr


N = 10
arr = [(rnd.randint(-100, 99)) for _ in range(N)]
print(arr)

print(bubble_sort(arr))


