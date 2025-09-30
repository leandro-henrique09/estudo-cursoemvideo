from datetime import date
ano = int(input('Digite o ano de nascimento: '))
ano_atual = date.today()
calculo_idade = ano_atual.year - ano
idade_menor = 18 - calculo_idade
print(f'Quem nasceu em {ano} tem {calculo_idade} anos em {ano_atual.year}')


if calculo_idade < 18: 
    print(f'Ainda faltam {idade_menor} anos para o alistamento')
    print(f'Seu alistamento será em {ano + 18}')
elif calculo_idade == 18:
    print('Você tem que se alistar imediatamente!')
else:
    print(f'Você já deveria ter se alistado há {calculo_idade - 18} anos')
    print(f'Seu alistamento foi em {ano + 18}')
