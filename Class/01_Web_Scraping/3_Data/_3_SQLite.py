import _0_Coin as coin_data
import sqlite3


db_name = "example.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()


def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS coin (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            current_info INTEGER,
            change_point INTEGER
        )
    ''')
    print("Table 'coin' created successfully.")


def insert_data(curr_point, changed_point):
    cursor.execute('''
        INSERT INTO coin (current_info, change_point) 
        VALUES (?, ?)
    ''', (curr_point, changed_point))
    conn.commit()
    print(f"Inserted {curr_point}, {changed_point} into the table.")


def fetch_data():
    cursor.execute('SELECT * FROM coin')
    rows = cursor.fetchall()
    print("\nFetched Data:")
    for row in rows:
        print(row)


def close_connection():
    conn.close()
    print("\nDatabase connection closed.")


if __name__ == "__main__":
    coin_name = "bitcoin"

    current_info, change_point = coin_data.get_today_stock_data(coin_name)
    create_table()  # Create the table

    # Insert sample data
    insert_data(current_info, change_point)

    # Fetch and display the data
    fetch_data()

    # Close the connection
    close_connection()
