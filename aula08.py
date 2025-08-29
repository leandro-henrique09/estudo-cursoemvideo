# AULA SOBRE MÓDULOS(BIBLIOTECAS, PACOTES E ETC..)

# explicação de como importar uma biblioteca
# import bebida = importando toda a biblioteca 'bebida'.
# from doce import pudim = importando apenas o item 'pudim' da biblioteca de doce

#   exemplo de biblioteca conhecida
# MATH  
#   ceil() = serve para arredondar um numero para cima.
#   floor() = serve para arredondar um numero para baixo.
#   trunc() = vai truncar um numero, removendo numeros após a virgula 
#   pow() = serve para fazer potencia
#   sqrt() = serve para calcular raiz quadrada
#   factorial() = serve para somar o fatorial 



# importando biblioteca inteira
# import math 
# num = int(input('Digite um número: '))
# raiz = math.sqrt(num)
# print('A raiz de {} é igual a {:.2f}'.format(num,raiz))

# importando apenas algumas coisas
# from math import sqrt, floor
# num = int(input('Digite um número: '))
# raiz = sqrt(num)
# print('A raiz de {} é igual a {:.2f}'.format(num,floor(raiz)))

# import random
# num = random.randint(1,10)
# print(num)

import emoji
print(emoji.emojize("Olá mundo :globe_showing_Americas:"))