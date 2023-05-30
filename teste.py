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
        quest = int(input('\033[33m1 -\033[m \033[34mEntrar\033[m\n\033[33m2 -\033[m \033[34m6\033[m\n'))
        if quest == 1:
            entrarSistema()
        else: 
            cabeçalho('SISTEMA ENCERRADO')
            break
    elif opcao == 2:
        entrarSistema()
             
    elif opcao == 3:
        cabeçalho('SISTEMA ENCERRADO')
        break
    else: cabeçalho(f'''\033[0;31m{opcao} é uma opção inválida.
                    \nInforme a opção desejada corretamente\033[m''')