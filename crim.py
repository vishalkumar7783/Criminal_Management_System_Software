import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="12345678"
    )
    print("MySQL Connection Successful!")
    conn.close()
except Exception as e:
    print(f"Connection failed: {e}")