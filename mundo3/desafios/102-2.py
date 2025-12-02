# Fiz dessa outra forma pra praticar com o while também.
def fatorial(n):
    total = 1

    while n >= 1:
        if n == 1:
            print(f'{n} = ', end='')
        else:
            print(f'{n} x ', end='')
        total *= n
        n -= 1
    print(total)

fat = int(input('Digite um numero: '))
fatorial(fat)
