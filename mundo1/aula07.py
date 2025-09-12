# OPERADORES ARITMÉTICOS
# '+' = Adição
# '-' = Subtração
# '*' = Mutiplicação
# '/' = Divisão
# '**' = Potência
# '//' = Divisão Inteira
# '%' = Resto da Divisão


# EXEMPLOS
# 5+2 == 7 - Adição
# 5-2 == 3 - Subtração
# 5*2 == 10 - Mutiplicação
# 5/2 == 2.5 - Divisão
# 5**2 == 25 - Potencia
# 5//2 == 2 - Divisão Inteira
# 5%2 == 1 - Resto da Divisão

# ORDEM DE PRECEDÊNCIA
# 1 - ()
# 2 - **
# 3 - *, /, //, %
# 4 - +, -

nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {}!'.format(nome))
print('Prazer em te conhecer {:20}!'.format(nome)) # o '{:20}' determina o campo ser escrito em 20 espaços
print('Prazer em te conhecer {:>20}!'.format(nome)) # o '{:>20}' posiciona o texto no a direita dos 20 espaços
print('Prazer em te conhecer {:<20}!'.format(nome)) # o '{:<20}' posiciona o texto a esquerda dos 20 espaços
print('Prazer em te conhecer {:^20}!'.format(nome)) # o '{:^20}' posiciona o texto no centro dos 20 espaços
print('Prazer em te conhecer {:=^20}!'.format(nome)) # o '{:=^20}' posiciona o texto no centro e coloca '=' em volta do texto

n1 = int(input('Digite um valor: '))
n2 = int(input('Outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma é {}, \n o produto é {} \n e a divisão é {}'.format(s, m, d), end=' ') # usando o 'end' para não quebrar a linha entre os prints e o '\n' para quebrar linhas de dentro do print
print('A soma é {}, e o produto é {} e a divisão é {:.3f}'.format(s, m, d)) # determinando que a divisão na ultima chave, só vai ter 3 numeros flutuantes
print('Divisão inteira {} e potência {}'.format(di, e))