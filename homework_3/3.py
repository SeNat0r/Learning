def fourth(x, y):
    if x == 0 or y == 0:
        f = 0
    elif x > 0:
        if y > 0:
            f = 1
        else:
            f = 4
    elif x < 0:
        if y > 0:
            f = 2
        else:
            f = 3

    return \
        print('Точка принадлежит {} четверти'.format(f)) if f > 0 else print('Точка не принадлежит какой-либо четверти')

x, y = int(input('Введите x: ')), int(input('Введите y: '))
fourth(x, y)
