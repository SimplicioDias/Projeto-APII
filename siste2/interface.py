

def linha(tam=50):
    return '-' * tam

def cabeçalho(txt):
    """Cabeçalho padrão do sistema sugerido.
    """
    print(linha())
    print(txt.center(50))
    print(linha())

def leiaInt(msg):
    """Método de receber do teclado um número inteiro válido.
    Só aceitará inteiros válidos (numéricos)

    Args:
        msg (str): usado com o mesmo objetivo do 'input()'
    Returns:
        int: retorna um número inteiro, se válido
        senão mostra um ERRO e pede uam entrada válida novamente
    """
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO user preferiu não informar os dados\033[m') 
            #return 'SAIR SISTEMA'
        else: return n
