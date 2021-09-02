# 5. Пользователь вводит две буквы.
# Определить, на каких местах алфавита они стоят и сколько между ними находится букв.

letter1 = ord(input('Введите первую букву: '))
letter2 = ord(input('Введите вторую букву: '))
a_place1 = letter1-96
a_place2 = letter2-96
print('Буква "' + chr(letter1) + '" находится на', a_place1, 'месте.')
print('Буква "' + chr(letter2) + '" находится на', a_place2, 'месте.')
kol_vo_letters = a_place2 - a_place1 - 1
if kol_vo_letters > 0:
    print('Между этими буквами находится', kol_vo_letters, 'букв(а/ы)')
elif kol_vo_letters < -2:
    print('Между этими буквами находится', kol_vo_letters * (-1) - 2, 'букв(а/ы). НО!!! в обратную сторону!')
else:
    print('Между этими буквами, нет букв...')


