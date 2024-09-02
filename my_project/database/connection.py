import pyodbc
from my_project.database.config import sistem
from  my_project.database.config import DATABASE_CONFIG

def get_connection():
    conn_str = (
        f"DRIVER={DATABASE_CONFIG['driver']};"
        f"SERVER={DATABASE_CONFIG['server']};"
        f"DATABASE={DATABASE_CONFIG['database']};"
        f"UID={DATABASE_CONFIG['username']};"
        f"PWD={DATABASE_CONFIG['password']}"
    )
    try:
        conn = pyodbc.connect(conn_str)
        print("Connection successful!")
        return conn
    except pyodbc.Error as e:
        print(f"Connection failed: {e}")
        return None

if __name__ == "__main__":
    connection = get_connection()

    if connection:
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT 1")
            result = cursor.fetchone()
            print(f"Query result: {result}")
        except pyodbc.Error as e:
            print(f"Query execution failed: {e}")
        finally:
            connection.close()
