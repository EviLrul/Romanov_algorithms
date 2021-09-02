# 2. Выполнить логические побитовые операции «И», «ИЛИ» и др. над числами 5 и 6.
# Выполнить над числом 5 побитовый сдвиг вправо и влево на два знака. Объяснить полученный результат.

a = 5
b = 6

bit_and = a & b
bit_or = a | b
bit_xor = a ^ b
bit_left = a << 2
bit_right = a >> 2

print('a -', int(a), '=', bin(a))
print('b -', int(b), '=', bin(b))
print('a & b =',  bin(bit_and), '=', int(bit_and))      # Кодга обе 1 то 1
print('a & b =',  bin(bit_or), '=', int(bit_or))        # Когда хотя б одна 1 то 1
print('a & b =',  bin(bit_xor), '=', int(bit_xor))      # Когда лишь одна 1 то 1
print('a << =',  bin(bit_left), '=', int(bit_left))     # В "хвосте" добавляются два младших бита
print('a >> =',  bin(bit_right), '=', int(bit_right))   # От "головы" откидывается 2 старших бита
