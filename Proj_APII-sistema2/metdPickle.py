import pickle


def criaArquivo(lista, nomeArq):    #Cria arquvio pelo pickle --  usado somente uma vez
    #Passado como parâmetro uma lista, e nome do arquivo a ser salvo essa lista de dados
    try:
        arquivo = open(nomeArq, "wb")
        pickle.dump(lista, arquivo)
        arquivo.close()
        print('Cadastro salvo com sucesso. ')
        return lista
    
    except:
        print("Ocorreu um erro ao salvar os arquivos.") 


def carregaDados(nomeArq):  #Carrega os dados do arquivo usando pickle
    #Passado como parâmetro o nome do arquivo
    try:
        arquivo = open(nomeArq, "rb")
        lista = pickle.load(arquivo)
        arquivo.close()
        return lista
    
    except:
        print("Ocorreu um erro ao carregar os arquivos.")


def atualizarDados(nomeArq, chave, newDado): #Atualiza dados do arquivo pelo pickle
    #Passado como parâmetro o nome do arquivo, uma 'chave' que representa o valor de um elemento de um dicinário 
    # e um 'newDado' que substiuirá esse valor da chave
    try:
            arquivo = open(nomeArq, 'rb')
            listaDados = pickle.load(arquivo)
        
    except:
            print("Arquivo não encontrado e/ou erro na estrura.")
            return
    
    if nomeArq == 'profissionais.dat':       
        for dado in listaDados:
            if dado['email'] == chave:
                dado.update(newDado)
                break
            
            elif dado['senha'] == chave:
                dado.update(newDado)
                break
            
            elif dado['número'] == chave:
                dado.update(newDado)
                break
            
            elif dado['cidade'] == chave:
                dado.update(newDado)
                break
            
            elif dado['profissão'] == chave:
                dado.update(newDado)
                break
            
            elif dado['descrição'] == chave:
                dado.update(newDado)
                break
            
            elif dado['preço'] == chave:
                dado.update(newDado)
                break
            
            else:
                print("Dados incorretos")
                return
                     
    if nomeArq == 'clientes.dat':      
        for dado in listaDados:
            if dado['email'] == chave:
                dado.update(newDado)
                break
            
            elif dado['senha'] == chave:
                dado.update(newDado)
                break
            
            elif dado['cidade'] == chave:
                dado.update(newDado)
                break
            
            else:
                print("Dados incorretos")
                return
            
    try:
            arquivo = open(nomeArq, 'wb')
            pickle.dump(listaDados, arquivo)
            print("Dados atualizados com sucesso!")
            arquivo.close()
            
    except IOError:
            print("Ocorreu um erro ao atualizar os dados no arquivo.")
            return



def adicionarDados(nomeArq, novoDado):  #Adiciona dados no arquivo pelo pickle
    #Passado como parâmetro o nome do arquivo e um novoDado a ser inserido
    #Para o sistema o tipo de dado será um dicionário contendo valores que representam um cadastro simples
    try:
        arquivo = open(nomeArq, 'rb')
        listaDados = pickle.load(arquivo)
        listaDados.append(novoDado)
        print('Cadastro feito com sucesso')
        arquivo.close()
        
    except:
        print("Arquivo não encontrado.") 
        return 
    
    try:
        arquivo = open(nomeArq, 'wb')
        pickle.dump(listaDados, arquivo)
        arquivo.close()
        
    except:
        print("Ocorreu um erro ao adicionar os dados ao arquivo.")
        return

def quest(msg): #Facilita uma reposta em T ou F
    #retorna True se a resposta for sim[S] e False se a resposta for não[N]
    while True:
        r = input(msg).strip().upper()
        if r == 'S':
            return True
        elif r == 'N':
            return False
        else:
            print('Inválido, informe somente sim ou não. [S/N]\n')

       
def login(nomeArq, email, senha):   #Tipo de login que valida um usuário usando pickle
    #Recebe como parâmetro o nomo do arquivo, email e senha de um cadastro
    #Retorna 'True' se encontrar os dados ou 'False' se não encontrar os dados no arquivo
    try:
        arquivo = open(nomeArq, 'rb')
        dados = pickle.load(arquivo)
        
    except:
        print("Arquivo não encontrado.")
        return False
    
    for dado in dados:
        if dado['email'] == email and dado['senha'] == senha:
            print("Login bem-sucedido!")
            return True
        
    print("Email ou senha incorretos.")
    return False

def removerCadastro(nomeArq, email, senha): #Remove dados do arquivo usando pickle
    #Passado como parâmetro o nome do arquivo, email e senha para confirmação de dados
    try:
        arquivo = open(nomeArq, 'rb')
        dados = pickle.load(arquivo)
        
    except:
        print("Arquivo não encontrado.")
        return
    
    indice = None
    for i, dado in enumerate(dados):
        if dado['email'] == email and dado['senha'] == senha:
            indice = i
            break
        
    if indice is not None:
        r = quest('Tem certeza que deseja apagar seu cadastro? [S/N]')
        if r:
            dados.pop(indice)
            try:     
                arquivo = open(nomeArq, 'wb')
                pickle.dump(dados, arquivo)
                print("\033[32mCadastro removido!\033[m")
            
            except:
                print("\033[31mOcorreu um erro ao remover o cadastro.\033[m")     
                    
        else:
            print('\033[31mCadastro não removido\033[m')


    else:
        print("Email ou senha incorretos.")





#adicionarDados('clientes.dat', {'nome': 'Natan', 'idade': 20, 'cidade': 'Crato', 'email': 'natan@natan.com', 'senha': 'natan20'})

#adicionarDados('profissionais.dat', {'nome': 'José', 'idade': 38, 'cidade': 'Jauzeiro', 'número': 88975674530, 'email': 'jose@j.com', 'senha': 'jose85', 'profissão': 'Pedreiro', 'descrição': 'Sou pedreiro a 10 anos, especializado em construção de casas, atualmente residindo em Juazeiro, também trabalho faço empeleitamento', 'preço': 'R$ 90,00 diária, + taxa de transporte + ajudantes | támbem é possível empeleitamento negocioável com o cliente'})






'''x = carregaDados('profissionais.dat')
y = carregaDados('clientes.dat')
print()
for pos, e in enumerate(y):
    print(e)
    pos+= 1
    print()
print(f'total de cadastros: {pos}')'''