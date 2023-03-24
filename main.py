"""Вариант 4.
Натуральные простые числа, не превышающие 1 000, у которых средняя цифра равна 4. Минимальное и максимальное число выводятся прописью."""
import re
m = []
def slovo(x):
    z = {'0': 'ноль', '1': 'один', '2': 'два', '3': 'три', '4': 'четыре', '5': 'пять', '6': 'шесть', '7': 'семь',
         '8': 'восемь', '9': 'девять'}
    return z[x]
f = open('text.txt')
buffer = f.readline().split()
if not buffer:
    print('Файл пустой.')
    quit()
else:
    while True:
        if not buffer:
            break
        for i in buffer:
            work_buffer = re.findall(r'[1-9]*4[1,3,7,9]', i)
            if work_buffer:
               if len(work_buffer[0]) == len(i) and len(work_buffer[0]) ==3:
                m += [int(work_buffer[0])]
        buffer = f.readline().split()
if m:
    max_number = max(m)
    k = ''
    for i in range(len(str(max_number))):
        g = slovo(str(max_number)[i])
        k += g + ' '
    print(f'Максимальное значение: {k}.')
else:
    print('В файле нет подходящих значений.')
if m:
    min_number = min(m)
    k = ''
    for i in range(len(str(min_number))):
        g = slovo(str(min_number)[i])
        k += g + ' '
    print(f'Минимальное значение: {k}.')
else:
    print('В файле нет подходящих значений.')
