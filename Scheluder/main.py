import sys
from scheluder import storage

# Подключение к базе
conn = storage.connect('tasks.db')
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

def action_all_tasks():
    storage.all_tasks(conn)

if __name__ == '__main__':
    action_show_menu()


while True:
    cmd = input('\nВведите команду: ')
    if cmd == '1':
        action_all_tasks()
    elif cmd == '2':
        action_add_task()
    elif cmd == 'q':
        action_exit()
    elif cmd == 'm':
        action_show_menu()