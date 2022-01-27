'''
Даны два действительных числа. Найти среднее арифметическое и
среднее геометрическое этих чисел
'''

from math import sqrt

a = 1
b = 2
srednee_ar = (a + b) / 2
srednee_ge = sqrt(a * b)

print(srednee_ge, srednee_ar)