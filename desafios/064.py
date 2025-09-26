entrada = int(input('Digite um número [999 para parar]: '))
count = 0
soma = 0
while entrada != 999:
    count += 1
    soma += entrada
    entrada = int(input('Digite um número [999 para parar]: '))

print(f'Você digitou {count} {'números' if count > 1  else 'número'} e a soma foi {soma}.')