import os
import sqlite3
import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

# Caminho do banco de dados
DB_PATH = r"C:\Users\998096\Documents\python\tkinter\DATA\vendas.db"
os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)

# Conectar e criar tabelas
conn = sqlite3.connect(DB_PATH)
c = conn.cursor()
c.execute('''CREATE TABLE IF NOT EXISTS usuarios (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario TEXT UNIQUE,
    senha TEXT
)''')
c.execute('''CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    preco REAL,
    estoque INTEGER
)''')
c.execute('''CREATE TABLE IF NOT EXISTS vendas (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    itens TEXT,
    total REAL
)''')
conn.commit()

# Inserir usuário padrão e dados iniciais
try:
    c.execute("INSERT INTO usuarios (usuario, senha) VALUES (?, ?)", ("admin", "admin"))
    c.executemany("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", [
        ("Mouse Gamer", 99.90, 10),
        ("Teclado Mecânico", 199.90, 5),
        ("Monitor 24\"", 899.90, 3)
    ])
    c.execute("INSERT INTO vendas (data, itens, total) VALUES (?, ?, ?)",
              (datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Mouse Gamer (2) - R$199.8", 199.8))
    conn.commit()
except sqlite3.IntegrityError:
    pass

# Fechar conexão inicial
conn.close()

# Funções auxiliares
def conectar_db():
    return sqlite3.connect(DB_PATH)

# Janela principal
class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Sistema de Vendas")
        self.login_frame()

    def login_frame(self):
        self.clear()
        frame = ttk.Frame(self.root, padding=20)
        frame.pack()

        ttk.Label(frame, text="Usuário:").pack()
        self.usuario_entry = ttk.Entry(frame)
        self.usuario_entry.pack()

        ttk.Label(frame, text="Senha:").pack()
        self.senha_entry = ttk.Entry(frame, show="*")
        self.senha_entry.pack()

        ttk.Button(frame, text="Entrar", command=self.verificar_login).pack(pady=10)

    def verificar_login(self):
        usuario = self.usuario_entry.get()
        senha = self.senha_entry.get()
        conn = conectar_db()
        c = conn.cursor()
        c.execute("SELECT * FROM usuarios WHERE usuario=? AND senha=?", (usuario, senha))
        if c.fetchone():
            self.tela_principal()
        else:
            messagebox.showerror("Erro", "Usuário ou senha incorretos")
        conn.close()

    def tela_principal(self):
        self.clear()
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True)

        self.cadastro_tab(notebook)
        self.vendas_tab(notebook)
        self.ver_produtos_tab(notebook)
        self.vendas_realizadas_tab(notebook)

    def cadastro_tab(self, notebook):
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Cadastro de Produtos")

        ttk.Label(frame, text="Nome:").grid(row=0, column=0)
        self.nome_produto = ttk.Entry(frame)
        self.nome_produto.grid(row=0, column=1)

        ttk.Label(frame, text="Preço:").grid(row=1, column=0)
        self.preco_produto = ttk.Entry(frame)
        self.preco_produto.grid(row=1, column=1)

        ttk.Label(frame, text="Estoque:").grid(row=2, column=0)
        self.estoque_produto = ttk.Entry(frame)
        self.estoque_produto.grid(row=2, column=1)

        ttk.Button(frame, text="Cadastrar", command=self.salvar_produto).grid(row=3, column=0, columnspan=2, pady=5)

    def salvar_produto(self):
        nome = self.nome_produto.get()
        try:
            preco = float(self.preco_produto.get())
            estoque = int(self.estoque_produto.get())
        except ValueError:
            messagebox.showerror("Erro", "Preço ou estoque inválido")
            return

        conn = conectar_db()
        c = conn.cursor()
        c.execute("INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)", (nome, preco, estoque))
        conn.commit()
        conn.close()

        messagebox.showinfo("Sucesso", "Produto cadastrado")
        self.nome_produto.delete(0, 'end')
        self.preco_produto.delete(0, 'end')
        self.estoque_produto.delete(0, 'end')
        self.carregar_produtos()

    def vendas_tab(self, notebook):
        self.carrinho = []
        frame = ttk.Frame(notebook, padding=10)
        notebook.add(frame, text="Vendas")

        self.produto_combo = ttk.Combobox(frame, state="readonly")
        self.produto_combo.grid(row=0, column=0)

        self.qtd_entry = ttk.Entry(frame, width=5)
        self.qtd_entry.grid(row=0, column=1)
        self.qtd_entry.insert(0, "1")

        ttk.Button(frame, text="Adicionar", command=self.adicionar_ao_carrinho).grid(row=0, column=2, padx=5)

        self.lista_carrinho = tk.Listbox(frame, width=60)
        self.lista_carrinho.grid(row=1, column=0, columnspan=3, pady=5)

        ttk.Button(frame, text="Finalizar Venda", command=self.finalizar_venda).grid(row=2, column=0, columnspan=3, pady=5)

        self.carregar_produtos()

    def carregar_produtos(self):
        conn = conectar_db()
        c = conn.cursor()
        c.execute("SELECT id, nome, preco, estoque FROM produtos")
        self.produtos = c.fetchall()
        nomes = [f"{p[1]} - R${p[2]:.2f} (Estoque: {p[3]})" for p in self.produtos]
        self.produto_combo['values'] = nomes
        conn.close()

    def adicionar_ao_carrinho(self):
        index = self.produto_combo.current()
        if index == -1:
            return
        try:
            qtd = int(self.qtd_entry.get())
        except ValueError:
            messagebox.showerror("Erro", "Quantidade inválida")
            return
        produto = self.produtos[index]
        if qtd > produto[3]:
            messagebox.showwarning("Estoque", "Estoque insuficiente")
            return
        total = qtd * produto[2]
        self.carrinho.append((produto[0], produto[1], qtd, total))
        self.lista_carrinho.insert('end', f"{produto[1]} x{qtd} - R${total:.2f}")

    def finalizar_venda(self):
        if not self.carrinho:
            return
        total = sum([item[3] for item in self.carrinho])
        resumo = "\n".join([f"{item[1]} ({item[2]}) - R${item[3]:.2f}" for item in self.carrinho])
        data = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        conn = conectar_db()
        c = conn.cursor()
        for item in self.carrinho:
            c.execute("UPDATE produtos SET estoque = estoque - ? WHERE id = ?", (item[2], item[0]))
        c.execute("INSERT INTO vendas (data, itens, total) VALUES (?, ?, ?)", (data, resumo, total))
        conn.commit()
        conn.close()

        messagebox.showinfo("Venda", f"Venda finalizada! Total: R${total:.2f}")
        self.lista_carrinho.delete(0, 'end')
        self.carrinho.clear()
        self.carregar_produtos()
        self.atualizar_listagens()

    def ver_produtos_tab(self, notebook):
        self.produtos_frame = ttk.Frame(notebook, padding=10)
        notebook.add(self.produtos_frame, text="Produtos Cadastrados")
        self.tree_produtos = ttk.Treeview(self.produtos_frame, columns=("nome", "preco", "estoque"), show="headings")
        self.tree_produtos.heading("nome", text="Nome")
        self.tree_produtos.heading("preco", text="Preço")
        self.tree_produtos.heading("estoque", text="Estoque")
        self.tree_produtos.pack(fill='both', expand=True)
        self.atualizar_listagens()

    def vendas_realizadas_tab(self, notebook):
        self.vendas_frame = ttk.Frame(notebook, padding=10)
        notebook.add(self.vendas_frame, text="Vendas Realizadas")
        self.tree_vendas = ttk.Treeview(self.vendas_frame, columns=("data", "itens", "total"), show="headings")
        self.tree_vendas.heading("data", text="Data")
        self.tree_vendas.heading("itens", text="Itens")
        self.tree_vendas.heading("total", text="Total")
        self.tree_vendas.pack(fill='both', expand=True)
        self.atualizar_listagens()

    def atualizar_listagens(self):
        conn = conectar_db()
        c = conn.cursor()

        for row in self.tree_produtos.get_children():
            self.tree_produtos.delete(row)
        c.execute("SELECT nome, preco, estoque FROM produtos")
        for row in c.fetchall():
            self.tree_produtos.insert('', 'end', values=row)

        for row in self.tree_vendas.get_children():
            self.tree_vendas.delete(row)
        c.execute("SELECT data, itens, total FROM vendas ORDER BY id DESC")
        for row in c.fetchall():
            self.tree_vendas.insert('', 'end', values=row)

        conn.close()

    def clear(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# Executar o app
root = tk.Tk()
app = App(root)
root.mainloop()