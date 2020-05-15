# 03_create_data_sql.py
import sqlite3

conn = sqlite3.connect('links.db')
cursor = conn.cursor()

# inserindo dados na tabela
cursor.execute("""
INSERT INTO python (titulo, link, codigo, descricao)
VALUES ('teste titulo', 'teste link', 'teste codigo','teste descricao')
""")

cursor.execute("""
INSERT INTO python (titulo, link, codigo, descricao)
VALUES ('teste titulo2', 'teste link2', 'teste codigo2','teste descricao2')
""")


# gravando no bd
conn.commit()

print('Dados inseridos com sucesso.')

conn.close()
