# minha resposta
tupla = count_par = ()
count_nine =  0

for i in range(1,5):
    num = int(input('Digite um valor: '))
    tupla += num,

    if num == 9:
        count_nine += 1

    if num % 2 == 0:
        count_par += num,

print(f'O número 9 apareceu {count_nine} vezes na tupla!')
if 3 in tupla:
    print(f'O número 3 foi escrito na posição {tupla.index(3)+1}°')
else:
    print('Não foi digitado nenhuma vez o numero 3')
print(f'{'Não teve nenhum número par na tupla!' if count_par == () else count_par}')

# resposta do video
núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Você digitou os valores {num}')

print(f'O valor 9 apareceu {núm.count(9)} vezes')
print(f'O valor 3 apareceu na {núm.index(3)+1}° posição')
print('Os valores pares digitados foram ', end='')
for n in núm:
    if n % 2 == 0:
        print(n, end=' ')