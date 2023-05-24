import sqlite3
import datetime
from interface import *
from menu import *


connection = sqlite3.connect('BancoDeDados.db')
cursor = connection.cursor()

def createTable():
    cursor.execute('CREATE TABLE IF NOT EXISTS cadastro (NOME text, IDADE integer, EMAIL text, NUMERO integer, SENHA text, CIDADE text, CPF integer, TRABALHO text )')


def entradaDeDados():
    nome = input('Nome: ')
    idade = datetime.datetime.now().year - leiaInt('Ano de nascimento: ')
    email = input('Email: ')
    numero = leiaInt('Número [Somente números]: ')
    senha = input('Senha: ')
    cidade = input('Cidade:')
    cpf = leiaInt('CPF [Somente números]')
    prof = input('trabalho: ')         
    cursor.execute("INSERT INTO users VALUES ('"+nome+"',"+str(idade)+",'"+email+"',"+str(numero)+",'"+senha+"','"+cidade+"',"+str(cpf)+",'"+prof+"')")      
    connection.commit()
    connection.close()
# Dento do Sistema

def atualizaCadastro():
    while True:
        cabeçalho('Opções de atualização')
        att = menu(['Email','Número','Senha','Cidade','Trabalho', 'Sair'])
        if att == 1:
            quest = input('Novo Email: ')
            cpf = leiaInt('CPF p/ confirmarção:')
            cursor.execute("UPDATE users SET email='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()  
            connection.close()
            print(f'Atualizado. NOW:{quest}')
        elif att == 2:
            quest = leiaInt('Novo Número: ')
            cpf = leiaInt('CPF p/ confirmarção:')
            cursor.execute("UPDATE users SET numero='"+str(quest)+"'WHERE cpf="+str(cpf)+"")
            connection.commit() 
            connection.close()  
            print(f'Atualizado. NOW:{quest}')
        elif att == 3:
            quest = input('Nova Senha: ')
            cpf = leiaInt('CPF p/ confirmarção:')
            cursor.execute("UPDATE users SET senha='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()
            connection.close()
            print(f'Atualizado. NOW:{quest}')
        elif att == 4:
            quest = input('Nova Cidade: ')
            cpf = leiaInt('CPF p/ confirmarção:')
            cursor.execute("UPDATE users SET cidade='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()
            connection.close()
            print(f'Atualizado. NOW:{quest}')
        elif att == 5:
            quest = input('Novo Trabalho: ')
            cpf = leiaInt('CPF p/ confirmarção:')
            cursor.execute("UPDATE users SET profissão='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()
            connection.close()
            print(f'Atualizado. NOW:{quest}')
        elif att == 6:
            cabeçalho('Atualização Finalizada')
            connection.close()
            break
        else: cabeçalho(f'{att} é uma opção inválida.\nInforme a opção desejada corretamente')

def apagaCadastro():
    cabeçalho('APAGANDO CADASTRO')
    cpf = leiaInt('CPF p/ confirmarção [Irá deletar o Usuário]: ')
    cursor.execute("DELETE FROM users WHERE cpf ="+str(cpf)+"")
    connection.commit()
    connection.close()
    cabeçalho(f'Usuário de CPF: {cpf} teve os dados apagado')


def buscar():
    cabeçalho('ÁREA DE BUSACA')


