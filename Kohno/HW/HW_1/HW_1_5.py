'''
5. Даны катеты прямоугольного треугольника. Найти его гипотенузу и
площадь
'''

from math import sqrt
katet_a = 5
katet_b = 10
gipotenuza = sqrt(katet_a ** 2 + katet_b ** 2)
ploschad = (katet_a * katet_b) / 2

print(ploschad, gipotenuza)
