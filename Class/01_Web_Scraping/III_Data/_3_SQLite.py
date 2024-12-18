import sqlite3

# Step 1: Connect to the SQLite database (or create it if it doesn't exist)
db_name = "example.db"
conn = sqlite3.connect(db_name)
cursor = conn.cursor()

# Step 2: Create a table
def create_table():
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            age INTEGER,
            email TEXT
        )
    ''')
    print("Table 'users' created successfully.")

# Step 3: Insert data into the table
def insert_data(name, age, email):
    cursor.execute('''
        INSERT INTO users (name, age, email) 
        VALUES (?, ?, ?)
    ''', (name, age, email))
    conn.commit()
    print(f"Inserted {name}, {age}, {email} into the table.")

# Step 4: Fetch data from the table
def fetch_data():
    cursor.execute('SELECT * FROM users')
    rows = cursor.fetchall()
    print("\nFetched Data:")
    for row in rows:
        print(row)

# Step 5: Close the connection
def close_connection():
    conn.close()
    print("\nDatabase connection closed.")

# Main workflow
create_table()  # Create the table

# Insert sample data
insert_data("Alice", 25, "alice@example.com")
insert_data("Bob", 30, "bob@example.com")
insert_data("Charlie", 35, "charlie@example.com")

# Fetch and display the data
fetch_data()

# Close the connection
close_connection()
