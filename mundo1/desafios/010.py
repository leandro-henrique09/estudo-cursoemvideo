# minha resposta
saldo = float(input('Quanto de dinheiro você tem na carteira? R$'))
# usei o valor do dólar atual
dolar = 5.43 
print('Com R${:.2f} você pode comprar US{:.2f}'.format(saldo, saldo / dolar))

# resposta do video
real = float(input('Quanto dinheiro você tem na carteira? R$'))
dolar = real / 3.27
print('Com R${:.2f} você pode comprar US${:.2f}'.format(real, dolar))