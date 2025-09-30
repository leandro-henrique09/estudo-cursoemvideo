maioridade = homens = mulheres_menor = 0
while True:
    idade = int(input('Digita uma idade: '))
    sexo = str(input('Digite um sexo: [M/F] ')).strip().upper()[0]
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
 
    if idade > 18:
        maioridade += 1
    
    if sexo == 'M':
        homens += 1
    
    if sexo == 'F' and idade < 20:
        mulheres_menor += 1

    if continuar == 'N':
        break
print('-=-' * 30)
print(f'{maioridade} {'pessoas' if maioridade > 1 else 'pessoa'} tem mais de 18 anos!')
print(f'Foram cadastrados {homens} {'homens' if homens > 1 else 'homem'}.')
print(f'{mulheres_menor} {'mulheres' if mulheres_menor > 1 else 'mulher'} tinha menos que 20 anos.')
print('-=-' * 30)