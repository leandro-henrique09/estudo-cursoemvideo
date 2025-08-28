# minha versão
salario = float(input('Qual é o salário do funcionario? R$'))
aumento = salario + (salario * 15 / 100)
print('Um funcionário que ganhava R${}, com 15% de aumento, passa a receber {}!'.format(salario,aumento))

# resposta do video(gabaritei rsrs)
salário = float(input('Qual é o salário do Funcionário? R$'))
novo = salário + (salário * 15 / 100)
print('Um funcionário que ganhava R${:.2f}, com 15% de aumento, passa a receber R${:.2f}'.format(salário, novo))
