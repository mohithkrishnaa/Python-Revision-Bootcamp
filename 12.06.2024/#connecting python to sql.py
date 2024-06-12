# Connecting Python to a SQL database allows you to execute queries, retrieve data, and interact with the database programmatically.
# This can be accomplished using various libraries depending on the type of SQL database you're using.
# Here, we'll focus on the most commonly used databases: SQLite, MySQL, and PostgreSQL.

# MySQL
# INSTALLATION
# pip install mysql-connector-python

# CONNECTING TO MySQL:
import mysql.connector

try:
    # Connect to the MySQL database
    conn = mysql.connector.connect(
        host='localhost',
        user='yourusername',
        password='yourpassword',
        database='yourdatabase'
    )

    # Create a cursor object
    cursor = conn.cursor()

    # CREATING A TABLE
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(255),
        age INT
    )
    ''')

    # Commit the changes
    conn.commit()

    # INSERTING DATA INTO THE TABLE
    cursor.execute('''
    INSERT INTO users (name, age) VALUES (%s, %s)
    ''', ('Alice', 30))

    # Commit the changes
    conn.commit()

    # QUERYING DATA
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()

    for row in rows:
        print(row)

    # UPDATING DATA
    cursor.execute('''
    UPDATE users SET age = %s WHERE name = %s
    ''', (32, 'Alice'))

    # Commit the changes
    conn.commit()

    # DELETING DATA
    cursor.execute('''
    DELETE FROM users WHERE name = %s
    ''', ('Alice',))

    # Commit the changes
    conn.commit()

except mysql.connector.Error as err:
    print(f"Error: {err}")
finally:
    # CLOSING THE CONNECTION:
    if conn.is_connected():
        cursor.close()
        conn.close()
