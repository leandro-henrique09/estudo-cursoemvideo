# Faça um programa que tenha uma função chamada ficha(), 
# que receba dois parâmetros opcionais: o nome de um jogador e quantos gols ele marcou. 
# O programa deverá ser capaz de mostrar a ficha do jogador, 
# mesmo que algum dado não tenha sido informado corretamente.
def ficha(j=0,g=0):
    if not j and not g:
        print(f'Jogador <desconhecido> fez 0 gols.')
    elif g == "" or g.isalpha():
        print(f'Jogador {j} fez 0 gols')
    elif j == "":
        print(f'Jogador <desconhecido> fez {g} gols')
    else:
        print(f'Jogador {j} fez {g} gols')

jogador = str(input('Nome do jogador: '))
gols = input('Número de gols: ')
ficha(jogador,gols)
