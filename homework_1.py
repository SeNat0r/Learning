from datetime import datetime

print('Введите номер задачи:')
zadacha = int(input())
if zadacha == 1:
    n = datetime.now().minute
    color = n % 5
    if 0 < color < 3:
        print('Горит зелёный!')
    else:
        print('DA RED GOEZ FASTA!!!')
elif zadacha == 2:
    print('Введите размер участка(в сотках)')
    sotka = input()
    S = int(sotka) * 100
    print('Введите длинну и ширину занятого пространства')
    a = int(input('Длинна (м)= '))
    b = int(input('Ширина (м)= '))
    free = S - a * b
    if free > 0:
        print('Незанято', free, 'метров')
    else:
        print('Вы прихватизировали', -free, 'метров у соседа')
elif zadacha == 3:
    print('Введите координаты точки А')
    xa = int(input('x: '))
    ya = int(input('y: '))
    print('Введите координаты точки B')
    xb = int(input('x: '))
    yb = int(input('y: '))
    print('Введите координаты точки C')
    xc = int(input('x: '))
    yc = int(input('y: '))
    if xa == xb == xc or ya == yb == yc:
        print('Это не треугольник!')
    elif (xa == xb and ya == yb) or (xa == xc and ya == yc) or (xc == xb and yc == yb):
        print('Я в ответах ограничен, задавай правильные координаты...')
    else:
        if xa == xb or xa == xc or xb == xc:
            if ya == yb or ya == yc or yb == yc:
                print('Это правильный треугольник!')
            else:
                print('Это не правильный треугольник')
        else:
            print('Это не правильный треугольник')
else:
    print("Нет такого номера задачи!")
