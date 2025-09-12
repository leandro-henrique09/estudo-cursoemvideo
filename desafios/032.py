# minha versao, foi a mesma reposta q o video 
from datetime import date
ano = int(input('Digite um ano para saber se é bissexto, para ver o ano atual digite 0: '))
ano_atual = date.today()

if ano == 0:
    ano = ano_atual.year

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano de {ano} é bissexto')
else:
    print(f'O ano de {ano} não é bissexto')

