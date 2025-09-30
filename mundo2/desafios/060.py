fat = int(input('Digite um número para ver o fatorial: '))
numfat = fat
num = fat 

while num >= 2:
    operacao = fat * (num - 1)
    fat = operacao
    num -= 1
    print(num)

print(f'O fatorial de {numfat} é {fat}')

