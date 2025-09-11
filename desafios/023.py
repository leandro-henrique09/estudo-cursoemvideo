# minha versão, passou batido :D
numero = input('Digite um numero de 0 a 9999: ')

print('unidade: ', numero[3])
print('dezena: ', numero[2])
print('centena: ', numero [1])
print('milhar: ', numero [0])

# resposta do video
num = int(input('Informe um número: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o número {}'.format(num))
print('Unidade : {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))