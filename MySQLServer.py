import mysql.connector
from mysql.connector import Error

def create_database():
    """Create the alx_book_store database in MySQL server."""
    connection = None

    try:
        # Connect to MySQL Server (update credentials if needed)
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="your_password"   # ← Replace with your MySQL root password
        )

        if connection.is_connected():
            cursor = connection.cursor()

            # Create database if it doesn't exist
            cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

            print("Database 'alx_book_store' created successfully!")

    except Error as e:
        print(f"Error while connecting to MySQL: {e}")

    finally:
        # Close the cursor and connection
        if connection and connection.is_connected():
            cursor.close()
            connection.close()
            # Optional: print message to confirm closure
            # print("MySQL connection closed.")

if __name__ == "__main__":
    create_database()
