# 1. Пользователь вводит данные о количестве предприятий,
# их наименования и прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и вывести наименования предприятий, чья прибыль выше среднего и отдельно вывести
# наименования предприятий, чья прибыль ниже среднего.
quarterly_profit = []
average_profit = 0
b = {}

number_factories = int(input('Ведите количество предприятий: '))

for i in range(number_factories):
    name_factory = input('Введите название предприятия: ')
    for j in range(4):
        profit = int(input('Введите прибыль этого преприятия за ' + str(j + 1) + ' квартал: '))
        quarterly_profit.append(profit)
        average_profit += profit
    b[i] = [name_factory, quarterly_profit.copy()]
    quarterly_profit.clear()

average_profit = average_profit / (number_factories * 4)
print('Средняя прибыль по всем предприятиям за год:', average_profit, '\n')

for i in range(number_factories):
    if average_profit > sum((b[i][1])):
        print('Прибыль предприятия за год', b[i][0], 'равна', sum(b[i][1]), 'и она ниже средней прибыли')
    elif average_profit < sum((b[i][1])):
        print('Прибыль предприятия за год', b[i][0], 'равна', sum(b[i][1]),  'и она выше средней прибыли')
    else:
        print('Прибыль предприятия за год', b[i][0], 'равна', sum(b[i][1]),  'и она равна средней прибыли')
