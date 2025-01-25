import sys
import psycopg2
from PyQt5 import QtWidgets

class DatabaseConnection:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.init_db()

    def init_db(self):
        """Устанавливает подключение к базе данных."""
        try:
            self.conn = psycopg2.connect(
                host="localhost",
                database="bd",
                port="5432",
                user="postgres",
                password="1"
            )
            self.cursor = self.conn.cursor()
        except psycopg2.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Ошибка подключения', f'Не удалось подключиться к базе данных: {e}')
            sys.exit(1)

    def execute_query(self, query, params=None):
        """Выполняет SQL-запрос и возвращает результат."""
        try:
            self.cursor.execute(query, params)
            if query.strip().lower().startswith('select'):
                return self.cursor.fetchall()
            else:
                self.conn.commit()
        except psycopg2.Error as e:
            QtWidgets.QMessageBox.critical(None, 'Ошибка выполнения запроса', f'Произошла ошибка при выполнении запроса: {e}')
            sys.exit(1)

    def close_connection(self):
        """Закрывает соединение с базой данных."""
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()