# minha versão
palavra = input("Digite uma palavra: ")
tipo = type(palavra)

print('O tipo primitivo desse valor é {}'.format(tipo))
print('É formada só por espaços ?', palavra.isspace())
print('É um número ? ', palavra.isnumeric())
print('É alfabetico ? ', palavra.isalpha())
print('É alfanumerico ? ', palavra.isalnum())
print('Está em maiúsculas ? ', palavra.isupper())
print('Está em minúsculas ? ', palavra.islower())
print('Está capitalizada ? ', palavra.istitle())

# versão do video
a = input('Digite algo: ')

print('O tipo primitivo desse valor é ', type(a)) # mostrando o tipo da variavel 'a'
print('Só tem espaços? ', a.isspace()) # verificando se a variavel 'a' só tem espaços como valor
print('É um número? ', a.isnumeric()) # verificando se a palavra é formada por um numero
print('É alfabético? ', a.isalpha()) # verificando se a palavra é alfabetica
print('É um alfanumérico? ', a.isalnum()) # verificando se a palavra é alfanumérica(formada por string e numero)
print('Está em maiúsculas ? ', a.isupper()) # verificando se a palavra esta totalmente em maiusculo
print('Está em minúsculas ? ', a.islower()) # verificando se a palavra esta totalmente em minusculo
print('Está capitalizada ? ', a.istitle()) # verificando se a primeira letra da palavra é maiuscula

# RESUMO

# No desafio acima, a variavel 'a' é sempre um 'objeto', 
# todo objeto tem caracteristicas e realiza funcionalidades como: atributos e metodos.
