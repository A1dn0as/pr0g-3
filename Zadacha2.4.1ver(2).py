def volume():

    print('Количество воды в сосуде :')
    v1 = int(input())
    print('Уровень воды : ')
    h1 = int(input())
    print('На сколько поднялся уровень воды :')
    h2 = int(input())
    volume_mute = (h2 / h1) * v1
    return volume_mute


a = volume()

print(a)
