import interface

def menu(lista):
    """Método de menu, gera opções para serem selecionadas
    automaticamente baseado no número de opções tratadas como
    elementos de uma lista

    Args:
        lista (list()): recebe uma lista com n elementos, sendo
        cada um deles uma opção do menu

    Returns:
        int: retorna o número da opção selecionada
    """
    print(interface.linha())
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(interface.linha())
    entrada = interface.leiaInt('\033[32mSua Opção: \033[m')
    return entrada
