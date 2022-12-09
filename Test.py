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

with open('file1.txt', 'r', encoding='utf-8') as file:
    text1 = file.read().split(' = ')

sum1 = 0
text1 = text1[0].split(' + ')
for i in text1:
    if 'x' in i:
        if '**' in i:
            i = i.split('**')
            i[1] = int(i[1])
            if '*' in i[0]:
                j = i[0].split('*')
                j[0] = int(j[0])
                j[1] = sympy.Symbol('x')
                sum1 += j[0]*(j[1]**i[1])
            else:
                i[0] = sympy.Symbol('x')
                sum1 += i[0]**i[1]
        else:
            if '*' in i:
                i = i.split('*')
                i[0] = int(i[0])
                i[1] = sympy.Symbol('x')
                sum1 += i[0]*i[1]
    else:
        i = int(i)
        sum1 += i

print(sum1)
# 6*x**5 + 5*x**4 + 2*x**2 + 5*x + 9 = 0


# with open('file.txt2', 'r', encoding='utf-8') as file:
#     # <.read()> - читаем нашу переменную <file>.
#     # <splitlines()> разделяет текст из файла и превращает его в список из строк (каждая строчка - отдельный элемент).
#     index_list = file.read().splitlines()
#     for index in index_list:
#         mult = mult * list[int(index)]
# print(mult)
