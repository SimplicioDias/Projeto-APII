import sqlite3
from tkinter import Tk, Label, Entry, Button, Text

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

# Criação da interface gráfica
janela = Tk()
janela.title("Sistema de Cadastro")
janela.geometry("400x400")
janela.configure(bg='#222222')

label_nome = Label(janela, text="Nome:", bg='#222222', fg='#ffffff')
label_nome.pack()
entry_nome = Entry(janela)
entry_nome.pack()

label_idade = Label(janela, text="Idade:", bg='#222222', fg='#ffffff')
label_idade.pack()
entry_idade = Entry(janela)
entry_idade.pack()

label_email = Label(janela, text="Email:", bg='#222222', fg='#ffffff')
label_email.pack()
entry_email = Entry(janela)
entry_email.pack()

label_numero = Label(janela, text="Número:", bg='#222222', fg='#ffffff')
label_numero.pack()
entry_numero = Entry(janela)
entry_numero.pack()

label_cidade = Label(janela, text="Cidade:", bg='#222222', fg='#ffffff')
label_cidade.pack()
entry_cidade = Entry(janela)
entry_cidade.pack()

label_profissao = Label(janela, text="Profissão:", bg='#222222', fg='#ffffff')
label_profissao.pack()
entry_profissao = Entry(janela)
entry_profissao.pack()

btn_cadastrar = Button(janela, text="Cadastrar", command=cadastrar_pessoa, bg='#444444', fg='#ffffff')
btn_cadastrar.pack()

label_pesquisa = Label(janela, text="Pesquisar por profissão:", bg='#222222', fg='#ffffff')
label_pesquisa.pack()
entry_pesquisa = Entry(janela)
entry_pesquisa.pack()

btn_pesquisar = Button(janela, text="Pesquisar", command=pesquisar_pessoas_por_profissao, bg='#444444', fg='#ffffff')
btn_pesquisar.pack()

resultado_text = Text(janela, bg='#111111', fg='#ffffff')
resultado_text.pack()

# Criação do banco de dados
criar_banco_dados()

janela.mainloop()
