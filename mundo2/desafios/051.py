primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))

for i in range(1, 11):
    num = primeiro_termo + (i - 1) * razao
    print(num)