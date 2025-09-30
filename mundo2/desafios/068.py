from random import randint
count = 0
while True:
    pc = randint(0,10)
    valor = int(input('Diga um valor: '))
    escolha = str(input('Par ou Impar? [P/I] ')).strip().upper()[0]
    resultado = pc + valor

    if resultado % 2 == 0 and escolha == 'P' or resultado % 1 == 0 and escolha == 'I':
        print(f'Você jogou {valor} e o computador {pc}. Total de {resultado} deu {'par'  if resultado % 2 == 0 else 'impar'}.')
        print(f'VOCÊ VENCEU!')
        print(f'Vamos jogar novamente')
        count += 1
    else:
        print(f'Você jogou {valor} e o computador {pc}. Total de {resultado} deu {'par'  if resultado % 2 == 0 else 'impar'}.')
        print(f'Você perdeu, e ganhou {count} {'rodadas' if count > 1 else 'rodada'}.')
        break