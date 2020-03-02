import math
print('Введите Не Отрицательные Числа: ')
a = float(input())
b = float(input())
c = float(input())

p = (a + b + c)/2

S = round(math.sqrt(p*(p-a)*(p-b)*(p-c)),2)
print(S)