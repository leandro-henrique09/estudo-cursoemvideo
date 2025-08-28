# minha versao
dias = int(input('Digite o total de dias alugados: '))
km = float(input('Digite a quantidade de km rodado: '))
diarias = 60 * dias
km_rodado = 0.15 * km
print('O total a pagar é de R${:.2f}'.format(diarias + km_rodado))

# resposta do video
dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos km rodados? '))
pago = (dias * 60) + (km * 0.15)
print('O total a pagar é de R${:.2f}'.format(pago))