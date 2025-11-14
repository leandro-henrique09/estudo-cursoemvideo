def leiaInt(n):
    if n.isnumeric():
        return n
    else:
        while not n.isnumeric():
            print('ERRO! Digite um numero inteiro válido.')
            n = input('Digite um numero: ')
    return n

num = input('Digite um número: ')
print(f'Você acabou de digitar o numero {leiaInt(num)}')