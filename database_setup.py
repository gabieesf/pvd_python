import sqlite3

# Conectar ao banco de dados (ou criar se não existir)
conn = sqlite3.connect('pdv_lanchonete.db')
cursor = conn.cursor()

# Criação da tabela de produtos
cursor.execute('''
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    preco REAL NOT NULL
)
''')

# Criação da tabela de clientes
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    telefone TEXT UNIQUE,
    endereco TEXT
)
''')

# Criação da tabela de funcionários
cursor.execute('''
CREATE TABLE IF NOT EXISTS funcionarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL UNIQUE,
    cargo TEXT NOT NULL
)
''')

# Criação da tabela de vendas
cursor.execute('''
CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    cliente_id INTEGER,
    funcionario_id INTEGER,
    data_venda TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id),
    FOREIGN KEY (funcionario_id) REFERENCES funcionarios(id)
)
''')

# Criação da tabela de itens de venda (relacionamento muitos para muitos entre vendas e produtos)
cursor.execute('''
CREATE TABLE IF NOT EXISTS itens_venda (
    venda_id INTEGER,
    produto_id INTEGER,
    quantidade INTEGER,
    preco_unitario REAL,
    PRIMARY KEY (venda_id, produto_id),
    FOREIGN KEY (venda_id) REFERENCES vendas(id),
    FOREIGN KEY (produto_id) REFERENCES produtos(id)
)
''')

conn.commit()
conn.close()

print("Banco de dados criado com sucesso.")
