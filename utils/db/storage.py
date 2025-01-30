from sqlite3 import connect


class DatabaseManager:

    def __init__(self, path):
        self.conn = connect(path)
        self.conn.execute('pragma foreign_keys = on')
        self.conn.commit()
        self.cur = self.conn.cursor()

    def create_tables(self):
        # Таблица для серверов
        self.query(
            '''
            CREATE TABLE IF NOT EXISTS servers (
                server_id SERIAL PRIMARY KEY,
                location TEXT NOT NULL,
                created_date DATE NOT NULL,
                prepaid_time INTEGER,
                server_characteristics TEXT,
                user_count INTEGER
            )
            '''
        )

        # Таблица для привязки пользователей
        self.query(
            '''
            CREATE TABLE IF NOT EXISTS users (
                user_id SERIAL PRIMARY KEY,
                tg TEXT NOT NULL,
                payment_sum REAL,
                ssh_start_date DATE,
                ssh_end_date DATE,
                ssh_id INTEGER,
                server_id INTEGER,
                FOREIGN KEY (ssh_id) REFERENCES ssh_keys(ssh_id),
                FOREIGN KEY (server_id) REFERENCES servers(server_id)
            )
            '''
        )

        # Таблица для SSH
        self.query(
            '''
            CREATE TABLE IF NOT EXISTS ssh_keys (
                ssh_id SERIAL PRIMARY KEY,
                ssh_key TEXT NOT NULL,
                key_id INTEGER,
                server_id INTEGER,
                FOREIGN KEY (server_id) REFERENCES servers(server_id)
            )
            '''
        )
    def query(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        self.conn.commit()

    def fetchone(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchone()

    def fetchall(self, arg, values=None):
        if values is None:
            self.cur.execute(arg)
        else:
            self.cur.execute(arg, values)
        return self.cur.fetchall()

    def __del__(self):
        self.conn.close()
