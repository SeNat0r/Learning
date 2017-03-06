import sys
from scheluder import storage

# Подключение к базе
conn = storage.connect('tasks.db')
storage.initialize(conn)


# Функция показа меню
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
    conn.close()
    sys.exit(0)


# Добавление задачи
def action_add_task():
    task_name = input('Название задачи:\n')
    task_date = input('Дата выполнения:\n')
    text = input('Текст задачи:\n')
    storage.add_task(conn, task_name, task_date, text)


# Вывод всех задач
def action_all_tasks():
    all_tasks = storage.all_tasks(conn)
    for task in all_tasks:
        print('{task[id]}.   {task[task_name]}   {task[task_date]} - {task[status]}'.format(task=task))


def action_close_task():
    act = input('id: ')
    storage.close_task(conn, act)


def action_re_task():
    act = input('id: ')
    storage.re_task(conn, act)


# Редактирование задачи
def action_update_task():
    idx = input('id задачи: \n')
    task = storage.find_by_id(conn, idx)
    print('{task[task_name]}   {task[task_date]} {task[text]}'.format(task=task))
    task_name = input('Название задачи:\n')
    task_date = input('Дата выполнения:\n')
    text = input('Текст задачи:\n')
    storage.update_task(conn, task_name, task_date, text, idx)


actions = {
    '1': action_all_tasks,
    '2': action_add_task,
    '3': action_update_task,
    '4': action_close_task,
    '5': action_re_task,
    'm': action_show_menu,
    'q': action_exit
}

if __name__ == '__main__':
    action_show_menu()

    while True:
        cmd = input('\nВведите команду: ')
        action = actions.get(cmd)
        if action:
            action()
        else:
            print('Неизвестная команда')
