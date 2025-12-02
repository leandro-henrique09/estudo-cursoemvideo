pessoas = {
    'nome': 'Leandro',
    'sexo': 'M',
    'idade': 21,
}

print(f'O {pessoas["nome"]} tem {pessoas["idade"]} anos.')
print(pessoas.keys()) # printando as chaves do dicionario, nesse caso ['nome', 'sexo', 'idade']
print(pessoas.values()) # printando os valores das chaves, ['Leandro', 'M', 21]
print(pessoas.items()) # printando o dicionario completo

for k in pessoas.keys():
    print(k)

for k, v in pessoas.items():
    print(f'{k} = {v}')

estado = {}
brasil = []
for c in range(0, 3):
    estado['uf'] = str(input('Unidade Federatia: '))
    estado['sigla'] = str(input('Sigla do Estado '))
    brasil.append(estado.copy())
for e in brasil:
    for k, v in e.items():
        print(f'O campo {k} tem valor {v}.')