mais_velho = 0
nome_mais_velho = ''
mulher_menor = 0
media = 0

for i in range(1, 5):
    print(f'----- {i}° PESSOA -----')
    nome = str(input(f'Digite o nome da {i}° pessoa: '))
    idade = int(input(f'Digite a idade dessa pessoa: '))
    sexo = str(input(f'Digite o sexo [M/F]: ')).upper()
    media += idade

    if sexo == 'M' and idade > mais_velho:
        mais_velho = idade
        nome_mais_velho = nome

    if sexo != 'M' and sexo != 'F':
        print('Digite o sexo correto! ')

    if sexo == 'F' and idade < 20:
        mulher_menor += 1

print(f'A média de idade do grupo é de {media / 4} anos.')
print(f'O homem mais velho tem {mais_velho} anos e se chama {nome_mais_velho}.')
print(f'Ao todo são {mulher_menor} mulheres com menos de 20 anos')
