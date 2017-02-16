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
    print('Введите длинну и ширину занятого пространства (м)')
    a = int(input())
    b = int(input())
    free = S - a * b
    if free > 0:
        print('Незанято', free, 'метров')
    else:
        print('Вы прихватизировали', -free, 'метров у соседа')
elif zadacha == 3:
