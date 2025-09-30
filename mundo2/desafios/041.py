from datetime import date 
nascimento = int(input('Digite o seu ano de nascimento: '))
data_atual = date.today()
idade = data_atual.year - nascimento
print(f'O atleta tem {idade} anos.')
if idade <= 9:
    print('Você faz parte da categoria Mirim')
elif idade <= 14:
    print('Você faz parte da categoria Infantil')
elif idade <= 19:
    print('Você faz parte da categoria Junior')
elif idade <= 25:
    print('Você faz parte da categoria Sênior')
else:
    print('Você faz parte da categoria MASTER')