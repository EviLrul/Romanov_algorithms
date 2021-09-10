# 4. Определить, какое число в массиве встречается чаще всего.

from random import randint
rnd_array = []
search_list = []
itog_list = []

for i in range(10):
    rnd_array.append(randint(1, 5))

print('Исходный массив:', rnd_array)

for z in range(len(rnd_array)):
    search_list.append([rnd_array[z], rnd_array.count(rnd_array[z])])

for i in search_list:
    if i not in itog_list:
        itog_list.append(i)

print('Первое значение - это значение в массиве, второе значение - это сколько раз оно встречается в массиве')
print(itog_list)
