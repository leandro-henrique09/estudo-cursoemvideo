from random import sample, shuffle

primeiro = str(input('Digite o primeiro nome: '))
segundo = str(input('Digite o segundo nome: '))
terceiro = str(input('Digite o terceiro nome: '))
quarto = str(input('Digite o quarto nome: '))

listaNomes = [primeiro, segundo, terceiro, quarto]
escolhido = sample(listaNomes, k=len(listaNomes))

print(f"A ordem de apresentação será\n {escolhido}")
