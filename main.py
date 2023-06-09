from funcoes import *
from menu import *
from interface import *
from database import *

#createTable()

while True:
    cabeçalho('BEM VINDO')
    opcao = menu(['Cadastrar', 'Entrar', 'Encerrar'])
    if opcao == 1:
        cadastrar()
        while True:
            quest = menu(['Entrar','Sair'])
            if quest == 1:
                entrarSistema()
            elif quest == 2:
                break
            else: cabeçalho(f'\033[0;31m{quest} é uma opção inválida.\nInforme a opção desejada corretamente\033[m')
    elif opcao == 2:
        entrarSistema()
        cabeçalho('SISTEMA ENCERRADO')
        break
    elif opcao == 3:
        cabeçalho('SISTEMA ENCERRADO')
        break
    else: cabeçalho(f'\033[0;31m{opcao} é uma opção inválida.\nInforme a opção desejada corretamente\033[m')
    
