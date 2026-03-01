# src/database/db_manager.py
import sqlite3
from datetime import datetime
import os

# Dynamic route
DB_PATH = os.path.join("data", "tracker.db")

def initialize_db():
    """Creates the SQLite database and table if they do not exist."""
    os.makedirs("data", exist_ok=True)
    
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS price_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product TEXT,
            price REAL,
            date TEXT,
            url TEXT
        )
    ''')

    conexion.commit()
    return conexion

def save_to_db(connection, product, price, url):
    """Persists the mathematical data in the relational table."""
    cursor = connection.cursor()
    current_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO price_history (product, price, date, url)
        VALUES (?, ?, ?, ?)
    ''', (product, price, current_date, url))
    connection.commit()
    
