from time import sleep
def ajuda(b):
    print('~' * 40)
    print(f'Acessando o manual do comando {b}')
    print('~' * 40)
    sleep(0.5)
    help(b)
    sleep(0.5)

while True:
    escolhaHelp = str(input('Função ou biblioteca > ')).lower()
    if escolhaHelp in "fim":
        print('Encerrando programa...')
        sleep(0.5)
        break
    else:
        ajuda(escolhaHelp)
