from datetime import date 
ano = date.today()
pessoa = {}
pessoa['nome'] = str(input('Nome: '))
idade = int(input('Ano de nascimento: '))
pessoa['idade'] = ano.year - idade
pessoa['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))
if pessoa['ctps'] != 0:
    pessoa['ano_contratação'] = int(input('Ano de contratação: '))
    pessoa['salario'] = float(input('Salário: R$'))
    pessoa['aposentadoria'] = pessoa['ano_contratação'] - idade + 35
print('-=' * 30)
for k, v in pessoa.items():
    print(f' - {k} tem o valor {v}')

