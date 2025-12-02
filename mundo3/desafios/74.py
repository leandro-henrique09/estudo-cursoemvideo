# Crie um programa que vai gerar cinco números aleatórios e colocar em uma tupla.
# Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.

from random import sample

num = tuple(sample(range(10),5))
print(num)
print(f'O maior valor é {max(num)} e o menor é {min(num)}')