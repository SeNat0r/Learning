import sqlite3


# Подключение(создание) к базе данных
def connect(db_name=None):
    # Если название базы не указано, загружать базу в ОЗУ
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    return conn


# Инициализация базы
def initialize(conn):
    with conn:
        cursor = conn.executescript('''
            CREATE TABLE IF NOT EXISTS scheluder (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                task_name TEXT NOT NULL DEFAULT '',
                task_date TEXT NOT NULL DEFAULT '',
                text TEXT NOT NULL DEFAULT '',
                status INTEGER NOT NULL DEFAULT 0
            )
        ''')


# Добавление задачи к базе данных
def add_task(conn, tsk_nm, tsk_dt, text):
    cursor = conn.execute('''
        INSERT INTO scheluder (task_name, task_date, text) VALUES (?,?,?)
    ''', (tsk_nm, tsk_dt, text))
    conn.commit()


def update_task(conn, tsk_nm, tsk_dt, text, ident):
    cursor = conn.execute('''
        UPDATE scheluder SET (task_name=?, task_date=?, text=?) WHERE id=?
    ''', (tsk_nm, tsk_dt, text, ident))
    conn.commit()



def all_tasks(conn):
    for row in conn.execute('''SELECT * FROM scheluder'''):
        if row[4] == 0:
            status = 'Не выполнено'
        else:
            status = 'Выполнено'
        print('{0[0]}   {0[1]}   {0[2]}   {0[3]}    {1}'.format(row, status))
