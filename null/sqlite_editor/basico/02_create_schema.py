# 02_create_schema.py
import sqlite3

# conectando...
conn = sqlite3.connect('links.db')
# definindo um cursor
cursor = conn.cursor()

# criando a tabela (schema)
cursor.execute("""
CREATE TABLE python (
	id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	titulo TEXT NOT NULL,
	link TEXT NOT NULL,
	codigo TEXT NOT NULL,
	descricao  TEXT NOT NULL
	
);
""")

print('Tabela criada com sucesso.')
# desconectando...
conn.close()
