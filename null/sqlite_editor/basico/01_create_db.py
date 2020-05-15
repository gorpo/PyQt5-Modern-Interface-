# 01_create_db.py
import sqlite3

# criando e conectando...
conn = sqlite3.connect('links.db')
# desconectando...
conn.close()
