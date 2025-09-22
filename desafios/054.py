from datetime import date
primeira = int(input('Digite o ano de nascimento da 1° pessoa: '))
segunda = int(input('Digite o ano de nascimento da 2° pessoa: '))
terceira = int(input('Digite o ano de nascimento da 3° pessoa: '))
quarta = int(input('Digite o ano de nascimento da 4° pessoa: '))
quinta = int(input('Digite o ano de nascimento da 5° pessoa: '))
sexta = int(input('Digite o ano de nascimento da 6° pessoa: '))
setima = int(input('Digite o ano de nascimento da 7° pessoa: '))
data_atual = date.today().year
count_maior = 0
count_menor = 0

lista_pessoas = [primeira, segunda, terceira, quarta, quinta, sexta, setima]

for idade in lista_pessoas:
    if data_atual - idade >= 18:
        count_maior += 1
    else:
        count_menor += 1
print(f'Das 7 pessoas {count_maior} são maiores de idade e {count_menor} são menores de idade')




# durante a aula também pensei na solução abaixo:

for i in range(1, 8):
    ano = int(input(f'Digite o ano de nascimento da {i}° pessoa. '))
    if data_atual - ano >= 18:
        count_maior += 1
    else:
        count_menor += 1

print(f'Das 7 pessoas {count_maior} são maiores de idade e {count_menor} são menores de idade')
