maior_peso = 0
menor_peso = 0

for i in range(1, 6):
    peso = float(input(f'Digite o peso da {i}° pessoa: '))

    if menor_peso == 0 or menor_peso >= peso:
        menor_peso = peso
    elif maior_peso <= peso:
        maior_peso = peso

print(f'O maior peso foi {maior_peso}Kg e o menor foi {menor_peso}Kg')