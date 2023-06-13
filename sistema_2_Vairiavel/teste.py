from func import *

clientes = [{'nome': 'carlos', 'idade': 23, 'cidade': 'Crato', 'email': 'carlos@c.com', 'senha': '123carlos'},
            {'nome': 'mario', 'idade': 25, 'cidade': 'crato', 'email': 'mario@m.com', 'senha': 'mario345'}
            ]
dadosC = {}
profissionais = [{'nome': 'josé', 'idade': 26, 'cidade': 'Crato', 'email': 'jose@j.com', 'senha': '345jose', 'Profissão': 'cabelereiro', 'Descrição Profissional': 'trabalho com cortes femininos e masculinos, tenho 4 anos de experiência no ramo do corte de cabelo, tenho um salão em Caririaçu bairro Centro Rua X número 453. Também faço cortes a domicílios agendados na cidade', 'Preço': 'Padrão de R$ 25,00 o corte + taxa nos cortes residenciais'},
                 {'nome': 'maria', 'idade': '33', 'cidade': 'Juazeiro', 'email': 'maria123@t.com', 'senha': 'mari345', 'Profissão': 'faxineira', 'Descrição Profissional': 'sou faxineira, trabalho com isso a 5 anos, trabalho em horários variádos a combinar com os clientes', 'Preço': 'R$ 30,00 o dia + taxa de distância'}
                 ]

cabeçalho('BEM VINDO')
opc = menu(['Sing Up', 'Login'])
if opc == 1:
    cad = singUp()
    clientes.append(cad)
elif opc == 2:
    validador = login()
    for e in clientes:
        if validador[0] == e['email'] and validador[1] == e['senha']:
            print('Logado.')
            cabeçalho(f'Cliente {e["nome"]}')
            sist = menu(['Buscar Profissional', 'Atualizar conta', 'sair'])        
    for e in profissionais:
        if validador[0] == e['email'] and validador[1] == e['senha']:
            print('Logado.')
            cabeçalho(f'Profissional {e["nome"]}')
            sist = menu(['Atualizar informações', 'Apagar meu cadastro', 'ver histórico de busca [notificação]'])
                           
    
        
        
        





""" print(clientes)
print(profissionais) """