import sqlite3

connection = sqlite3.connect('my_data.db')

# here you create the cursor
cursor = connection.cursor()

# here you create the table
cursor.execute("""
CREATE TABLE IF NOT EXISTS expenses (
    ID INTEGER PRIMARY_KEY,
    Name TEXT,
    Category TEXT,
    Amount FLOAT
)
""")

# Here you Insert values into the database
cursor.execute(f"""
INSERT INTO expenses VALUES
('1','Paul','Smith','2763'),
('2','Anna','Johnson', 42)
""")


# cursor.execute("""
# SELECT * from expenses
# WHERE Expense_category = 'Smith'
# """)


rows = cursor.fetchall()
print(rows)

for index, row in enumerate(rows):
    print(index, row)

connection.commit()
connection.close()
