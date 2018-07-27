import sqlite3

# name of DB + connection
sqlite_file = "db/FinanceHolderDB.sqlite" 
conn = sqlite3.connect(sqlite_file)

# CREATE finances TABLE
def create_table():
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS finances (
id INTEGER PRIMARY KEY ASC, current_date TEXT, description TEXT,
income_expense TEXT, total REAL)
''')
    c.close()
    
# INSERT new record in finances TABLE
def data_insert(current_date, description, income_expense, total):
    c = conn.cursor()
    c.execute('''INSERT INTO finances (current_date, description,
income_expense, total) VALUES (?, ?, ?, ?)''', (current_date,
                                                description,
                                                income_expense, total))
    conn.commit()
    c.close

# DELETEing record from finances TABLE by ID
def data_remove(idd):
    c = conn.cursor()
    c.execute("DELETE FROM finances WHERE id=?", (idd,))
    conn.commit()
    c.close

# SELECT * records from finances and DISPLAY them in the TABLE
def display_records(tree):
    c = conn.cursor()
    db_rows = c.execute("SELECT * FROM finances ORDER BY id DESC")
    for row in db_rows:
        tree.insert ('', 0, values = (row[0], row[1], row[2], row[3], row[4]))

# SELECT recods from finances by MONTH
def display_records_by_month(tree, selected_month):
    c = conn.cursor()
    #db_rows = c.execute('''SELECT * FROM finances WHERE strftime("%m", t)='07' ORDER BY id DESC''')
    db_rows = c.execute('''SELECT * FROM finances WHERE current_date
LIKE ? ORDER BY id DESC''', ('%-'+selected_month+'-%',))
    for row in db_rows:
        tree.insert ('', 0, values = (row[0], row[1], row[2], row[3], row[4]))

# SELECT recods from finances by INCOME EXPENSE
def display_records_by_income_expense(tree, selected_value):
    c = conn.cursor()
    db_rows = c.execute('''SELECT * FROM finances WHERE income_expense
LIKE ? ORDER BY id DESC''', (selected_value,))
    for row in db_rows:
        tree.insert ('', 0, values = (row[0], row[1], row[2], row[3], row[4]))
               
# UPDATE THIS PART
# every time script is running it will try to create DB    
create_table()
