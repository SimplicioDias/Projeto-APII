import sqlite3
from tkinter import Tk, Label, Entry, Button, Text, messagebox

# Função para criar o banco de dados e a tabela "pessoas"
def criar_banco_dados():
    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS pessoas (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            idade INTEGER,
            email TEXT,
            numero TEXT,
            cidade TEXT,
            profissao TEXT
        )
    ''')
    conn.commit()
    conn.close()

# Função para cadastrar uma pessoa
def cadastrar_pessoa():
    nome = entry_nome.get()
    idade = int(entry_idade.get())
    email = entry_email.get()
    numero = entry_numero.get()
    cidade = entry_cidade.get()
    profissao = entry_profissao.get()

    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO pessoas (nome, idade, email, numero, cidade, profissao)
        VALUES (?, ?, ?, ?, ?, ?)
    ''', (nome, idade, email, numero, cidade, profissao))
    conn.commit()
    conn.close()
    resultado_text.insert('end', "Pessoa cadastrada com sucesso!\n")

# Função para pesquisar pessoas por profissão
def pesquisar_pessoas_por_profissao():
    profissao = entry_pesquisa.get()

    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''
        SELECT nome, idade, email, numero, cidade
        FROM pessoas
        WHERE profissao = ?
    ''', (profissao,))
    resultados = cursor.fetchall()
    conn.close()

    if len(resultados) == 0:
        resultado_text.insert('end', "Nenhum profissional encontrado.\n")
    else:
        resultado_text.insert('end', "Profissionais encontrados:\n")
        for resultado in resultados:
            nome, idade, email, numero, cidade = resultado
            resultado_text.insert('end', f"Nome: {nome}\nIdade: {idade}\nEmail: {email}\nNúmero: {numero}\nCidade: {cidade}\n\n")

# Função para remover um cadastro
def remover_cadastro():
    nome = entry_remover.get()

    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''
        DELETE FROM pessoas
        WHERE nome = ?
    ''', (nome,))
    conn.commit()
    conn.close()
    resultado_text.insert('end', f"Cadastro de {nome} removido com sucesso!\n")

# Função para atualizar um cadastro
def atualizar_cadastro():
    nome = entry_atualizar.get()
    profissao = entry_nova_profissao.get()

    conn = sqlite3.connect('cadastro.db')
    cursor = conn.cursor()
    cursor.execute('''
        UPDATE pessoas
        SET profissao = ?
        WHERE nome = ?
    ''', (profissao, nome))
    conn.commit()
    conn.close()
    resultado_text.insert('end', f"Cadastro de {nome} atualizado com sucesso!\n")

# Função para sair do programa
def sair():
    if messagebox.askyesno("Sair", "Deseja sair do programa?"):
        janela.destroy()

# Criação da interface gráfica
janela = Tk()
janela.title("Sistema de Cadastro")
janela.attributes('-fullscreen', True)
janela.configure(bg='#222222')

# Definindo o alinhamento da esquerda para a direita
janela.columnconfigure(0, weight=1)
janela.columnconfigure(1, weight=1)
janela.columnconfigure(2, weight=1)

# Componentes de entrada e rótulos para o cadastro
label_nome = Label(janela, text="Nome:", bg='#222222', fg='#ffffff')
label_nome.grid(row=0, column=0, sticky='e')
entry_nome = Entry(janela)
entry_nome.grid(row=0, column=1, sticky='w')

label_idade = Label(janela, text="Idade:", bg='#222222', fg='#ffffff')
label_idade.grid(row=1, column=0, sticky='e')
entry_idade = Entry(janela)
entry_idade.grid(row=1, column=1, sticky='w')

label_email = Label(janela, text="Email:", bg='#222222', fg='#ffffff')
label_email.grid(row=2, column=0, sticky='e')
entry_email = Entry(janela)
entry_email.grid(row=2, column=1, sticky='w')

label_numero = Label(janela, text="Número:", bg='#222222', fg='#ffffff')
label_numero.grid(row=3, column=0, sticky='e')
entry_numero = Entry(janela)
entry_numero.grid(row=3, column=1, sticky='w')

label_cidade = Label(janela, text="Cidade:", bg='#222222', fg='#ffffff')
label_cidade.grid(row=4, column=0, sticky='e')
entry_cidade = Entry(janela)
entry_cidade.grid(row=4, column=1, sticky='w')

label_profissao = Label(janela, text="Profissão:", bg='#222222', fg='#ffffff')
label_profissao.grid(row=5, column=0, sticky='e')
entry_profissao = Entry(janela)
entry_profissao.grid(row=5, column=1, sticky='w')

# Botão para cadastrar uma pessoa
btn_cadastrar = Button(janela, text="Cadastrar", command=cadastrar_pessoa, bg='#444444', fg='#ffffff')
btn_cadastrar.grid(row=6, column=1, sticky='w')

# Componentes de entrada e rótulo para pesquisar pessoas por profissão
label_pesquisa = Label(janela, text="Pesquisar por profissão:", bg='#222222', fg='#ffffff')
label_pesquisa.grid(row=7, column=0, sticky='e')
entry_pesquisa = Entry(janela)
entry_pesquisa.grid(row=7, column=1, sticky='w')

# Botão para pesquisar pessoas por profissão
btn_pesquisar = Button(janela, text="Pesquisar", command=pesquisar_pessoas_por_profissao, bg='#444444', fg='#ffffff')
btn_pesquisar.grid(row=8, column=1, sticky='w')

# Componentes de entrada e rótulo para remover um cadastro
label_remover = Label(janela, text="Remover cadastro:", bg='#222222', fg='#ffffff')
label_remover.grid(row=9, column=0, sticky='e')
entry_remover = Entry(janela)
entry_remover.grid(row=9, column=1, sticky='w')

# Botão para remover um cadastro
btn_remover = Button(janela, text="Remover", command=remover_cadastro, bg='#444444', fg='#ffffff')
btn_remover.grid(row=10, column=1, sticky='w')

# Componentes de entrada e rótulo para atualizar um cadastro
label_atualizar = Label(janela, text="Nome para atualizar cadastro:", bg='#222222', fg='#ffffff')
label_atualizar.grid(row=11, column=0, sticky='e')
entry_atualizar = Entry(janela)
entry_atualizar.grid(row=11, column=1, sticky='w')

label_nova_profissao = Label(janela, text="Nova profissão:", bg='#222222', fg='#ffffff')
label_nova_profissao.grid(row=12, column=0, sticky='e')
entry_nova_profissao = Entry(janela)
entry_nova_profissao.grid(row=12, column=1, sticky='w')

# Botão para atualizar um cadastro
btn_atualizar = Button(janela, text="Atualizar", command=atualizar_cadastro, bg='#444444', fg='#ffffff')
btn_atualizar.grid(row=13, column=1, sticky='w')

# Área de texto para exibir os resultados
resultado_text = Text(janela, bg='#111111', fg='#ffffff')
resultado_text.grid(row=0, column=2, rowspan=14, sticky='nsew')

# Botão para sair do programa
btn_sair = Button(janela, text="Sair", command=sair, bg='#444444', fg='#ffffff')
btn_sair.grid(row=14, column=1, sticky='w')

# Criação do banco de dados
criar_banco_dados()

# Iniciar a interface gráfica
janela.mainloop()
