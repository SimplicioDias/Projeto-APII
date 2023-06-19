import datetime
from metdPickle import *


def menu(lista):    #Menu baseado em uma lista de opções
    #Rece uma lista, e enumera todos elementos da lista, que representam opções
    print(linha())
    for pos, item in enumerate (lista):
        print(f'\033[33m{pos+1}\033[33m - \033[34m{item}\033[m')
    print(linha())
    entrada = leiaInt('\033[32mSua Opção: \033[m')
    return entrada

def linha(tam=200): #Printa uma linha
    #Recebe o tamanho como parametro
    #tam 50 -> Padrão
    return '-' * tam

def cabeçalho(txt): # Faz um cabeçalho formatado no terminal
    #recebe uma texto como centro, ou mensagem principal do cabeçalho
    print(linha())
    print(txt.center(180))
    print(linha())

def leiaInt(msg): #Facilita a leitura de um inteiro funcionando como um input
    #Recebe uma mensagem [como um 'input()']
    #Só retorna um inteiro 
    #A Função só encerra quando o usuário digitar um número inteiro válido
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: por favor, digite um número inteiro válido\033[m')
        except KeyboardInterrupt:
            print('\n\033[0;31mO user preferiu não informar os dados\033[m') 
            #return 'SAIR SISTEMA'
        else: return n       


def singUp(): #faz um cadastro e adiciona-o a um arquivo usando pickle
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
{'nome': 'Ana', 'idade': 29, 'cidade': 'Crato', 'email': 'ana@ana.com', 'senha': 'ana1'}, 
{'nome': 'Natan', 'idade': 20, 'cidade': 'Crato', 'email': 'natan@natan.com', 'senha': 'natan20'}, 
{'nome': 'Simplício', 'idade': 20, 'cidade': 'Caririaçu', 'email': 'simp@simp.com', 'senha': 'simp19'},
{'nome': 'Vitória', 'idade': 23, 'cidade': 'Barbalha', 'email': 'Vitoria@vitoria.com', 'senha': 'vi23'},
{'nome': 'Yuri', 'idade': 34, 'cidade': 'Crato', 'email': 'yuri@yuri.com', 'senha': 'yuri89'},
{'nome': 'Maria', 'idade': 24, 'cidade': 'Barbalha', 'email': 'maria@maria.com', 'senha': 'mari99'},

{}

]


l2 = [
{'nome': 'Ana', 'idade': 29, 'cidade': 'Juazeiro', 'número': 88987546780, 'email': 'ana@ana.com', 'senha': 'ana29', 'profissão': 'Faxineira', 'descrição': 'Sou faxineira a 7 anos. Faço faxina completa, atualmente autônoma morando no Crato', 'preço': 'R$ 25,00 por dia + taxa de viagem (negociável)'},
{'nome': 'José', 'idade': 38, 'cidade': 'Jauzeiro', 'número': 88975674530, 'email': 'jose@j.com', 'senha': 'jose85', 'profissão': 'Pedreiro', 'descrição': 'Sou pedreiro a 10 anos, especializado em construção de casas, atualmente residindo em Juazeiro, também trabalho faço empeleitamento', 'preço': 'R$ 90,00 diária, + taxa de transporte + ajudantes | támbem é possível empeleitamento negocioável com o cliente'}, 
{'nome': 'Lara', 'idade': 22, 'cidade': 'Juazeiro', 'número': 88975678670, 'email': 'lara@l.com', 'senha': 'lara22', 'profissão': 'Advogada', 'descrição': 'Sou recem formada em Direito, por enquanto estou tentando seguir solo no ramo na advocacia, sou muito dedicada aos estudos. Não pesem que só por ser recem formada me falta experiência, sou muito boa no que faço !', 'preço': 'depende do caso. consigo negociar com o cliente'}, 
{'nome': 'Maria', 'idade': 33, 'cidade': 'Crato', 'número': 88923456670, 'email': 'maria@m.com', 'senha': 'maria90', 'profissão': 'Faxineira', 'descrição': 'Trabalho com faxina a 10 anos, já fui empregada mas hoje estou sem emprego. Faço todo tipo de faxina domiciliar, maior atuação na cidade do Crato.', 'preço': 'R$ 27,00 acrésimo de transporte e taxa de produtos (se os produtos forem meus)'},
{'nome': 'Roni', 'idade': 33, 'cidade': 'Barbalha', 'número': 88975654090, 'email': 'roni@roni.com', 'senha': 'roni90', 'profissão': 'Pedreiro', 'descrição': 'Trabalho como pedreiro ou ajudante de pedreiro a 3 anos, moro em Barbalha e estou disponível no mercado', 'preço': 'R$ 70,00 diária de pedreiro chefe ou R$ 35,00 diária de servente. Possível acordo de empeleita'},
{'nome': 'Mario ', 'idade': 45, 'cidade': 'Crato', 'número': 88967554320, 'email': 'mario@mario.com', 'senha': 'mario123', 'profissão': 'Freteiro', 'descrição': 'Trabalho fazendo fretes a muito tempo, tenho uma rede de transportes de médio porte para lhe ajudar com sua mudança ou sua carga! entre em contato caso deseje negociar :)', 'preço': 'R$ 50,00 fixo + R$ 5,50/km com descarga incluida'},
{'nome': 'Joaquim', 'idade': 26, 'cidade': 'Caririaçu', 'número': 8876756678, 'email': 'joaquim@j.com', 'senha': 'j97', 'profissão': 'Advogado', 'descrição': 'Sou advogado a 3 anos, atuo no criminal e familiar, tenho escritório em juazeiro, entre em contato cajo precise de um bom advogado', 'preço': 'R$ 100,00 fixo da reunião, + contrato acordado com os clientes, em % do caso'},
{}

]


"""

