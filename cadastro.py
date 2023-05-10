from datetime import datetime           #import para saber a idade da pessoa com base no ano atual da máquina

cadastro = list()
pessoa = dict()

print('▬▬▬▬▬▬ Cadastro ▬▬▬▬')          #CABEÇALHO
pessoa['nome'] = str(input('Nome: '))
pessoa['idade'] = datetime.now().year - int(input('Ano de nascimento: '))
pessoa['email'] = str(input('E-mail: '))


print('▬▬▬▬▬▬ Cadastro Finalizado ▬▬▬▬▬▬')
cadastro.append(pessoa.copy())
pessoa.clear()


print(cadastro)     #teste
print(pessoa)