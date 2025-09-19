soma = 0
total = 0
for i in range(0,6):
    num = int(input('Digite um numero inteiro: '))
    if num % 2 == 0:
        soma += 1
        total += num
    else:
        print(f'O número {num} não é par, portanto foi desconsiderado!')
print(f'A soma dos numeros pares foi {total}')