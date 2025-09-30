# minha resposta
numero = int(input('Digite um número inteiro: '))
print('Abaixo veja as conversões possíveis')
print('[ 1 ] Converter para binário')
print('[ 2 ] Converter para octal')
print('[ 3 ] Converter para hexadecimal')
opçao = int(input('Escolha uma das bases para conversão! '))
num_binario = bin(numero)[2:]
num_octal = oct(numero)[2:]
num_hexadecimal = hex(numero)[2:]

if opçao == 1:
    print(num_binario)
elif opçao == 2:
    print(num_octal)
elif opçao == 3:
    print(num_hexadecimal)
else:
    print('Essa opção não existe! Tente Novamente.')


#  resposta do video
num = int(input('Digite um número inteiro: '))
print('''Escolha uma das bases para conversão:
[ 1 ] Converter para BINÁRIO
[ 2 ] Converter para OCTAL
[ 3 ] Converter para HEXADECIMAL''')
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num, bin(num)[2:]))
elif opção == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opção == 3:
    print('{} convertido para HEXADECIMAL é igual a {}'.format(num, hexa(num)[2:]))
else:
    print('Opção inválida. Tente novamente.')
