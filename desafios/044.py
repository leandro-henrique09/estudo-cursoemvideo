valor = float(input('Digite o valor das compras: '))

print('FORMAS DE PAGAMENTO')
print('[ 1 ] à vista dinheiro/cheque' )
print('[ 2 ] à vista cartão')
print('[ 3 ] 2x no cartão')
print('[ 4 ] 3x ou mais no cartão')
opcao = int(input('Qual é a opção? '))

if opcao == 1:
    desconto = valor * 10 / 100
    print(f'Sua compra de R${valor} vai custar R${valor - desconto} no final')
elif opcao == 2:
    desconto = valor * 5 / 100
    print(f'Sua compra de R${valor} vai custar R${valor - desconto} no final')
elif opcao == 3:
    parcela = valor / 2
    print(f'Sua compra de R${valor} vai ficar em 2x de R${parcela}')
elif opcao == 4:
    parcelas = int(input('Quantas parcelas? '))
    juros = valor * 20 / 100
    valor_final = valor + juros 
    parcela = valor_final / parcelas
    print(f'Sua compra será parcelada em {parcelas}x de R${parcela} COM JUROS')
    print(f'Sua compra de {valor} vai custar R${valor_final} no final')
else:
    print('Digite uma opção válida! ')
