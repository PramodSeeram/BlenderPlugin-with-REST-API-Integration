import sqlite3

DATABASE = 'inventory.db'

def create_db():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS items
                 (id INTEGER PRIMARY KEY AUTOINCREMENT,
                 name TEXT NOT NULL,
                 quantity INTEGER NOT NULL)''')
    conn.commit()
    conn.close()

def add_item(name, quantity):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('INSERT INTO items (name, quantity) VALUES (?, ?)', (name, quantity))
    conn.commit()
    conn.close()

def remove_item(name):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('DELETE FROM items WHERE name = ?', (name,))
    conn.commit()
    conn.close()

def update_quantity(name, quantity):
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('UPDATE items SET quantity = ? WHERE name = ?', (quantity, name))
    conn.commit()
    conn.close()

def get_inventory():
    conn = sqlite3.connect(DATABASE)
    c = conn.cursor()
    c.execute('SELECT * FROM items')
    rows = c.fetchall()
    conn.close()
    return rows
