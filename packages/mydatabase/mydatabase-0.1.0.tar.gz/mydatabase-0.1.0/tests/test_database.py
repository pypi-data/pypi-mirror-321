import unittest
from unittest.mock import patch, MagicMock
from my_library.core import DatabaseConnection

class TestDatabaseConnection(unittest.TestCase):
    @patch('my_library.core.psycopg2.connect')
    def test_init_db_success(self, mock_connect):
        # Симулируем успешное подключение к базе данных
        mock_connection = MagicMock()
        mock_connect.return_value = mock_connection

        db = DatabaseConnection()
        self.assertEqual(db.conn, mock_connection)
        self.assertEqual(db.cursor, mock_connection.cursor.return_value)

    @patch('my_library.core.psycopg2.connect')
    def test_init_db_failure(self, mock_connect):
        # Симулируем ошибку при подключении
        mock_connect.side_effect = psycopg2.Error("Ошибка подключения")

        with self.assertRaises(SystemExit):  # Ожидаем, что программа выйдет с ошибкой
            DatabaseConnection()

if __name__ == '__main__':
    unittest.main()
