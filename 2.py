# 2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50).
# Выведите на экран исходный и отсортированный массивы.

import random as rnd


def bubble_sort(in_arr):
    end_flag = True
    while end_flag:
        end_flag = False
        for i in range(
                len(in_arr) - 1):
            if in_arr[i] > in_arr[i + 1]:
                tmp = in_arr[i]
                in_arr[i] = in_arr[i + 1]
                in_arr[i + 1] = tmp
                end_flag = True
    return in_arr


def merge_sort(a, b):
    res_arr = []
    seek_a, seek_b = 0, 0
    while True:
        if a[seek_a] < b[seek_b]:
            res_arr.append(a[seek_a])
            seek_a += 1
        elif b[seek_b] < a[seek_a]:
            res_arr.append(b[seek_b])
            seek_b += 1
        if seek_a == len(a):
            res_arr.extend(b[seek_b:])
            break
        elif seek_b == len(b):
            res_arr.extend(a[seek_a:])
            break
    return res_arr


N = 9
arr = [(rnd.uniform(0, 49.999)) for _ in range(N)]

print('*' * 50, '\nНачальный массив\n', arr)
arr_a = arr[:len(arr) // 2]
arr_b = arr[len(arr) // 2:]

print('Подмассив А -   ', arr_a)
arr_a = bubble_sort(arr_a)
print('Предв.сорт. А - ', arr_a)

print('Подмассив B -   ', arr_b)
arr_b = bubble_sort(arr_b)
print('Предв.сорт. B - ', arr_b)

print('*' * 50, '\nНачальный массив\n', arr)
print('Массив после merge-сортировки\n', merge_sort(arr_a, arr_b))
