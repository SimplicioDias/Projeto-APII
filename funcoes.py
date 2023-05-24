import database
from datetime import datetime
from interface import *
from menu import *



def cadastrar():
    database.entradaDeDados()
    cabeçalho('Cadastrado com Sucesso!')
    

def entrarSistema():
    while True:
        cabeçalho('<NOME PROJ>')
        opcao = menu(['Buscar', 'Atualizar cadastro', 'Apagar cadastro','Voltar'])
        if opcao == 1:
                print('menuBusca()')
        elif opcao == 2:
            database.atualizaCadastro()
        elif opcao == 3:
            database.apagaCadastro()
        elif opcao == 4:
            break
        else: cabeçalho(f'{opcao} é uma opção inválida.\nInforme a opção desejada corretamente')
            

