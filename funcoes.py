def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO user preferiu não informar os dados\033[m') 
            #return 'SAIR SISTEMA'
        else: return n