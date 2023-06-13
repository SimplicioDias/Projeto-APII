from database import *
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
    button = menu(['Cadastrar como cliente', 'Cadastrar como Profissional'])
    if button == 1:
        x = entradaDeDados(1)
        return x
    elif button == 2:
        x = entradaDeDados(2)
        return x




def login():
    valido = []
    user = input('Email: ')
    senha = input('Senha: ')
    valido.append(user)
    valido.append(senha)
    return valido


def client():
    clientes = [{'nome': 'carlos', 'idade': 23, 'cidade': 'Crato', 'email': 'carlos@c.com', 'senha': '123carlos'},
            {'nome': 'mario', 'idade': 25, 'cidade': 'crato', 'email': 'mario@m.com', 'senha': 'mario345'}
            ]
    return clientes
def prof():
    profissionais = [{'nome': 'josé', 'idade': 26, 'cidade': 'Crato', 'email': 'jose@j.com', 'senha': '345jose', 'Profissão': 'cabelereiro', 'Descrição Profissional': 'trabalho com cortes femininos e masculinos, tenho 4 anos de experiência no ramo do corte de cabelo, tenho um salão em Caririaçu bairro Centro Rua X número 453. Também faço cortes a domicílios agendados na cidade', 'Preço': 'Padrão de R$ 25,00 o corte + taxa nos cortes residenciais'},
                 {'nome': 'maria', 'idade': '33', 'cidade': 'Juazeiro', 'email': 'maria123@t.com', 'senha': 'mari345', 'Profissão': 'faxineira', 'Descrição Profissional': 'sou faxineira, trabalho com isso a 5 anos, trabalho em horários variádos a combinar com os clientes', 'Preço': 'R$ 30,00 o dia + taxa de distância'}
                 ]
    return profissionais