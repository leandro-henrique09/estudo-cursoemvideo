# minha versão
um = int(input('Digite o primeiro numero: '))
dois = int(input('Digite o segundo numero: '))
tres = int(input('Digite o terceiro numero: '))

# usei o list para conseguir chegar no resultado usando o max() e min().
lista = list((um, dois, tres))
print(f'O maior valor digitado foi: ',max(lista))
print(f'O menor valor digitado foi: ',min(lista))

# resposta do video
a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
maior = a 
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O menor valor digitado foi {menor}')
print(f'O maior valor digitado foi {maior}')