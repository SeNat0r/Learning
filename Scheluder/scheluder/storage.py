import sqlite3

SQL_SELECT = '''SELECT id, task_name, task_date, text, status FROM scheluder'''


def dict_factory(cursor, row):
    d = {}
    for idx, col in enumerate(cursor.description):
        d[col[0]] = row[idx]
    return d


# Инициализация базы
def initialize(conn):
    with conn:
        cursor = conn.executescript('''
            CREATE TABLE IF NOT EXISTS scheluder (
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                task_name TEXT NOT NULL DEFAULT '',
                task_date DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
                text TEXT NOT NULL DEFAULT '',
                status TEXT NOT NULL DEFAULT 'Не выполнено'
            )
        ''')


# Подключение(создание) к базе данных
def connect(db_name=None):
    # Если название базы не указано, загружать базу в ОЗУ
    if db_name is None:
        db_name = ':memory:'

    conn = sqlite3.connect(db_name)
    conn.row_factory = dict_factory

    return conn


# Добавление задачи к базе данных
def add_task(conn, task_name, task_date, text):
    with conn:
        cursor = conn.execute('''
            INSERT INTO scheluder (task_name, task_date, text) VALUES (?,?,?)
        ''', (task_name, task_date, text))


def update_task(conn, tsk_nm, tsk_dt, text, ident):
    cursor = conn.execute('''
        UPDATE scheluder SET task_name=?, task_date=?, text=? WHERE id=?
    ''', (tsk_nm, tsk_dt, text, ident))
    conn.commit()


def re_task(conn, ident):
    cursor = conn.execute('''
            UPDATE scheluder SET status=0 WHERE id=?
        ''', ident)
    conn.commit()


def close_task(conn, ident):
    cursor = conn.execute('''
            UPDATE scheluder SET status=1 WHERE id=?
        ''', ident)
    conn.commit()


def all_tasks(conn):
    for row in conn.execute('''SELECT * FROM scheluder'''):
        if row[4] == 0:
            status = 'Не выполнено'
        else:
            status = 'Выполнено'
        print('{0[0]}   {0[1]}   {0[2]}   {0[3]}    {1}'.format(row, status))
