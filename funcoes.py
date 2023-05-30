import database
from datetime import datetime
from interface import *
from menu import *



def cadastrar():
    database.entradaDeDados()
    cabeçalho('\033[32mCadastrado com Sucesso!\033[m')
    

def entrarSistema():
    while True:
        cabeçalho('Outsourcing Contractors'.upper())
        opcao = menu(['Buscar', 'Atualizar cadastro', 'Apagar meu cadastro','Voltar'])
        if opcao == 1:
                database.buscarUser()
        elif opcao == 2:
            database.atualizaCadastro()
        elif opcao == 3:
            database.apagaCadastro()
        elif opcao == 4:
            break
        else: cabeçalho(f'\033[0;31m{opcao} é uma opção inválida.\nInforme a opção desejada corretamente\033[m')

