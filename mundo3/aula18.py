# teste = list() --- criando lista
# teste.append('Gustavo') --- adicionando 'Gustavo' na lista
# teste.append(40) --- adicionando 40 na lista
# galera = list() --- criando lista 'galera'
# galera.append(teste[:]) --- dando um append de uma cópia da lista 'teste'
# teste[0] = 'Maria' --- mudando valor do indice 0 de teste
# teste[1] = 22 --- mudando o valor do indice 1 de teste
# galera.append(teste[:]) --- fazendo um append da lista com novos valores
# print(galera) --- printando lista 'galera'

# galera = [['João', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
# for p in galera:
#     print(f'{p[0]} tem {p[1]} anos de idade')

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmen += 1
    
print(f'Temos {totmai} maiores e {totmen} menores de idade.')