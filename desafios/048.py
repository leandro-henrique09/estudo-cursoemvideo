soma = 0
total = 0
for i in range(1, 501, 2):
    if i % 3 == 0:
        print(i)
        soma += 1
        total += i

print(f'A soma dos {soma} números resultam em {total}.')   