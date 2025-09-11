# minha versão
nome = str(input('Digite seu nome completo: ')).strip()
nome_dividido = nome.split()

print('primeiro: ', nome_dividido[0])
print('ultimo: ', nome_dividido[-1])

# resposta do video
n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()
print('Muito prazer em te conhecer')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))