import interface



def menu(lista):
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(interface.linha())
    entrada = interface.leiaInt('\033[32mSua Opção: \033[m')
    return entrada

def menuInicial(lista):
    interface.cabeçalho('BEM VINDO')
    
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(interface.linha())
    entrada = interface.leiaInt('\033[32mSua Opção: \033[m')
    return entrada

def menuSystem(lista):

    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(interface.linha())
    entrada = interface.leiaInt('\033[32mSua Opção: \033[m')
    return entrada

def menuBusca(lista):
    interface.cabeçalho('<Procurando usuário>')
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(interface.linha())
    entrada = interface.leiaInt('\033[32mSua Opção: \033[m')
    return entrada
