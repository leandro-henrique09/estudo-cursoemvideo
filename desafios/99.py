from time import sleep
def maior(* n):
    print('-=' * 30)
    print(f'Analisando os valores passados...')
    sleep(0.5)
    for i in n:
        print(f'{i}', end=' ', flush=True)
        sleep(0.5)
    print(f'{'Foram' if len(n) > 1 else 'Foi'} {'informados' if len(n) > 1 else 'informado'} {len(n)} {'valores' if len(n) > 1 else 'valor'} ao todo.')
    print(f'O maior valor informado foi {max(n)}')

maior(2, 4, 6, 8, 9, 1)
maior(2, 14, 12, 32)
maior(1)