import sys
from scheluder import storage

# Подключение к базе
conn = storage.connect()
storage.initialize(conn)

#Функция показа меню
def action_show_menu():
    print('''
Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
m. Показать меню
q. Выход
    ''')

# Выход
def action_exit():
    sys.exit(0)

# Добавление задачи
def action_add_task():
    tsk_nm = input('Название задачи:\n')
    task_date = input('Дата выполнения:\n')
    text = input('Текст задачи:\n')
    storage.add_task(conn, tsk_nm, task_date, text)

def action_find_all():
    tasks = storage.find_all(conn)

    for t in tasks:
        print('{t[id]}  {t[task_name]}  {t[task_date]}  {t[status]}'.format(t=t))

if __name__ == '__main__':
    action_show_menu()

# actions = {'2': action_add_task(), 'q': action_exit()}


while True:
    cmd = input('\nВведите команду: ')
    if cmd == '1':
        action_find_all()
    elif cmd == '2':
        action_add_task()
    elif cmd == 'q':
        action_exit()
    elif cmd == 'm':
        action_show_menu()