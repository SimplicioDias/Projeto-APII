from funcoes import *
from menu import *
from interface import *
from database import *

#createTable()

while True:
    opcao = menuInicial(['Cadastrar', 'Entrar', 'Encerrar'])
    if opcao == 1:
        cadastrar()
        quest = int(input('1 - Entrar\n2 - Sair\n'))
        if quest == 1:
            print('entrarSistema()')
        else: 
            cabeçalho('SISTEMA ENCERRADO')
            break
    elif opcao == 2:
        print('entrarSistema()')
    elif opcao == 3:
        cabeçalho('SISTEMA ENCERRADO')
        break
    else: cabeçalho(f'{opcao} é uma opção inválida.\nInforme a opção desejada corretamente')


#teste

#teste1
