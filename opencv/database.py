
import pymysql

# MySQL connection settings
DB_HOST = 'localhost'
DB_USER = 'root'
DB_PASSWORD = ''
DB_NAME = 'flask_db'

def insert_serial(serial_number):
    conn = pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD,
        db=DB_NAME
    )
    cursor = conn.cursor()
    cursor.execute("INSERT INTO computer_traking(serial_number) VALUES (%s)", (serial_number,))
    conn.commit()
    cursor.close()
    conn.close()
