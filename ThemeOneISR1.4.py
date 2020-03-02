print('Выберите ваше действие:\n1.Сложение\n2.Вычитание\n3.Умножение\n4.Деление')
print('Введите число выбора: ')
choice = int(input())

if choice == 1:

    print('Вы выбрали сложение.\n Введите 2 числа для сложения:')
    a = int(input())
    b = int(input())
    print(a+b)
elif choice == 2:

    print('Вы выбрали вычитание.\n Введите 2 числа для вычитания:')
    a = int(input())
    b = int(input())
    print(a - b)
elif choice == 3:

    print('Вы выбрали умножение.\n Введите 2 числа для умножения:')
    a = int(input())
    b = int(input())
    print(a * b)
elif choice == 4:

    print('Вы выбрали деление.\n Введите 2 числа для деления:')
    a = int(input())
    b = int(input())
    print(round(a / b),2)
else:
    print('пока-пока')