product_mil = total = menor_price = 0
nome_menor = ''

while True:
    produto = str(input('Nome do produto: '))
    preco = float(input('Preço: R$'))
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]

    if menor_price == 0 or menor_price > preco:
        menor_price = preco
        nome_menor = produto

    if preco > 1000:
        product_mil += 1
    
    total += preco
    
    if continua == 'N':
        break
    
print(f'O total da compra foi R${total:.2f}')
print(f'Temos {product_mil} produtos custando mais de R$1000.00')
print(f'O produto mais barato foi {nome_menor} que custa R${menor_price:.2f}')