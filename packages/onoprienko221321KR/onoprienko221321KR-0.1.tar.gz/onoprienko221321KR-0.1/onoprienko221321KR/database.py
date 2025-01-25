import psycopg2
from psycopg2 import sql

# Параметры подключения к базе данных
DB_NAME = "medical_inventory"
DB_USER = "postgres"
DB_PASSWORD = "pdthmerh"
DB_HOST = "localhost"
DB_PORT = "5432"

# Функция для подключения к базе данных
def connect():
    return psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

# Функция для выполнения SQL-запросов
def execute_query(query, params=None, fetch=False):
    conn = connect()
    try:
        with conn.cursor() as cursor:
            cursor.execute(query, params)
            if fetch:
                result = cursor.fetchall()
                return result
            conn.commit()
    except Exception as e:
        print(f"Ошибка: {e}")
    finally:
        conn.close()

# Функция для получения отчёта по статусу оборудования
def get_equipment_by_status_report():
    query = """
    SELECT 
        Equipment.id AS equipment_id,
        Equipment.name AS equipment_name,
        Equipment.status
    FROM Equipment
    ORDER BY Equipment.status;
    """
    return execute_query(query, fetch=True)

# Функция для получения данных из VIEW (EquipmentView)
def get_equipment_view():
    query = "SELECT * FROM EquipmentView;"
    return execute_query(query, fetch=True)

# Функция для добавления нового оборудования
def add_equipment(name, description, status, location_id):
    query = """
    INSERT INTO Equipment (name, description, status, location_id)
    VALUES (%s, %s, %s, %s);
    """
    execute_query(query, (name, description, status, location_id))

# Функция для редактирования оборудования
def update_equipment(equipment_id, name, description, status, location_id):
    query = """
    UPDATE Equipment
    SET name = %s, description = %s, status = %s, location_id = %s
    WHERE id = %s;
    """
    execute_query(query, (name, description, status, location_id, equipment_id))