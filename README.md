# pr0g-3
## LR - 1
```python
"""
Написать скрипт, который организует вычисление
суммы элементов арифметической прогрессии
от 1 до 100 Sum(1,2,3, .. 100)

Работу выполнил студент 2-го курса Галактионов Максим, 1 группа, 1 подгруппа
"""
x = 0
for i in range(101):
    x = x + i
    assert isinstance(x, object)
    print(x)

```
## SR - 2
```python
"""
Создание таблицы истинности без циклов
Работу выполнил студент 2-го курса Галактионов Максим, 1 группа, 1 подгруппа
"""
t_true = " 1 "
f_false = " 0 "

a = '  A '
b = ' B '
a_b = ' A⋁B '
slash = '|'
sym = '----------------'
sym_ = '⌜──────────────⌝'
bol = '⌞──────────────⌟'
print(sym_)
print(str(slash) + a + str(slash) + b + str(slash) + a_b + str(slash))
print(sym)

first: str = (str(slash) + str(" ") + f_false + str(slash) + str("") + f_false + str(slash) + str(" ") + f_false + str(
    " ") + str(slash))
print(first)
print(sym)
second: str = (str(slash) + str(" ") + f_false + str(slash) + str("") + t_true + str(slash) + str(" ") + t_true + str(
    " ") + str(slash))
print(second)
print(sym)
third: str = (str(slash) + str(" ") + t_true + str(slash) + str("") + f_false + str(slash) + str(" ") + t_true + str(
    " ") + str(slash))
print(third)
print(sym)
fourth: str = (str(slash) + str(" ") + t_true + str(slash) + str("") + t_true + str(slash) + str(" ") + t_true + str(
    " ") + str(slash))
print(fourth)
print(bol)

"""
Создание таблицы истинности без циклов
Работу выполнил студент 2-го курса Галактионов Максим, 1 группа, 1 подгруппа
"""
t_true = " 1 "
f_false = " 0 "

a = '  A '
b = ' B '
a_b = ' A⋁B '
slash = '|'
sym = '----------------'
sym_ = '⌜──────────────⌝'
bol = '⌞──────────────⌟'
print(sym_)
print(str(slash) + a + str(slash) + b + str(slash) + a_b + str(slash))
print(sym)

first: str = (str(slash) + str(" ") + f_false + str(slash) + str("") + f_false + str(slash) + str(" ") + f_false + str(
    " ") + str(slash))
print(first)
print(sym)
second: str = (str(slash) + str(" ") + f_false + str(slash) + str("") + t_true + str(slash) + str(" ") + f_false + str(
    " ") + str(slash))
print(second)
print(sym)
third: str = (str(slash) + str(" ") + t_true + str(slash) + str("") + f_false + str(slash) + str(" ") + f_false + str(
    " ") + str(slash))
print(third)
print(sym)
fourth: str = (str(slash) + str(" ") + t_true + str(slash) + str("") + t_true + str(slash) + str(" ") + t_true + str(
    " ") + str(slash))
print(fourth)
print(bol)

"""
Работа со списками:
Сумма четных элементов
Сумма нечетных элементов
Перевернутый список нечетных элементов

Работу выполнил студент 2-го курса Галактионов Максим, 1 группа, 1 подгруппа
"""
lst = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
print(lst)
l = lst[1::2]
print(l)
print(sum(l))
s = lst[5:-1:2]
print(s)
print(sum(s))
f = lst[::-1]
a = f[1::2]
print(a)

import math
"""
работа с кортежем и изменением его внутренних переменных 
найти Сумму всех чисел с плавающей точкой
Работу выполнил студент 2-го курса Галактионов Максим, 1 группа, 1 подгруппа"""
car = ("name", " DeLorean DMC-12", "motor_pos", "rear", "n_of_wheels", 4, "n_of_passengers", 2, "weight", 1.230,
       "height", 1.140, "length", 4.216, "width", 1.857, "max_speed", 177)
f = list(car)
print(f)
s =f[::-1]
print(s)
a = s[0:-6:2]
print(a)
print(round(sum(a),5))

```
