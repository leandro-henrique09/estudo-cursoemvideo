# minha versão, não tirei os espaços entre os nomes.
nome = str(input('Digite seu nome completo: ')).strip()
primeiro_nome = nome.split()

print(nome.upper())
print(nome.lower())
print(len(nome))
print(len(primeiro_nome[0]))

# resposta
nome = str(input(Digite seu nome completo: )).strip()
print('Analisando seu nome...')
print('Seu nome em maiúsculas é {}'.format(nome.upper()))
print('Seu nome em minúsculas é {}'.format(nome.lower()))
print('Seu nome tem ao todos {} letras.'.format(len(nome) - nome.count(' ')))
separa = nome.split()
print('Seu primeiro nome é {} e tem {} letras.'.format(separa[0] ,len(separa[0])))