frase = str(input('Digite uma frase: ')).upper().replace(' ','')

palindromo = frase[::-1]

if palindromo == frase:
    print('é um palindromo!')
else:
    print('não é um palindromo')