pessoa = {}
lista_pessoas = []

while True:
    pessoa['nome'] = str(input('Nome: '))
    pessoa['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    while pessoa['sexo'] not in 'MF':
        pessoa['sexo'] = str(input('ERRO! Digite M ou F para escolha do sexo ')).strip().upper()[0]
    pessoa['idade'] = int(input('Idade: '))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    lista_pessoas.append(pessoa.copy())
    while continua not in 'SN':
        continua = str(input('ERRO! Digite S ou N para avançar!!! ')).strip().upper()[0]
    if continua in 'N':
        break
print('-=' * 30)
print(f'A) Ao todos temos {len(lista_pessoas)} pessoas cadastradas.')
media_idade = 0
for c, v in enumerate(lista_pessoas):
    media_idade += v['idade']
print(f'B) A média de idade é de {media_idade / len(lista_pessoas)}')
mulheres = []
for c, v in enumerate(lista_pessoas):
    if v['sexo'] == 'F':
        mulheres.append(v['nome'])
print(f'As mulheres cadastradas foram {mulheres}')
print(f'D) Lista das pessoas que estão acima da média:')
for p in lista_pessoas:
    if p['idade'] > media_idade / len(lista_pessoas):
        for k, v in p.items():
            print(f'  {k} = {v};', end='')
        print()
