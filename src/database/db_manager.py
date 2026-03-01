# src/database/db_manager.py
import sqlite3
from datetime import datetime
import os

# Ruta dinámica a la carpeta data (asumiendo que ejecutamos desde la raíz del proyecto)
DB_PATH = os.path.join("data", "tracker.db")

def inicializar_db():
    """Crea la base de datos SQLite y la tabla si no existen."""
    # Nos aseguramos de que la carpeta 'data' exista
    os.makedirs("data", exist_ok=True)
    
    conexion = sqlite3.connect(DB_PATH)
    cursor = conexion.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS historial_precios (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            producto TEXT,
            precio REAL,
            fecha TEXT,
            url TEXT
        )
    ''')
    conexion.commit()
    return conexion

def guardar_en_db(conexion, producto, precio, url):
    """Persiste los datos en la tabla relacional."""
    cursor = conexion.cursor()
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
    cursor.execute('''
        INSERT INTO historial_precios (producto, precio, fecha, url)
        VALUES (?, ?, ?, ?)
    ''', (producto, precio, fecha_actual, url))
    conexion.commit()