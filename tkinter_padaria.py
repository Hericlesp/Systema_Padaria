import os
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Caminho do banco de dados
DB_DIR = r"C:\Users\998096\Documents\python\tkinter\DATA"
os.makedirs(DB_DIR, exist_ok=True)
DB_PATH = os.path.join(DB_DIR, "sistema_vendas.db")

# Inicializar o banco de dados
def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()

    cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE,
        password TEXT
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS produtos (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        preco REAL,
        quantidade INTEGER
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        data TEXT,
        total REAL
    )''')

    cursor.execute('''CREATE TABLE IF NOT EXISTS itens_venda (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        venda_id INTEGER,
        produto_nome TEXT,
        preco REAL,
        quantidade INTEGER,
        FOREIGN KEY(venda_id) REFERENCES vendas(id)
    )''')

    # Usuário padrão
    cursor.execute("INSERT OR IGNORE INTO usuarios (username, password) VALUES (?, ?)", ("admin", "admin"))

    conn.commit()
    conn.close()

# Função para login
def login():
    user = username_entry.get()
    pwd = password_entry.get()
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM usuarios WHERE username = ? AND password = ?", (user, pwd))
    result = cursor.fetchone()
    conn.close()
    if result:
        login_frame.pack_forget()
        main_app()
    else:
        messagebox.showerror("Erro de login", "Usuário ou senha inválidos")

# Função para cadastrar produto
def cadastrar_produto():
    nome = nome_entry.get()
    preco = float(preco_entry.get())
    quantidade = int(quantidade_entry.get())

    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO produtos (nome, preco, quantidade) VALUES (?, ?, ?)", (nome, preco, quantidade))
    conn.commit()
    conn.close()

    messagebox.showinfo("Sucesso", "Produto cadastrado!")
    nome_entry.delete(0, tk.END)
    preco_entry.delete(0, tk.END)
    quantidade_entry.delete(0, tk.END)
    listar_produtos()

# Função para adicionar item ao carrinho
def adicionar_ao_carrinho():
    try:
        produto = combo_produtos.get()
        quantidade = int(qtd_venda_entry.get())

        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM produtos WHERE nome = ?", (produto,))
        prod = cursor.fetchone()
        conn.close()

        if prod and prod[3] >= quantidade:
            carrinho.append((produto, prod[2], quantidade))
            carrinho_list.insert('', 'end', values=(produto, f"R$ {prod[2]:.2f}", quantidade))
        else:
            messagebox.showwarning("Estoque insuficiente", "Quantidade indisponível!")
    except Exception as e:
        messagebox.showerror("Erro", str(e))

# Finalizar venda
def finalizar_venda():
    if not carrinho:
        messagebox.showwarning("Carrinho vazio", "Adicione produtos antes de finalizar.")
        return

    total = sum(p[1] * p[2] for p in carrinho)
    data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO vendas (data, total) VALUES (?, ?)", (data, total))
    venda_id = cursor.lastrowid

    for nome, preco, qtd in carrinho:
        cursor.execute("INSERT INTO itens_venda (venda_id, produto_nome, preco, quantidade) VALUES (?, ?, ?, ?)", (venda_id, nome, preco, qtd))
        cursor.execute("UPDATE produtos SET quantidade = quantidade - ? WHERE nome = ?", (qtd, nome))

    conn.commit()
    conn.close()

    carrinho.clear()
    carrinho_list.delete(*carrinho_list.get_children())
    listar_produtos()
    listar_vendas()
    messagebox.showinfo("Venda Finalizada", f"Venda de R$ {total:.2f} registrada.")

# Listar produtos

def listar_produtos():
    for item in lista_produtos.get_children():
        lista_produtos.delete(item)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM produtos")
    for row in cursor.fetchall():
        lista_produtos.insert('', 'end', values=row)
    conn.close()

# Listar vendas

def listar_vendas():
    for item in lista_vendas.get_children():
        lista_vendas.delete(item)
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM vendas")
    for row in cursor.fetchall():
        lista_vendas.insert('', 'end', values=row)
    conn.close()

# Interface principal com abas
def main_app():
    notebook = ttk.Notebook(root)
    notebook.pack(fill='both', expand=True)

    # Página Cadastro
    aba_cadastro = ttk.Frame(notebook)
    notebook.add(aba_cadastro, text="Cadastrar Produto")

    global nome_entry, preco_entry, quantidade_entry

    ttk.Label(aba_cadastro, text="Nome:").pack()
    nome_entry = ttk.Entry(aba_cadastro)
    nome_entry.pack()

    ttk.Label(aba_cadastro, text="Preço:").pack()
    preco_entry = ttk.Entry(aba_cadastro)
    preco_entry.pack()

    ttk.Label(aba_cadastro, text="Quantidade:").pack()
    quantidade_entry = ttk.Entry(aba_cadastro)
    quantidade_entry.pack()

    ttk.Button(aba_cadastro, text="Cadastrar", command=cadastrar_produto).pack(pady=10)

    # Página Vendas
    aba_venda = ttk.Frame(notebook)
    notebook.add(aba_venda, text="Realizar Venda")

    global combo_produtos, qtd_venda_entry, carrinho_list, carrinho
    carrinho = []

    ttk.Label(aba_venda, text="Produto:").pack()
    combo_produtos = ttk.Combobox(aba_venda)
    combo_produtos.pack()

    ttk.Label(aba_venda, text="Quantidade:").pack()
    qtd_venda_entry = ttk.Entry(aba_venda)
    qtd_venda_entry.pack()

    ttk.Button(aba_venda, text="Adicionar ao Carrinho", command=adicionar_ao_carrinho).pack(pady=5)

    carrinho_list = ttk.Treeview(aba_venda, columns=("Produto", "Preço", "Qtd"), show="headings")
    for col in ("Produto", "Preço", "Qtd"):
        carrinho_list.heading(col, text=col)
    carrinho_list.pack(fill='both', expand=True)

    ttk.Button(aba_venda, text="Finalizar Venda", command=finalizar_venda).pack(pady=10)

    # Página Produtos
    aba_lista_produtos = ttk.Frame(notebook)
    notebook.add(aba_lista_produtos, text="Produtos Cadastrados")

    global lista_produtos
    lista_produtos = ttk.Treeview(aba_lista_produtos, columns=("ID", "Nome", "Preço", "Qtd"), show="headings")
    for col in ("ID", "Nome", "Preço", "Qtd"):
        lista_produtos.heading(col, text=col)
    lista_produtos.pack(fill='both', expand=True)

    # Página Vendas Realizadas
    aba_vendas = ttk.Frame(notebook)
    notebook.add(aba_vendas, text="Vendas Realizadas")

    global lista_vendas
    lista_vendas = ttk.Treeview(aba_vendas, columns=("ID", "Data", "Total"), show="headings")
    for col in ("ID", "Data", "Total"):
        lista_vendas.heading(col, text=col)
    lista_vendas.pack(fill='both', expand=True)

    atualizar_combobox_produtos()
    listar_produtos()
    listar_vendas()

# Atualizar Combobox com os produtos

def atualizar_combobox_produtos():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute("SELECT nome FROM produtos")
    nomes = [row[0] for row in cursor.fetchall()]
    combo_produtos["values"] = nomes
    conn.close()

# --- GUI Principal ---
root = tk.Tk()
root.title("Sistema de Vendas")
root.geometry("800x600")

init_db()

login_frame = tk.Frame(root)
login_frame.pack(pady=100)

username_entry = ttk.Entry(login_frame)
username_entry.insert(0, "admin")
username_entry.pack()

password_entry = ttk.Entry(login_frame, show="*")
password_entry.insert(0, "admin")
password_entry.pack()

login_btn = ttk.Button(login_frame, text="Login", command=login)
login_btn.pack(pady=10)

root.mainloop()