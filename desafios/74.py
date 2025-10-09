from random import sample

num = tuple(sample(range(10),5))
print(num)
print(f'O maior valor é {max(num)} e o menor é {min(num)}')