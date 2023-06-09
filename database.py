import sqlite3
import datetime
from interface import *
from menu import *


def createTable():
    """
    Função que cria a tabela 'users' no banco de dados 'BancoDeDados.db'.
    """
    connection = sqlite3.connect('BancoDeDados.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS users (NOME text, IDADE integer, EMAIL text, NUMERO integer, SENHA text, CIDADE text, CPF integer, TRABALHO text )')


def deleteTable():
    """
    Deleta a tabela
    """
    connection = sqlite3.connect('BancoDeDados.db')
    cursor = connection.cursor()
    cursor.execute("DROP TABLE IF EXISTS cadastro")
    connection.commit()
    connection.close()


def deleteAllDados():
    """
    Deleta todos os dados de uma tabela
    """
    connection = sqlite3.connect('BancoDeDados.db')
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users ") # WHERE se deseja deletar parcialmente, sem WHERE deleta tudo
    connection.commit()
    connection.close()
    

def entradaDeDados():
    """
    recebe os dados de cadastrais para inserir na tabela 'users' no bd.
    """
    connection = sqlite3.connect('BancoDeDados.db')
    cursor = connection.cursor()
    nome = input('\033[33mNome:\033[m').capitalize()
    idade = datetime.datetime.now().year-leiaInt('\033[33mAno de nascimento:\033[m')
    email = input('\033[33mEmail:\033[m')
    numero = leiaInt('\033[33mNúmero < Somente números >\033[m: ')
    senha = input('\033[33mSenha:\033[m')
    cidade = input('\033[33mCidade:\033[m').capitalize()
    cpf = leiaInt('\033[33mCPF < Somente números >\033[m: ')
    prof = input('\033[33mtrabalho:\033[m').capitalize()       
    cursor.execute("INSERT INTO users VALUES ('"+nome+"',"+str(idade)+",'"+email+"',"+str(numero)+",'"+senha+"','"+cidade+"',"+str(cpf)+",'"+prof+"')")      
    connection.commit()
    connection.close()


def atualizaCadastro():
    """
    Modifica/Atualiza os dados do usuário que são permitidos pelo sistema.
    """
    connection = sqlite3.connect('BancoDeDados.db')
    cursor = connection.cursor()
    while True:
        cabeçalho('Opções de atualização')
        att = menu(['Email','Número','Senha','Cidade','Trabalho', 'Sair'])
        if att == 1:
            quest = input('\033[33mNovo Email:\033[m ')
            cpf = leiaInt('\033[33mCPF p/ confirmarção:\033[m ')
            cursor.execute("UPDATE users SET email='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()  
            cabeçalho(f'\033[32mAtualizado\033[m')
        elif att == 2:
            quest = leiaInt('\033[33mNovo Número:\033[m ')
            cpf = leiaInt('\033[33mCPF p/ confirmarção:\033[m ')
            cursor.execute("UPDATE users SET numero='"+str(quest)+"'WHERE cpf="+str(cpf)+"")
            connection.commit()   
            cabeçalho(f'\033[32mAtualizado\033[m')
        elif att == 3:
            quest = input('\033[33mNova Senha:\033[m ')
            cpf = leiaInt('\033[33mCPF p/ confirmarção:\033[m')
            cursor.execute("UPDATE users SET senha='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()
            cabeçalho(f'\033[32mAtualizado\033[m')
        elif att == 4:
            quest = input('\033[33mNova Cidade:\033[m ').capitalize()
            cpf = leiaInt('\033[33mCPF p/ confirmarção:\033[m')
            cursor.execute("UPDATE users SET cidade='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()
            cabeçalho(f'\033[32mAtualizado.\033[m')
        elif att == 5:
            quest = input('\033[33mNovo Trabalho:\033[m ').capitalize()
            cpf = leiaInt('\033[33mCPF p/ confirmarção:\033[m')
            cursor.execute("UPDATE users SET profissão='"+quest+"'WHERE cpf="+str(cpf)+"")
            connection.commit()
            cabeçalho(f'\033[32mAtualizado\033[m')
        elif att == 6:
            cabeçalho('\033[32mAtualização Finalizada\033[m')
            break
        else: 
            cabeçalho(f'{att} é uma opção inválida.\nInforme a opção desejada corretamente')
    connection.close()


def apagaCadastro():
    """
    Apaga o cadastro do usuário que deseja remever-se do sistema.
    """
    connection = sqlite3.connect('BancoDeDados.db')
    cursor = connection.cursor()
    cabeçalho('APAGANDO CADASTRO')
    cpf = leiaInt('\033[33mCPF p/ confirmarção [Irá deletar o Usuário]:\033[m ')
    cursor.execute("DELETE FROM users WHERE cpf ="+str(cpf)+"")
    opc = input('\033[33mTem certerza que quer continuar [S/N]?\033[m ').upper().strip()
    if opc == 'S':
        connection.commit()
        cabeçalho(f'Usuário de CPF: \033[32m{cpf}\033[m teve os dados apagado')
    else:
        cabeçalho('\033[32mUsuário mantido\033[m')
    connection.close()


def buscarUser():
    """Faz a busca nos dados, usado para encontrar o profissional desejado.
    """
    connection = sqlite3.connect('BancoDeDados.db')
    cursor = connection.cursor()
    while True:
        cabeçalho('ÁREA DE BUSCA')
        opcao = menu(['Buscar por nome', 'Buscar por email', 
                      'Buscar por numero', 'Buscar por cidade', 
                      'Buscar por profissão', 'Voltar'])
        
        if opcao == 1:
            sql = 'SELECT * FROM users WHERE nome = ?'
            busca = input('\033[33mInoforme o nome que deseja buscar:\033[m').capitalize()
            for linha in cursor.execute(sql, (busca,)):
                cabeçalho(f'Nome: {linha[0]}\nIdade: {linha[1]} anos\nEmail: {linha[2]}\nnúmero: {linha[3]}\nCidade: {linha[5]}\nTrabalho: {linha[7]}')
        
        elif opcao == 2:
            sql = 'SELECT * FROM users WHERE email = ?'
            busca = input('\033[33mInoforme o email de quem deseja buscar:\033[m')
            for linha in cursor.execute(sql, (busca,)):
                cabeçalho(f'Nome: {linha[0]}\nIdade: {linha[1]} anos\nEmail: {linha[2]}\nnúmero: {linha[3]}\nCidade: {linha[5]}\nTrabalho: {linha[7]}')
        
        elif opcao == 3:
            sql = 'SELECT * FROM users WHERE numero = ?'
            busca = leiaInt('\033[33mInoforme o Número de quem deseja buscar:\033[m')
            for linha in cursor.execute(sql, (busca,)):
                cabeçalho(f'Nome: {linha[0]}\nIdade: {linha[1]} anos\nEmail: {linha[2]}\nnúmero: {linha[3]}\nCidade: {linha[5]}\nTrabalho: {linha[7]}')
        
        elif opcao == 4:
            sql = 'SELECT * FROM users WHERE cidade = ?'
            busca = input('\033[33mInoforme a cidade que deseja buscar:\033[m').capitalize()
            for linha in cursor.execute(sql, (busca,)):
                cabeçalho(f'Nome: {linha[0]}\nIdade: {linha[1]} anos\nEmail: {linha[2]}\nnúmero: {linha[3]}\nCidade: {linha[5]}\nTrabalho: {linha[7]}')
                
        elif opcao == 5:
            sql = 'SELECT * FROM users WHERE profissão = ?'
            busca = input('\033[33mInoforme a profissão que deseja buscar:\033[m').capitalize()
            for linha in cursor.execute(sql, (busca,)):
                cabeçalho(f'Nome: {linha[0]}\n{linha[1]} anos\nEmail: {linha[2]}\nnúmero: {linha[3]}\nCidade: {linha[5]}\nTrabalho: {linha[7]}')
        elif opcao == 6:
            cabeçalho('\033[32mBUSCA FINALIZADA\033[m')
            break
        else:
            cabeçalho(f'\033[0;31m{opcao} é uma opção inválida.\nInforme a opção desejada corretamente\033[m')
    connection.close()


