# minha resposta
from time import sleep
primeiro = int(input('Primeiro valor: '))
segundo = int(input('Segundo valor: '))
entrada = True

while entrada:
    opção = int(input('[ 1 ] somar\n[ 2 ] mutiplicar\n[ 3 ] maior\n[ 4 ] novos números\n[ 5 ] sair do programa\nQual é a sua opção? '))
    sleep(1.0)

    if opção == 1:
        print(f'A soma de {primeiro} + {segundo} é {primeiro + segundo}')
    elif opção == 2:
        print(f'O número {primeiro} x {segundo} é igual a {primeiro * segundo}')
    elif opção == 3:
        if primeiro > segundo:
            print(f'Entre {primeiro} e {segundo} o maior é o {primeiro}')
        elif segundo > primeiro:
            print(f'Entre {primeiro} e {segundo} o maior é o {segundo}')
        else:
            print(f'Os números {primeiro} e {segundo} são iguais.')
    elif opção == 4:
        primeiro = int(input('Digite o primeiro valor: '))
        segundo = int(input('Digite o segundo valor: '))
    elif opção == 5:
        entrada = False
    else:
        print('Digite uma opção correta! ')

print('Como escolhido, o programa foi encerrado! ')

#  resposta do video
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] mutiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('Qual é a sua opção? '))
    if opção == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif opção == 2:
        produto = n1 * n2
        print(f'O resultado de {n1} x {n2} é {produto}')
    elif opção == 3:
        if n1 > n2:
            maior = n1
        else: 
            maior = n2
        print(f'Entre {n1} e {n2} o maior valor é {maior}')
    elif opção == 4:
        print('Informe os números novamente: ')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
print('Fim do programa! Volte sempre! ')