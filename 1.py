# 1. Написать программу, которая будет складывать, вычитать, умножать или делить два числа.
# Числа и знак операции вводятся пользователем. После выполнения вычисления программа не должна
# завершаться, а должна запрашивать новые данные для вычислений. Завершение программы должно
# выполняться при вводе символа '0' в качестве знака операции. Если пользователь вводит
# неверный знак (не '0', '+', '-', '*', '/'), то программа должна сообщать ему об ошибке и снова
# запрашивать знак операции. Также сообщать пользователю о невозможности деления на ноль,
# если он ввел 0 в качестве делителя.

while True:
    number_one = int(input('Введите первое число: '))
    number_two = int(input('Введите второе число: '))
    while True:
        action = input('Введите действие (+, -, *, /, для выхода введите - 0): ')
        if action == '0':
            print('Завершение программы. Спасибо!!!')
            exit()
        if number_one == 0 and action == '/':
            print('На ноль делить нельзя, попробуейте ещё раз!!!')
            break
        if action == '+':
            print(number_one, action, number_two, '=', number_one+number_two)
            break
        elif action == '-':
            print(number_one, action, number_two, '= ', number_one-number_two)
            break
        elif action == '*':
            print(number_one, action, number_two, '= ', number_one*number_two)
            break
        elif action == '/':
            print(number_one, action, number_two, '= ', number_one/number_two)
            break
        else:
            print('Не корректно введено действие!!! Попробуйте снова')

