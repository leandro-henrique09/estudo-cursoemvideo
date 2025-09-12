# minha versão
salario = float(input('Digite o salário do funcionario: '))

if salario <= 1250:
    print(f'O salario que era {salario}, passa a ser {salario + (salario * 15 / 100)}')
else: 
    print(f'O salario que era {salario}, passa a ser {salario + (salario * 10 / 100)}')

# resposta do video
salario = float(input('Qual é o salario do funcionario? R$'))
if salario <= 1250:
    novo = salario + (salario * 15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print('Quem ganhava R${:.2f} passa a ganhar R${:.2f} agora.'.format(salario, novo) )