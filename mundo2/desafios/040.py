n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2

if media < 5:
    print(f'Sua média foi de {media}, portando você foi reprovado!')
elif media >= 5 and media < 6.9:
    print(f'A sua média foi de {media}, portanto está de recuperação')
else:
    print(f'Sua média foi de {media}, portanto foi aprovado!')