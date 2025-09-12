# minha resolução
preco = float(input('Informe o valor do produto: '))
desconto = (preco * 5 / 100)
preco_final = preco - desconto

print('O valor do produto R${}, aplicando o desconto de 5%, ficou por {}'.format(preco, preco_final))

# resposta do video
preco = float(input('Qual é o preço do produto? R$ '))
novo = preco - (preco * 5 / 100)
print('O produto que custava R${:.2f}, na promoção com desconto de 5% vai custar R${:.2f}'.format(preco, novo))