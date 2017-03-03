import sys
from scheluder import storage

conn = storage.connect('1.db')
storage.initialize(conn)


def action_show_menu():
    print('''
Ежедневник. Выберите действие:

1. Вывести список задач
2. Добавить задачу
3. Отредактировать задачу
4. Завершить задачу
5. Начать задачу сначала
q. Выход
    ''')



action_show_menu()



