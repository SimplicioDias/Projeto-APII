def linha(tam=42):
    return '-' * tam

def cabeçalho(txt):
    print(linha())
    print(txt.center(42))
    print(linha())

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO user preferiu não informar os dados\033[m') 
            return 3
        else: return n

def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
        
    print(linha())
    opc = leiaInt('\033[32mSua Opção: \033[m')
    return opc