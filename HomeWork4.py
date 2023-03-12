# Вычислить число π c заданной точностью *d*
# Пример:
# при d = 0.001, π = 3.141
# при d = 0.1, π = 3.1
# при d = 0.00001, π = 3.14154
# d от 0.1 до 0.0000000001

import math
x=math.pi
n=input('Введите число d чтобы задать точность вывода числа π (например: 0.001, 0,01): ')
count = 0

n = n.replace('0.', '')

for i in n:
    count+=1

print(f'Число {x:.{count}f}')


# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

n = int(input('Введите число N: '))
list = []
a = n
if n > 1:
    restart = True
    while restart:
        restart = False
        for i in range (2, n+1):
            if n%i == 0:
                list.append(i)
                n = int(n/i)
                restart = True
                break

    print(f'Простые множители числа {a} - {list}')
elif n == 1:
    print(f'Простые множители числа {a} - [1]')
else:
    print(f'Вы ввели не правильное число')

    
# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности. 

n = list("1115566773322")

list = n
print(list)

list_count = []
for i in list:
    count = 0
    for k in list:
        if k == i:
            count += 1
    list_count.append(count)
print(list_count)

result = []
for i in range(len(list_count)):
    if list_count[i] == 1:
        result.append(list[i])
print(result)

# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень следующего на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

from random import randint
import random

k = int(input('Введите число k: '))

result = ''
temp = []
for i in range(k):
    temp.append(randint(0, 100))


znak = ['+', '-']
i = 0
j = 0
while k > 1:
    if temp[i] != 0:
        result += (f'{temp[i]}x**{k}{random.choice(znak)}')
    k -= 1
    i += 1


if temp[-1] != 0:
    result += (f'{temp[-1]}=0')
else:
    result += ('=0')
with open('result.txt', 'w', encoding='utf8') as file:
    file.write(f'Сгенерированные числа: {temp}\nОтвет: {result}')
    
