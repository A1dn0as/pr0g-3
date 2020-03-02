import math

print('Введите Три Стороны:')


def func_geron():
    a = int(input())
    b = int(input())
    c = int(input())
    p = (a + b + c) / 2
    s = math.sqrt(p * (p - a) * (p - c) * (p - b))
    return s


vv = func_geron()
print(vv)
