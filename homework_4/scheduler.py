# from datetime import date
def tsk(dt,name,text):
    task = {'dt': dt, 'name': name, 'text': text, 'status': 'Не выполнено'}
    return task

tasks = {
    1: {'dt': '01.03.2017', 'name': 'lalala', 'text': 'atatattata', 'status': 'Не выполнено'},
    2: {'dt': '01.03.2017', 'name': 'orooror', 'text': 'nannaa','status': 'Не выполнено'}
}

# print(tasks)

while True:
    print('1. Вывести список задач')
    act = int(input())
    if act == 0:
        break
    elif act == 1:
        i = 1
        for n in tasks.values():
            print(i, n['dt'], n['name'])
            i += 1
        while True:
            numer = int(input('Введите номер задачи для её просмотра '))
            if 0 < numer <= len(tasks):
                tmp = tasks[numer]
                print(tmp['text'])
            elif numer == 0:
                break
    elif act == 2:
        tasks.update({(len(tasks) + 1): (tsk(name=input('Введите название задачи: '), \
                     dt=input('Введите дату: '), text=input('Введите текст задачи: ')))})
