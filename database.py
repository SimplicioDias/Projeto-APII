import sqlite3
import datetime
from funcoes import leiaInt
connection = sqlite3.connect('BancoDeDados.db')
cursor = connection.cursor()
def createTable():
    cursor.execute('CREATE TABLE IF NOT EXISTS usuários (nome text, idade integer, email text, numero integer, senha text, cidade text, cpf integer, profissão text )')

createTable()

def entradaDeDados( email, numero, senha, cidade, cpf, prof):
    nome = input('Nome: ')
    idade = datetime.datetime.now().year - leiaInt('Ano de nascimento: ')
    if idade < 16:
            print('Usuário menor de 16 anos não poderá fazer cadastro.')
            return 'Sair do Sistema'
    email = input('Email: ')
    numero = leiaInt('Número [Somente números]: ')
    senha = input('Senha: ')
    cidade = input('Cidade:')
    cpf = leiaInt('CPF [Somente números]')
    prof = input('Profissão: ')
            
    cursor.execute("INSERT INTO usuários VALUES ()")   
     
    connection.commit()