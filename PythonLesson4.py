import msvcrt
import math
import sympy
import random


print('\n1. Вычислите число c заданной точностью d.\nПример:' +
      '\nпри d = 0.001, π = 3.141\n10^{-1} ≤ d ≤ 10^{-10}' +
      '\nРешение:')

d = int(input('Введите количество знаков после запятой (например, при вводе 1 -> d = 0.1, при вводе 2 -> d = 0.01 и т.д.): '))

# x = str(math.pi).split('.')
x = input('Введите число, которое нужно округлить: ').split('.')

print(x[0] + '.' + x[1][0:d])


msvcrt.getch()
print('\n2. Задайте натуральное число N. Напишите программу, которая ' +
      'составит список простых множителей числа N.' +
      '\nРешение:')

n = int(input('Введите число N: '))
some_list1 = [i for i in range(1, n+1) if not n % i]

some_list2 = []

for el in some_list1:
    exit = False
    d = 2
    while not exit:
        if el % d == 0:
            exit = True
        if el % d != 0:
            d += 1
        if d >= el:
            some_list2.append(el)
            exit = True

print(f'Cписок простых множителей числа {n} -> {some_list2}')


msvcrt.getch()
print('\n3. Задайте последовательность чисел. Напишите программу, которая выведет ' +
      'список неповторяющихся элементов исходной последовательности.' +
      '\nРешение:')

n = int(input('Введите размер списка: '))

some_list3 = [random.randint(0, n) for _ in range(n)]

print(f'Исходный список -> {some_list3}')

for el in some_list3:
    ind = some_list3.index(el)
    if el in some_list3[ind+1:]:
        for i in some_list3[ind:]:
            if i == el:
                some_list3.remove(i)

print(f'Список неповторяющихся элементов -> {some_list3}')


msvcrt.getch()
print('\n4. Задана натуральная степень k. Сформировать случайным образом список ' +
      'коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.' +
      '\nПример:\nk=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0' +
      '\nРешение:')

k = int(input('Введите k: '))

x = sympy.Symbol('x')
funk = 0

for n in range(k+1):
    funk = random.randint(0, 100) * (x**n) + funk

with open('file.txt', 'w+', encoding='utf-8') as file:
    file.write(f'{funk}' + ' = 0')

    file.seek(0, 0)
    for text in file:
        print(text)


msvcrt.getch()
