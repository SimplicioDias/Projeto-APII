def menu(lista):
    print(linha())
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(linha())
    entrada = leiaInt('\033[32mSua Opção: \033[m')
    return entrada


def linha(tam=50):
    return '-' * tam

def cabeçalho(txt):

    print(linha())
    print(txt.center(50))
    print(linha())

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



def singUp():
    c = []
    dadosC = {}
    profissionais = []

    dadosP = {}
    button = menu(['Cadastrar como cliente', 'Cadastrar como Profissional'])
    if button == 1:
            dadosC['nome'] = input('Digite seu Nome: ')
            dadosC['idade'] = leiaInt('Digite sua Idade: ')
            dadosC['cidade'] = input('Digite sua Cidade: ')
            dadosC['email'] = input('Digite sue Email: ')
            dadosC['senha'] = input('Digite sua senha: ')
            print(f'{dadosC["nome"]} cadastrado com sucesso!')
            c.append(dadosC.copy())
            return c[0]
    elif button == 2:
            dadosP['nome'] = input('Digite seu Nome: ')
            dadosP['idade'] = input('Digite sua Idade: ')
            dadosP['cidade'] = input('Digite sua Cidade: ')
            dadosP['email'] = input('Digite sue Email: ')
            dadosP['senha'] = input('Digite sua senha: ')
            dadosP['Profissão'] = input('Qual sua profissão: ')
            dadosP['Descrição Profissional'] = input('Descrição do seu Trabalho: ')
            dadosP['Preço'] = input('Preço do seu serviço: ')
            print(f'Profissional {dadosP["nome"]} cadastrado com sucesso!')
            profissionais.append(dadosP.copy())
            print(profissionais)
            dadosP.clear()


def login():
    validoC = []
    validoP = []
    button = menu(['Iniciar como Cliente', 'Iniciar como Profissional'])
    if button == 1:
        user = input('Email: ')
        senha = input('Senha: ')
        validoC.append(user)
        validoC.append(senha)
        return validoC
    elif button == 2:
        user = input('Email: ')
        senha = input('Senha: ')
        validoP.append(user)
        validoP.append(senha)
        return validoP
        
    