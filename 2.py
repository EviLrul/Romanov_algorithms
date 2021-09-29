# 2. Закодируйте любую строку из трех слов по алгоритму Хаффмана.

"""
фраза: hello happy hell

из полученного графа(ссылка на документ:
https://docs.google.com/drawings/d/1HvJgnHeNtwTJXSFW-4RNUJkN-SLMlnM9T5zqFLYzsLk/edit?usp=sharing)
можно закодировать символы
h - 00
l - 10
p - 010
e - 110
o - 1110
y - 11110
a - 11111

Таким образом получим кодированную фразу

00 110 10 10 1110       - hello
00 11111 010 010 11110  - happy
00 110 10 10            - hell


"""