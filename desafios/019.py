from random import choice, shuffle

primeiro = str(input('Digite o primeiro nome: '))
segundo = str(input('Digite o segundo nome: '))
terceiro = str(input('Digite o terceiro nome: '))
quarto = str(input('Digite o quarto nome: '))

listaNomes = [primeiro, segundo, terceiro, quarto]
escolhido = choice(listaNomes)

print(f"O nome escolhido foi o {escolhido}")
