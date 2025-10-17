# # listas são feitas com []
# lanche = ['hamburguer', 'suco', 'pizza', 'pudim']

# # adicionando itens a uma lista
# lanche = ['hamburguer', 'suco', 'pizza', 'pudim']
# lanche.append('cookies')
# # após rodar o append o resultado vai ser esse abaixo:
# lanche = ['hamburguer', 'suco', 'pizza', 'pudim','cookies']

# # ==============================================================

# # adicionando item em uma posição especifica
# lanche = ['hamburguer', 'suco', 'pizza', 'pudim',]
# lanche.insert(0,'cachorro-quente')
# # após rodar o insert o resultado vai ser esse abaixo:
# lanche = ['cachorro-quente','hamburguer', 'suco', 'pizza', 'pudim']

# # ==============================================================

# # maneiras de remover um item da lista:

# del lanche[3] # vai remover o indice 3
# lanche.pop(3) # também vai remover o indice 3
# lanche.remove('pizza') # serve para remover pelo nome do elemento
# lanche.pop() # vai eliminar o ultimo elemento da lista

# # =============================================================

# # como criar uma lista com um range de 4 até 10
# valores = list(range(4,11))

# # como organizar os valores dentro de uma lista
# valor = [2, 5, 6, 4, 9]
# valores.sort() # para deixar em ordem crescente
# valor.sort(reverse=True) # para deixar em ordem decrescente

# # como saber o tamanho de uma lista
# len(valores)

# ===================================== PARTE PRATICA ================================================

valores = []

for i in range(0, 5):
    valores.append(int(input('Digite um valor: ')))

for c, v in enumerate(valores):
    print(f'Na posição {c}, está o numero {v}!')
print('Cheguei ao final da lista!')