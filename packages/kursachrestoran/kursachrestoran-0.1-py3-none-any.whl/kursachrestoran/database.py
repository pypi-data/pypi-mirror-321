import psycopg2
from psycopg2 import sql

class Database:
    def __init__(self, dbname, user, password, host, port):
        self.dbname = "Restaraunt"  # Имя базы данных с маленькой буквы
        self.user = "postgres"
        self.password = "123"
        self.host = "localhost"
        self.port = "5432"
        self.connection = self._connect()

    def _connect(self):
        return psycopg2.connect(
            dbname=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host,
            port=self.port
        )

    def _reconnect(self):
        self.connection.close()
        self.connection = self._connect()

    def execute_query(self, query, params=None):
        try:
            with self.connection.cursor() as cursor:
                # Преобразуем sql.Composed в строку, если это необходимо
                if isinstance(query, sql.Composed):
                    query_str = query.as_string(self.connection)
                else:
                    query_str = query

                cursor.execute(query_str, params)
                if query_str.strip().upper().startswith("SELECT"):
                    return cursor.fetchall()
                self.connection.commit()
        except psycopg2.Error as e:
            print(f"Ошибка при выполнении запроса: {e}")
            self._reconnect()
            raise e

    def get_sales_by_date(self, start_date, end_date):
        return self.execute_query("SELECT * FROM get_sales_by_date(%s, %s)", (start_date, end_date))

    def get_ingredient_balances(self):
        return self.execute_query("SELECT * FROM get_ingredient_balances()")

    def get_revenue_by_category(self, start_date, end_date):
        return self.execute_query("SELECT * FROM get_revenue_by_category(%s, %s)", (start_date, end_date))

    def get_average_bill(self, start_date, end_date):
        return self.execute_query("SELECT get_average_bill(%s, %s)", (start_date, end_date))[0][0]

    def get_table_data(self, table_name):
        # Используем sql.Identifier для корректного указания имени таблицы
        query = sql.SQL("SELECT * FROM {}").format(sql.Identifier(table_name))
        return self.execute_query(query)

    def insert_record(self, table_name, columns, values):
        # Используем sql.Identifier для корректного указания имени таблицы и столбцов
        query = sql.SQL("INSERT INTO {} ({}) VALUES ({})").format(
            sql.Identifier(table_name),
            sql.SQL(', ').join(map(sql.Identifier, columns)),
            sql.SQL(', ').join(sql.Placeholder() * len(values))
        )
        self.execute_query(query, values)

    def update_record(self, table_name, columns, values, condition):
        # Используем sql.Identifier для корректного указания имени таблицы и столбцов
        set_clause = sql.SQL(', ').join(
            sql.SQL("{} = {}").format(sql.Identifier(col), sql.Placeholder()) for col in columns
        )
        query = sql.SQL("UPDATE {} SET {} WHERE {}").format(
            sql.Identifier(table_name),
            set_clause,
            sql.SQL(condition)
        )
        self.execute_query(query, values)

    def delete_record(self, table_name, condition):
        # Используем sql.Identifier для корректного указания имени таблицы
        query = sql.SQL("DELETE FROM {} WHERE {}").format(
            sql.Identifier(table_name),
            sql.SQL(condition)
        )
        self.execute_query(query)

    def close(self):
        self.connection.close()