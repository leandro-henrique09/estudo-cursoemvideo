primeiro_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
count = 1

while count <= 10:
    num = primeiro_termo + (count - 1) * razao
    count += 1
    print(num, end=' - ')
print('FIM')