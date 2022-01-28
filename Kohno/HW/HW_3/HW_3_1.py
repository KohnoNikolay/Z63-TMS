'''
1) Введите число. Если это число делиться на 1000 без остатка, то выведите на
экран "millennium"
'''

number = int(input("input number "))

if number % 1000 == 0:
    print("millennium")