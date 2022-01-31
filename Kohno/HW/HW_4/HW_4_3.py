'''
3) Дан словарь: {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
Добавить каждому ключу число равное длине этого ключа (пример {‘key’: ‘value’} -> {‘key3’:
‘value’}). Чтобы получить список ключей - использовать метод .keys()
(подсказка: создается новый ключ с цифрой в конце, старый удаляется)
'''

dict_start = {'test': 'test_value', 'europe': 'eur', 'dollar': 'usd', 'ruble': 'rub'}
list_keys = dict_start.keys()
list_values = dict_start.values()
list_keys_normal = []

for i in list_keys:
    i = i + str(len(i))
    list_keys_normal.append(i)

list_values_normal = []
for i in list_values:
    list_values_normal.append(i)

dict_new_faq = {}
while list_keys_normal:
    dict_new_faq.update([(list_keys_normal.pop(), list_values_normal.pop())])
print(dict_new_faq)