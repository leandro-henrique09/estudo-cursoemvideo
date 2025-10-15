vogal = ()

while True:
    palavra = str(input('Digite uma palavra e veja a vogal dela no final: ')).lower().strip()

    for v in palavra:
        if v in 'aeiou':
            vogal += v,

    print(f'A palavra digitada foi {palavra} e as vogais dela são {vogal}')

    continuar = str(input('Quer escrever mais palavras? [S/N] ')).strip()[0]
    vogal = ()
    if continuar == 'N':
        break
    
    

    
