# atividade 16
pessoa = {}
pessoa["nome"] = input('Informe o nome: ')
pessoa["idade"] = input('Informe a Idade: ')
pessoa["CPF"] = input('Informe o CPF: ')
pessoa["RG"] = input('Informe o RG: ')
pessoa["data_nasc"] = input('Informe a data de nascimento: ')
pessoa["sexo"] = input('Informe o sexo: ')
pessoa["signo"] = input('Informe o signo: ')
pessoa["mae"] = input('Informe o nome da Mãe: ')
pessoa["pai"] = input('Informe o nome do Pai: ')
pessoa["email"] = input('Informe o e-mail: ')
pessoa["senha"] = input('Informe uma senha: ')
pessoa["CEP"] = input('Informe o CEP: ')
pessoa["endereco"] = input('Informe o endereço: ')
pessoa["numero"] = input('Informe o numero: ')
pessoa["bairro"] = input('Informe o bairro: ')
pessoa["cidade"] = input('Informe o cidade: ')
pessoa["estado"] = input('Informe o estado: ')
pessoa["telefone"] = input('Informe o telefone: ')
pessoa["celular"] = input('Informe o celular: ')
pessoa["altura"] = input('Informe a altura: ')
pessoa["peso"] = input('Informe o peso: ')
pessoa["tipo_sanguineo"] = input('Informe o tipo sanguíneo: ')
pessoa["cor"] = input('Informe uma cor: ')
print('\n')
for tela in pessoa:
    print(f'{tela}: {pessoa.get(tela)}')
    