import tkinter as tk
from tkinter import messagebox, ttk
import sqlite3
from datetime import datetime
import csv

# Função para listar produtos
def listar_produtos():
    conn = sqlite3.connect('pdv_lanchonete.db')
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM produtos')
    produtos = cursor.fetchall()
    conn.close()
    return produtos

# Função para registrar uma venda
def registrar_venda(produto_id, quantidade):
    conn = sqlite3.connect('pdv_lanchonete.db')
    cursor = conn.cursor()
    cursor.execute('SELECT preco FROM produtos WHERE id = ?', (produto_id,))
    preco = cursor.fetchone()[0]
    total = preco * quantidade
    data_venda = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('INSERT INTO vendas (produto_id, quantidade, total, data_venda) VALUES (?, ?, ?, ?)', 
                   (produto_id, quantidade, total, data_venda))
    conn.commit()
    conn.close()
    messagebox.showinfo('Venda Registrada', f'Produto ID: {produto_id}\nQuantidade: {quantidade}\nTotal: R${total:.2f}')

# Função para adicionar um novo produto
def adicionar_produto(nome, preco):
    conn = sqlite3.connect('pdv_lanchonete.db')
    cursor = conn.cursor()
    cursor.execute('INSERT INTO produtos (nome, preco) VALUES (?, ?)', (nome, preco))
    conn.commit()
    conn.close()
    atualizar_lista_produtos()
    messagebox.showinfo('Produto Adicionado', f'Produto {nome} adicionado com sucesso.')

# Função para editar um produto
def editar_produto():
    selecionado = listbox.curselection()
    if selecionado:
        index = selecionado[0]
        produto_id = produtos[index][0]
        nome = nome_entry.get()
        preco = preco_entry.get()
        conn = sqlite3.connect('pdv_lanchonete.db')
        cursor = conn.cursor()
        cursor.execute('UPDATE produtos SET nome=?, preco=? WHERE id=?', (nome, preco, produto_id))
        conn.commit()
        conn.close()
        atualizar_lista_produtos()
        messagebox.showinfo('Produto Atualizado', 'Produto atualizado com sucesso.')
    else:
        messagebox.showerror('Erro', 'Selecione um produto para editar.')

# Função para deletar um produto
def deletar_produto():
    selecionado = listbox.curselection()
    if selecionado:
        index = selecionado[0]
        produto_id = produtos[index][0]
        conn = sqlite3.connect('pdv_lanchonete.db')
        cursor = conn.cursor()
        cursor.execute('DELETE FROM produtos WHERE id=?', (produto_id,))
        conn.commit()
        conn.close()
        atualizar_lista_produtos()
        messagebox.showinfo('Produto Deletado', 'Produto deletado com sucesso.')
    else:
        messagebox.showerror('Erro', 'Selecione um produto para deletar.')

# Função para atualizar a lista de produtos na interface
def atualizar_lista_produtos():
    global produtos
    produtos = listar_produtos()
    produto_var.set([f"{p[0]} - {p[1]} - R${p[2]:.2f}" for p in produtos])

# Função para gerar relatório de vendas
def gerar_relatorio():
    conn = sqlite3.connect('pdv_lanchonete.db')
    cursor = conn.cursor()
    cursor.execute('''
    SELECT vendas.id, produtos.nome, vendas.quantidade, vendas.total, vendas.data_venda 
    FROM vendas 
    INNER JOIN produtos ON vendas.produto_id = produtos.id
    ''')
    vendas = cursor.fetchall()
    conn.close()

    with open('relatorio_vendas.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['ID da Venda', 'Nome do Produto', 'Quantidade', 'Total', 'Data da Venda'])
        writer.writerows(vendas)

    messagebox.showinfo('Relatório Gerado', 'Relatório de vendas gerado com sucesso!')

# Função para cadastrar um novo produto
def cadastrar_produto():
    nome = nome_entry.get()
    try:
        preco = float(preco_entry.get())
        adicionar_produto(nome, preco)
    except ValueError:
        messagebox.showerror('Erro', 'Digite um preço válido.')

# Função para registrar a venda
def vender_produto():
    selecionado = listbox.curselection()
    if selecionado:
        index = selecionado[0]
        produto_id = produtos[index][0]
        try:
            quantidade = int(quantidade_entry.get())
            registrar_venda(produto_id, quantidade)
        except ValueError:
            messagebox.showerror('Erro', 'Digite uma quantidade válida.')
    else:
        messagebox.showerror('Erro', 'Selecione um produto para vender.')

# Interface Gráfica
root = tk.Tk()
root.title('PDV Lanchonete')
root.geometry('500x600')

style = ttk.Style()
style.configure('TLabel', font=('Helvetica', 12))
style.configure('TButton', font=('Helvetica', 12))
style.configure('TEntry', font=('Helvetica', 12))
style.configure('TListbox', font=('Helvetica', 12))

# Frame principal
frame = ttk.Frame(root, padding="10")
frame.pack(fill=tk.BOTH, expand=True)

# Listar produtos
produtos = listar_produtos()
produto_var = tk.StringVar(value=[f"{p[0]} - {p[1]} - R${p[2]:.2f}" for p in produtos])
listbox = tk.Listbox(frame, listvariable=produto_var, height=10, font=('Helvetica', 12))
listbox.grid(row=0, column=0, columnspan=2, pady=10, padx=10)

# Campos para editar e cadastrar produto
nome_label = ttk.Label(frame, text='Nome do Produto:')
nome_label.grid(row=1, column=0, pady=5, sticky=tk.W)
nome_entry = ttk.Entry(frame)
nome_entry.grid(row=1, column=1, pady=5, sticky=tk.EW)

preco_label = ttk.Label(frame, text='Preço do Produto:')
preco_label.grid(row=2, column=0, pady=5, sticky=tk.W)
preco_entry = ttk.Entry(frame)
preco_entry.grid(row=2, column=1, pady=5, sticky=tk.EW)

# Campos para registrar venda
quantidade_label = ttk.Label(frame, text='Quantidade:')
quantidade_label.grid(row=3, column=0, pady=5, sticky=tk.W)
quantidade_entry = ttk.Entry(frame)
quantidade_entry.grid(row=3, column=1, pady=5, sticky=tk.EW)

# Botões de cadastrar, editar, deletar e registrar venda
cadastrar_button = ttk.Button(frame, text='Cadastrar Produto', command=cadastrar_produto)
cadastrar_button.grid(row=4, column=0, columnspan=2, pady=10, sticky=tk.EW)

editar_button = ttk.Button(frame, text='Editar Produto', command=editar_produto)
editar_button.grid(row=5, column=0, pady=10, sticky=tk.EW)

deletar_button = ttk.Button(frame, text='Deletar Produto', command=deletar_produto)
deletar_button.grid(row=5, column=1, pady=10, sticky=tk.EW)

vender_button = ttk.Button(frame, text='Registrar Venda', command=vender_produto)
vender_button.grid(row=6, column=0, columnspan=2, pady=10, sticky=tk.EW)

# Botão para gerar relatório de vendas
relatorio_button = ttk.Button(frame, text='Gerar Relatório de Vendas', command=gerar_relatorio)
relatorio_button.grid(row=7, column=0, columnspan=2, pady=10, sticky=tk.EW)

# Atualizar lista de produtos
atualizar_lista_produtos()

root.mainloop()
