# minha resposta
entrada = str(input('Informe seu sexo: [M/F] ')).upper().strip()

while entrada != 'M' and entrada != 'F':
    entrada = str(input('Dados inválidos. Por favor, informe seu sexo: ')).upper().strip()

print(f'Sexo {entrada} registrado com sucesso!')

# respota do video
sexo = str(input('Informe seu sexo: [M/F] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()[0]
print(f'Sexo {} registrado com sucesso.')