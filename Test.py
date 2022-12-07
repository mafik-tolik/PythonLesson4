import os
import math
import sympy
import random

os.system('cls')

# -----------------------------------------------------------------------------------

# ЗАДАЧА НЕ РЕШЕНА

print('\n5. Даны два файла, в каждом из которых находится запись многочлена. ' +
      'Задача - сформировать файл, содержащий сумму многочленов.' +
      '\nРешение:')

x = sympy.Symbol('x')

with open('file1.txt', 'r', encoding='utf-8') as file:
    text_srt = file.read().split('=')


# for i in text_srt:
#     if 'x' in i:
#         'x' = x
# text_int = list(map(int, text_srt[0].split('+')))


# for i in text_srt:
#     if '**' in i:
#         i = i.split('*')
#         i[0] = int(i[0])
#         i = tuple(i)
#     elif '*' in i:
#         i = i.split('*')
#         i[0] = int(i[0])
#         i = tuple(i)
#     else:
#         i = int(i)

# print(text_srt)


# with open('file.txt2', 'r', encoding='utf-8') as file:
#     # <.read()> - читаем нашу переменную <file>.
#     # <splitlines()> разделяет текст из файла и превращает его в список из строк (каждая строчка - отдельный элемент).
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * list[int(index)]
# print(mult)
