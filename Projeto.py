cadastros = []

def cadastrar_pessoa():
    print("==== Cadastro de Pessoa ====")
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("E-mail: ")
    pessoa = {
        "Nome": nome,
        "Idade": idade,
        "Email": email
    }
    cadastros.append(pessoa)
    print("Cadastro realizado com sucesso!\n")

def visualizar_cadastros():
    print("==== Cadastros ====")
    if not cadastros:
        print("Nenhum cadastro encontrado.\n")
    else:
        for i, pessoa in enumerate(cadastros, start=1):
            print(f"Cadastro {i}:")
            print(f"Nome: {pessoa['Nome']}")
            print(f"Idade: {pessoa['Idade']}")
            print(f"E-mail: {pessoa['Email']}")
            print()
    
def exibir_menu():
    print("==== Menu ====")
    print("1. Cadastrar pessoa")
    print("2. Visualizar cadastros")
    print("3. Encerrar programa")

exibir_menu()

while True:
    opcao = input("Digite o número da opção desejada: ")
    
    if opcao == "1":
        cadastrar_pessoa()
    elif opcao == "2":
        visualizar_cadastros()
    elif opcao == "3":
        print("Encerrando o programa...")
        break
    else:
        print("Opção inválida. Por favor, tente novamente.\n")
    
    exibir_menu()
