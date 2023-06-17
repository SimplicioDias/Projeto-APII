import pickle


def criaArquivo(lista, nomeArq):
    try:
        arquivo = open(nomeArq, "wb")
        pickle.dump(lista, arquivo)
        arquivo.close()
        print('Cadastro salvo com sucesso. ')
        return lista
    except:
        print("Ocorreu um erro ao salvar os arquivos.") 



def carregaDados(nomeArq):
    try:
        arquivo = open(nomeArq, "rb")
        lista = pickle.load(arquivo)
        arquivo.close()
        return lista
    except:
        print("Ocorreu um erro ao carregar os arquivos.")



def atualizarDados(nomeArq, chave, newDado):
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
                print("O dado fornecido não foi encontrado nos dados existentes.")
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
                print("O dado fornecido não foi encontrado nos dados existentes.")
                return
    try:
        arquivo = open(nomeArq, 'wb')
        pickle.dump(listaDados, arquivo)
        print("Dados atualizados com sucesso!")
        arquivo.close()
    except IOError:
        print("Ocorreu um erro ao atualizar os dados no arquivo.")
        return


def adicionarDados(nomeArq, novoDado):
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


def login(nomeArq, email, senha):
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

def removerCadastro(nomeArq, email, senha):
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
        dados.pop(indice)
        try:
            arquivo = open(nomeArq, 'wb')
            pickle.dump(dados, arquivo)
            print("Cadastro removido com sucesso!")
        except:
            print("Ocorreu um erro ao remover o cadastro.")
    else:
        print("Email ou senha incorretos.")



""" def remover_dados(arquivo, dado_remover):
    try:
        # Carrega os dados existentes do arquivo
        with open(arquivo, 'rb') as file:
            dados_existentes = pickle.load(file)
    except FileNotFoundError:
        print("Arquivo não encontrado.")
        return
    
    # Verifica se o dado a ser removido está na lista
    if dado_remover in dados_existentes:
        # Remove o dado da lista
        dados_existentes.remove(dado_remover)
        
        try:
            # Salva os dados atualizados no arquivo
            with open(arquivo, 'wb') as file:
                pickle.dump(dados_existentes, file)
            print("Dado removido com sucesso!")
        except IOError:
            print("Ocorreu um erro ao remover o dado do arquivo.")
    else:
        print("O dado não existe no arquivo.")
arquivo = "profissionais.dat"
dado_remover = 1 """



#adicionarDados('clientes.dat', {'nome': 'Natan', 'idade': 20, 'cidade': 'Crato', 'email': 'natan@natan.com', 'senha': 'natan20'})
#print(carregaDados('clientes.dat'))

#adicionarDados('profissionais.dat', {'nome': 'José', 'idade': 38, 'cidade': 'Jauzeiro', 'número': 88975674530, 'email': 'jose@j.com', 'senha': 'jose85', 'profissão': 'Pedreiro', 'descrição': 'Sou pedreiro a 10 anos, especializado em construção de casas, atualmente residindo em Juazeiro, também trabalho faço empeleitamento', 'preço': 'R$ 90,00 diária, + taxa de transporte + ajudantes | támbem é possível empeleitamento negocioável com o cliente'})
#print(carregaDados('profissionais.dat'))

