import sqlite3

def init_db():
    conn = sqlite3.connect('marketplace.db')
    c = conn.cursor()

    # Crear tabla de usuarios
    c.execute('''CREATE TABLE IF NOT EXISTS users (
                 id INTEGER PRIMARY KEY,
                 username TEXT UNIQUE,
                 email TEXT UNIQUE,
                 password TEXT,
                 role TEXT)''')

    # Crear tabla de apps
    c.execute('''CREATE TABLE IF NOT EXISTS apps (
                 id INTEGER PRIMARY KEY,
                 name TEXT,
                 description TEXT,
                 price REAL,
                 link TEXT,
                 publisher_id INTEGER,
                 FOREIGN KEY (publisher_id) REFERENCES users (id))''')

    conn.commit()
    conn.close()

# Inicializar la base de datos al ejecutar este archivo
if __name__ == "__main__":
    init_db()

