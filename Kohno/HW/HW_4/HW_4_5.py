'''
5) Составить список чисел Фибоначчи содержащий 15 элементов.
(Подсказка: Числа Фибоначчи - последовательность, в которой первые два числа равны
либо 1 и 1, а каждое последующее число равно сумме двух предыдущих чисел.
Пример: 1, 1, 2, 3, 5, 8, 13, 21, 34... )
'''

list_fib = [1, 1]
elem = 2

while elem < 15:
    elem += 1
    new_numb = list_fib[-1] + list_fib[-2]
    list_fib.append(new_numb)

print(list_fib)
