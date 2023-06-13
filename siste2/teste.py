from func import *
import database
clientes = client()
dadosC = {}
profissionais = prof()

cabeçalho('BEM VINDO')
while True:
    opc = menu(['Sing Up', 'Login'])
    if opc == 1:
        cad = singUp()
        clientes.append(cad)
        print(clientes)
    elif opc == 2:
        validador = login()
        for e in clientes:
            if validador[0] == e['email'] and validador[1] == e['senha']:
                print('Logado.')
                cabeçalho(f'Cliente {e["nome"]}')
                while True:
                    cabeçalho('Outsourcing Contractors'.upper())
                    opcao = menu(['Buscar Profissional', 'Atualizar cadastro', 'Apagar meu cadastro','Voltar'])
                    if opcao == 1:
                            database.buscarUser()
                    elif opcao == 2:
                        database.atualizaCadastro()
                    elif opcao == 3:
                        database.apagaCadastro()
                    elif opcao == 4:
                        break
                    else: cabeçalho(f'\033[0;31m{opcao} é uma opção inválida.\nInforme a opção desejada corretamente\033[m')
                    
                    
        for e in profissionais:
            if validador[0] == e['email'] and validador[1] == e['senha']:
                print('Logado.')
                cabeçalho(f'Profissional {e["nome"]}')
                while True:
                    cabeçalho('Outsourcing Contractors'.upper())
                    opcao = menu(['Atualizar informações', 'Apagar meu cadastro','ver buscas [notificação]'])
                    if opcao == 1:
                        database.atualizaCadastro()
                    elif opcao == 2:
                        database.apagaCadastro()
                    elif opcao == 3:
                        cabeçalho('EM BREVE')
                    elif opcao == 4:
                        break
                    else: cabeçalho(f'\033[0;31m{opcao} é uma opção inválida.\nInforme a opção desejada corretamente\033[m')
                    
                            
    
        
        
    