frase = 'Curso em Video Python'

#  exemplos de fatiamento

# frase[5] # vai pegar o caracter que esteja na posição 5
# frase[5:10] # vai pegar os caracteres da posição 5 até a 9(contando que ele sempre corta a ultima, nesse caso o 10)
# frase[5:10:2] # vai pegar os caracteres da posição 5 até a 9 pulando de dois em dois
# frase[:5] # vai pegar os caracteres do inicio até a posição 4
# frase[15:] # vai pegar os caracteres a partir da posição 15 até o final
# frase[9::3] # vai pegar os caracteres a partir da posição 9 até o fim, pulando de 3 em 3

# len(frase) # pegando o comprimento de "frase" com o len.
# frase.count('o') # contando quantas vezes aparece a letra 'o' na frase
# frase.count('o', 0, 13) # contando quantas vezes aparece a letra 'o' na frase, dentro de um fatiamento entre o numero 0 ao 12.
# frase.find('deo') # onde ele encontra a sequencia 'deo' dentro da frase.
# frase.find('Android') # o parametro 'Android' não existe na frase, então ele vai retornar -1
# 'Curso' in frase # verifica se existe a palavra 'Curso' dentro de frase.

# frase.replace('Python', 'Android') # substitui o 'Python' por 'Android'
# frase.upper() # tornar os caracteres maiusculos.
# frase.lower() # tornar os caracteres minusculos
# frase.capitalize() # colocar todos os caracteres minusculos, exceto o primeiro caracter.
# frase.title() # analisa quantas palavras tem separadas por espaços e torna o inicio de cada uma em maiuscula
# frase.strip() # remove todos espaços inuteis
# frase.rstrip() # remove os espaçoes da direita
# frase.lstrip() # remove os espaços da esquerda

# frase.split() # faz uma divisão nos espaços entre uma palavra e outra, gerando uma lista dividindo todas as palavras
# -.join(frase) # inclui um '-' entre as palavras divididas 
#  

# PARTE PRATICA
print(frase.split())

