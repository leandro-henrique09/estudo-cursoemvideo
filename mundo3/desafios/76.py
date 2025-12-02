# Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
# No final, mostre uma listagem de preços, organizando os dados em forma tabular.

# minha resposta
# nessa solução, acabei fazendo o exercicio de um jeito um pouco mais complexo.
# onde a tupla não vem pronta com itens colocado manualmente, e sim em um loop onde o usuario vai adicionando coisas na tupla;

lista_itens = ()
c = 0
while True:
    produto = str(input('Digite o produto: '))
    valor = float(input('Digite o valor desse produto: R$'))
    
    lista_itens += produto,
    lista_itens += valor,

    adicionar = str(input('Quer adicionar mais itens na lista? [S/N] ')).upper().strip()[0]

    while adicionar not in 'SsNn':
        adicionar = str(input('Digite um valor válido: [S/N] ')).upper().strip()[0]

    if adicionar == 'N':
        break


for i in range(0, len(lista_itens), 2):
    print(f'{lista_itens[i]:.<32} R${lista_itens[i + 1]:.2f}')

# ---------------------------------------------------------------


# resposta do video
listagem = ('Lápis', 1.75,
            'Borracha', 2,
            'Caderno', 15.90,
            'Estojo', 25,
            'Transferidor', 4.20,
            'Compasso', 9.99,
            'Mochila', 120.32,
            'Canetas', 22.30,
            'Livro', 34.90)
print('-' * 40)
print(f'{"LISTAGEM DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end='')
    else:
        print(f'R${listagem[pos]:>7.2f}')