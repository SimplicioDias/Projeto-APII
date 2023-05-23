import sqlite3
import datetime
from interface import *


connection = sqlite3.connect('BancoDeDados.db')
cursor = connection.cursor()

def createTable():
    cursor.execute('CREATE TABLE IF NOT EXISTS users (nome text, idade integer, email text, numero integer, senha text, cidade text, cpf integer, profissão text )')


def entradaDeDados():
    nome = input('Nome: ')
    idade = datetime.datetime.now().year - leiaInt('Ano de nascimento: ')
    email = input('Email: ')
    numero = leiaInt('Número [Somente números]: ')
    senha = input('Senha: ')
    cidade = input('Cidade:')
    cpf = leiaInt('CPF [Somente números]')
    prof = input('Profissão: ')         
    cursor.execute("INSERT INTO users VALUES ('"+nome+"',"+str(idade)+",'"+email+"',"+str(numero)+",'"+senha+"','"+cidade+"',"+str(cpf)+",'"+prof+"')")      
    connection.commit()
    

