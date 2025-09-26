continua = 'S'
count = 0
valores = 0 
maior = 0
menor = 0

while continua == 'S':
    num = int(input('Digite um número: '))
    continua = str(input('Quer continuar? [S/N]')).upper()
    count += 1
    valores += num

    if menor == 0 or menor >= num:
        menor = num
    elif maior < num:
        maior = num

print(f'Você digitou {count} {'números' if count > 1 else 'número'} e a média foi {valores / count}')
print(f'O maior valor foi {maior} e o menor foi {menor}')
