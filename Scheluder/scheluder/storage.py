import sqlite3

SQL_SELECT = '''
    SELECT
        id, task_name, task_date, text, status
    FROM
        scheluder
'''


# Вывод значений из базы в списке (а не в кортеже)
def dict_factory(cursor, row):
    d = {}
    for i, col in enumerate(cursor.description):
        d[col[0]] = row[i]
    return d


# Подключение(создание) к базе данных
def connect(db_name=None):
    # Если название базы не указано, загружать базу в ОЗУ
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory
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

