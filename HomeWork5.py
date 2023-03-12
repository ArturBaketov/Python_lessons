'''
Напишите программу, которая на вход принимает два числа A и B, 
и возводит число А в целую степень B с помощью рекурсии.
'''

def power(a, n):
    if n == 0:
        return 1
    if n == 1:
        return a
    return power(a, n - 1) * a

print(power(float(input()), int(input())))

'''
Напишите рекурсивную функцию sum(a, b),
возвращающуюсумму двух целых неотрицательных
чисел. Из всех арифметических операций
допускаютсятолько +1 и -1. Также нельзя
использовать циклы.
'''


def sum(a, b):
    if b == 0:
        return a
    else:
        if b > 0:
            return sum(a + 1, b - 1)
        else:
            return sum(a - 1, b + 1)

print(sum(int(input()), int(input())))

