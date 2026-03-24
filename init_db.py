import sqlite3

DATABASE = "jogos.db"

conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Criar tabela
cursor.execute("""
CREATE TABLE IF NOT EXISTS jogos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    genero TEXT NOT NULL,
    plataforma TEXT NOT NULL,
    ano_lancamento INTEGER NOT NULL,
    quantidade INTEGER NOT NULL
)
""")

# Limpar dados antigos (opcional)
cursor.execute("DELETE FROM jogos")

# Inserir jogos
cursor.executemany("""
INSERT INTO jogos (titulo, genero, plataforma, ano_lancamento, quantidade)
VALUES (?, ?, ?, ?, ?)
""", [
    ("Super Mario Bros", "Plataforma", "Nintendo", 1985, 10),
    ("GTA V", "Ação/Aventura", "PC/PS5/Xbox", 2013, 7),
    ("FIFA 23", "Esporte", "PC/PS5/Xbox", 2022, 15)
])

conn.commit()
conn.close()

print("Banco criado e jogos inseridos com sucesso!")