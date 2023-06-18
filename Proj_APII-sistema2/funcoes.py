import datetime
from metdPickle import *


def menu(lista):
    print(linha())
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(linha())
    entrada = leiaInt('\033[32mSua Opção: \033[m')
    return entrada

def linha(tam=200):
    #tam 50
    return '-' * tam

def cabeçalho(txt):

    print(linha())
    print(txt.center(180))
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
    dados = {}
    
    if button == 1:
        dados["nome"] = input('\033[33mNome:\033[m').capitalize()
        dados["idade"] = datetime.datetime.now().year-leiaInt('\033[33mAno de nascimento:\033[m')
        dados["cidade"] = input('\033[33mCidade:\033[m').capitalize()
        dados["email"] = input('\033[33mEmail:\033[m')
        dados["senha"] = input('\033[33mSenha:\033[m')
        adicionarDados("clientes.dat", dados)
        dados.clear()
    
    elif button == 2:
        dados["nome"] = input('\033[33mNome:\033[m').capitalize()
        dados["idade"] = datetime.datetime.now().year-leiaInt('\033[33mAno de nascimento:\033[m')
        dados["cidade"] = input('\033[33mCidade:\033[m').capitalize()
        dados["número"] = leiaInt('\033[33mNúmero < Somente números >\033[m: ')
        dados["email"] = input('\033[33mEmail:\033[m')
        dados["senha"] = input('\033[33mSenha:\033[m')
        dados["profissão"] = input('\033[33mProfissão:\033[m').capitalize()
        dados["descrição"] = input('\033[33mDescrição do Trabalho:\033[m')
        dados["preço"] = input('\033[33mPreço do serviço:\033[m') 
        adicionarDados("profissionais.dat", dados)
        dados.clear()


"""

l1 = [
{'nome': 'Ana', 'idade': 29, 'cidade': 'Juazeiro', 'email': 'ana1@ana.com', 'senha': 'ana28'}, {'nome': 'Natan', 'idade': 20, 'cidade': 'Crato', 'email': 'natan@natan.com', 'senha': 'natan20'}, 
{'nome': 'Simplício', 'idade': 20, 'cidade': 'Caririaçu', 'email': 'simp@simp.com', 'senha': 'simp19'},
{}

]


l2 = [
{'nome': 'Ana', 'idade': 29, 'cidade': 'Juazeiro', 'número': 88987546780, 'email': 'ana@ana.com', 'senha': 'ana29', 'profissão': 'Faxineira', 'descrição': 'Sou faxineira a 7 anos. Faço faxina completa, atualmente autônoma morando no Crato', 'preço': 'R$ 25,00 por dia + taxa de viagem (negociável)'},
{'nome': 'José', 'idade': 38, 'cidade': 'Jauzeiro', 'número': 88975674530, 'email': 'jose@j.com', 'senha': 'jose85', 'profissão': 'Pedreiro', 'descrição': 'Sou pedreiro a 10 anos, especializado em construção de casas, atualmente residindo em Juazeiro, também trabalho faço empeleitamento', 'preço': 'R$ 90,00 diária, + taxa de transporte + ajudantes | támbem é possível empeleitamento negocioável com o cliente'}, 
{'nome': 'Lara', 'idade': 22, 'cidade': 'Juazeiro', 'número': 88975678670, 'email': 'lara@l.com', 'senha': 'lara22', 'profissão': 'Advogada', 'descrição': 'Sou recem formada em Direito, por enquanto estou tentando seguir solo no ramo na advocacia, sou muito dedicada aos estudos. Não pesem que só por ser recem formada me falta experiência, sou muito boa no que faço !', 'preço': 'depende do caso. consigo negociar com o cliente'}, 
{'nome': 'Maria', 'idade': 33, 'cidade': 'Crato', 'número': 88923456670, 'email': 'maria@m.com', 'senha': 'maria90', 'profissão': 'Faxineira', 'descrição': 'Trabalho com faxina a 10 anos, já fui empregada mas hoje estou sem emprego. Faço todo tipo de faxina domiciliar, maior atuação na cidade do Crato.', 'preço': 'R$ 27,00 acrésimo de transporte e taxa de produtos (se os produtos forem meus)'},
{}

]


"""

