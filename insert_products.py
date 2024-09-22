import sqlite3

conn = sqlite3.connect('pdv_lanchonete.db')
cursor = conn.cursor()

# Inserir produtos
produtos = [
    ('Hambúrguer', 10.0),
    ('Batata Frita', 5.0),
    ('Refrigerante', 3.5)
]
cursor.executemany('INSERT INTO produtos (nome, preco) VALUES (?, ?)', produtos)

# Inserir clientes
clientes = [
    ('João', '9999-8888', 'Rua A, 123'),
    ('Maria', '7777-6666', 'Rua B, 456')
]
cursor.executemany('INSERT INTO clientes (nome, telefone, endereco) VALUES (?, ?, ?)', clientes)

# Inserir funcionários
funcionarios = [
    ('Ana', 'Atendente'),
    ('Pedro', 'Caixa')
]
cursor.executemany('INSERT INTO funcionarios (nome, cargo) VALUES (?, ?)', funcionarios)

conn.commit()
conn.close()

print("Dados inseridos com sucesso.")
