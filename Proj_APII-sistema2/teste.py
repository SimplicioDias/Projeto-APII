from funcoes import *


# LINK DO REPOSITÓRIO DO GITHUB : https://github.com/SimplicioDias/Projeto-APII

while True:
    cabeçalho('BEM VINDO')
    
    opc = menu(['Criar conta', 'Login como Cliente', 'Login como Parceiro', 'Apagar meu cadastro', 'Encerrar Sistema'])
    if opc == 1: #Cadastro
        cad = singUp()
        
    elif opc == 2: #Login Client
        email = input('email:')
        senha = input('senha:')
        lc = login('clientes.dat',email, senha)
        
        if lc:
            while True: # SISTEMA VISÃO CLIENTE
                cabeçalho('Click Service'.upper())
                
                opcao = menu(['Buscar por Profissionais', 'Atualizar cadastro', 'Ver meus contratos','Voltar para o Inicio'])
                
                if opcao == 1: #Faz pesquisa de profissionais
                    while True:
                        m = menu(['Procurar profissionais [profissão]: ', 'Contratar profissional', 'Voltar'])
                        db = carregaDados('profissionais.dat')
                        
                        if m == 1:
                            
                            busca = input('informe a profissão que deseja procurar no sistema: ').capitalize()
                            exist = False
                            
                            for e in db:
                                if e['profissão'] == busca:
                                    exist = True
                                    cabeçalho(f'\033[32mNome: {e["nome"]}\nIdade: {e["idade"]}\nCidade: {e["cidade"]}\nDescrição do Profissional: {e["descrição"]}\nPreço: {e["preço"]}\033[m')                              
                                    
                             
                            if exist == False:
                                
                                cabeçalho('\033[0;31mNão foi encontrado esse tipo de profissional no sistema\033[m') 
                                
                        elif m == 2:
                                contrato = input('Informe o nome do Profissional que deseja contratar: ').capitalize()
                                profi = input('Informe a profissão: ').capitalize()
                                ext = False
                                
                                for e in db:
                                    if e['nome'] == contrato and e['profissão'] == profi:
                                        ext = True
                                        cabeçalho(f'\033[32mNome: {e["nome"]}\nIdade: {e["idade"]}\nCidade: {e["cidade"]}\nDescrição do Profissional: {e["descrição"]}\nPreço: {e["preço"]}\033[m')
                                        
                                        q = quest(f'Deseja enviar solicitação de contrato para {e["nome"]} ? [S/N]')
                                        if q:
                                            
                                            cabeçalho(f'\033[32mSolicitação enviada para {e["nome"]}. Aguarde respostas .\033[m')
 
                                        else:
                                            
                                            cabeçalho('\033[31mSolicitação não foi enviada.\033[m')
                                                        
                                if ext == False:
                                    
                                    cabeçalho('\033[0;31mEsse profissional não foi encontrado, verifique os dados.\033[m') 
                        
                        elif m == 3:
                            
                            cabeçalho('\033[32mABusca Finalizada\033[m')
                            break
                                    
                        else:
                            cabeçalho(f'\033[0;31m{m} é uma opção inválida.\033[m')
                            
                elif opcao == 2:   #Configurações de Dados do cliente 
                    while True:
                        cabeçalho('CONFIGURAÇÕES DE CADASTRO')
                        
                        att = menu(['Email','Senha', 'Cidade', 'Sair das configurações'])
                        
                        if att == 1:
                            dado = input('\033[33mEmail atual:\033[m ')
                            new = {'email':input('\033[33mNovo Email:\033[m ')}
                            atualizarDados("clientes.dat",dado, new)                        
                            
                        elif att == 2:
                            dado = input('\033[33mSenha atual:\033[m ')
                            new = {'senha':input('\033[33mNova senha:\033[m ')}
                            atualizarDados("clientes.dat",dado, new)                        
                            
                        elif att == 3:
                            dado = input('\033[33mCidade atual:\033[m ').capitalize()
                            new = {'cidade':input('\033[33mNova Cidade:\033[m ').capitalize()}
                            atualizarDados("clientes.dat",dado, new)                        
                            
                        elif att == 4:
                            
                            cabeçalho('\033[32mAtualização Finalizada\033[m')
                            break
                        
                        else: 
                            cabeçalho(f'\033[0;31m{att} é uma opção inválida.\033[m')
                            
                elif opcao == 3: #Mostra os contratos vigentes
                    cabeçalho('Nenhum contrato encontrado')
                    
                elif opcao == 4:
                    break
                
                else: cabeçalho(f'\033[0;31m{opcao} é uma opção inválida.\033[m')
    
    elif opc == 3:  #Login PRO
        email = input('email:')
        senha = input('senha:')
        lp = login('profissionais.dat', email, senha)
        
        if lp:
            while True: #SISTEMA VISÃO PROFISSIONAL
                cabeçalho('Click Service'.upper())
                opcao = menu(['Atualizar informações', 'Ver meus contratos', 'Ver buscas [notificação]', 'Voltar ao início'])
                
                if opcao == 1: #Configuração de dados do parceiro
                    while True:
                        cabeçalho('CONFIGURAÇÕES DE CADASTRO')
                        
                        at = menu(['Email','Senha', 'Cidade', 'Número', 'Minha profissão','Descrição de trabalho','Preço do serviço','Sair das configurações'])
                        
                        if at == 1: 
                            dado = str(input('\033[33mEmail atual:\033[m '))
                            new = {'email':input('\033[33mNovo Email:\033[m ')}
                            atualizarDados("profissionais.dat",dado, new)                        
                            
                        elif at == 2:
                            dado = str(input('\033[33mSenha atual:\033[m '))
                            new = {'senha':input('\033[33mNova senha:\033[m ')}
                            atualizarDados("profissionais.dat",dado, new)                        
                            
                        elif at == 3:
                            dado = str(input('\033[33mCidade atual:\033[m ')).capitalize()
                            new = {'cidade':input('\033[33mNova Cidade:\033[m ').capitalize()}
                            atualizarDados("profissionais.dat",dado, new)                        
                            
                        elif at == 4:
                            dado = str(input('\033[33mInforme o email:\03)3[m '))
                            new = {'número':input('\033[33mNovo número:\033[m ')}
                            atualizarDados("profissionais.dat",dado, new)                        
                            
                        elif at == 5:
                            dado = str(input('\033[33mProfissão:\033[m ')).capitalize()
                            new = {'profissão':input('\033[33mNova Profissão:\033[m ').capitalize()}
                            atualizarDados("profissionais.dat",dado, new)                        
                            cabeçalho('\033[32mSuguestão de atualização: Descrição e preço agora podem estar desatualizados\033[m') 
                            
                        elif at == 6:
                            dado = str(input('\033[33mInforme o email:\033[m ')).capitalize()
                            new = {'descrição':input('\033[33mNova Descrição:\033[m ')}
                            atualizarDados("profissionais.dat",dado, new)                        
                            
                        elif at == 7:
                            dado = str(input('\033[33mInforme seu email:\033[m '))
                            new = {'preço': input('\033[33mNovo Preço:\033[m')}
                            atualizarDados("profissionais.dat",dado, new)                        
                            
                        elif at == 8:
                            
                            cabeçalho('\033[32mAtualização Finalizada\033[m')
                            break
                        
                        else: 
                            cabeçalho(f'{at} é uma opção inválida.')
                            
                elif opcao == 2: #Mostra os contratos vigenste do profissional
                    
                    cabeçalho('Nenhum contrato encontrado')
                    
                elif opcao == 3: #Mostra as notificações, buscas que os clietnes fazem e o encontram
                    
                    cabeçalho('Sem notificações recentes')
                    
                elif opcao == 4:
                    break
                
                else: cabeçalho(f'\033[0;31m{opcao} é uma opção inválida.\033[m')
    
    elif opc == 4:  #Apaga Cadastro
        x = menu(['Sou cliente', 'Sou Parceiro'])
        
        if x == 1:
            email = input('email:')
            senha = input('senha:')
            conf = removerCadastro('clientes.dat', email, senha )
        
        elif x == 2:
            email = input('email:')
            senha = input('senha:')
            conf = removerCadastro('profissionais.dat', email, senha )
        
    elif opc == 5: #Encerra programa

        cabeçalho('Sistema Encerrado'.upper())
        break
    
    else: 
        cabeçalho(f'\033[0;31m{opc} é uma opção inválida.\033[m')
 