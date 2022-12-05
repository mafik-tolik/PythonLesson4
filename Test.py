import os
import math
import sympy
import random

os.system('cls')

# -----------------------------------------------------------------------------------

print('\n4. Задана натуральная степень k. Сформировать случайным образом список ' +
      'коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.' +
      '\nПример:\nk=2 => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0' +
      '\nРешение:')

k = int(input('Введите k: '))

x = sympy.Symbol('x')
funk = 0
n = 0

# while n < k:

funk = random.randint(0, 100) * (x**n) + funk
if not sympy.solve(funk):
    n += 1
    funk = random.randint(0, 100) * (x**n) + funk


print(funk)

