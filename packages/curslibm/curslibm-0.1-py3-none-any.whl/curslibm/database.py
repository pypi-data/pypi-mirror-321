import psycopg2
from psycopg2 import sql
DB_NAME = "warehouse"
DB_USER = "postgres"
DB_PASSWORD = "12"
DB_HOST = "localhost"
DB_PORT = "5432"
def create_connection():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
def execute_query(query, params=None, fetch=False):
    connection = create_connection()
    cursor = connection.cursor()
    try:
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
        else:
            connection.commit()
            result = None
    except Exception as e:
        print(f"Ошибка при выполнении запроса: {e}")
        result = None
    finally:
        cursor.close()
        connection.close()
    return result

# Функции для работы с таблицами

def get_table_data(table_name):
    query = sql.SQL("SELECT * FROM {};").format(sql.Identifier(table_name))
    return execute_query(query, fetch=True)

def get_table_columns(table_name):
    query = """
    SELECT column_name
    FROM information_schema.columns
    WHERE table_name = %s;
    """
    return execute_query(query, (table_name,), fetch=True)

def insert_record(table_name, values):
    columns = get_table_columns(table_name)
    if not columns:
        return False
    columns = [col[0] for col in columns]
    query = sql.SQL("INSERT INTO {} ({}) VALUES ({});").format(
        sql.Identifier(table_name),
        sql.SQL(", ").join(map(sql.Identifier, columns)),
        sql.SQL(", ").join(sql.Placeholder() * len(columns))
    )
    execute_query(query, values)
    return True

def update_record(table_name, record_id, values):
    columns = get_table_columns(table_name)
    if not columns:
        return False
    columns = [col[0] for col in columns]
    query = sql.SQL("UPDATE {} SET {} WHERE {} = %s;").format(
        sql.Identifier(table_name),
        sql.SQL(", ").join(sql.Identifier(col) + sql.SQL(" = %s") for col in columns),
        sql.Identifier(columns[0])  # Предполагаем, что первый столбец - это ID
    )
    # Преобразуем values в кортеж и добавляем record_id
    execute_query(query, tuple(values) + (record_id,))
    return True

def delete_record(table_name, record_id):
    columns = get_table_columns(table_name)
    if not columns:
        return False
    query = sql.SQL("DELETE FROM {} WHERE {} = %s;").format(
        sql.Identifier(table_name),
        sql.Identifier(columns[0][0])  # Предполагаем, что первый столбец - это ID
    )
    execute_query(query, (record_id,))
    return True

# Функции для отчётов

def get_reports():
    return {
        "Общая выручка": calculate_total_revenue,
        "Проданные единицы": calculate_sold_quantity,
        "Остатки на складе": calculate_stock_balance
    }

def calculate_total_revenue(start_date, end_date):
    query = "SELECT calculate_total_revenue(%s, %s);"
    return execute_query(query, (start_date, end_date), fetch=True)

def calculate_sold_quantity(start_date, end_date):
    query = "SELECT * FROM calculate_sold_quantity(%s, %s);"
    return execute_query(query, (start_date, end_date), fetch=True)

def calculate_stock_balance(as_of_date):
    query = "SELECT * FROM calculate_stock_balance(%s);"
    return execute_query(query, (as_of_date,), fetch=True)