peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / altura ** 2

if imc < 18.5:
    print(f'Seu imc é {imc:.2f} e está abaixo do peso.')
elif 25 > imc >= 18.5:
    print(f'Seu imc é {imc:.2f} e você está no peso ideal.')
elif 30 > imc >= 25:
    print(f'Seu imc é {imc:.2f} e você esta com sobrepeso.')
elif 40 > imc >= 30:
    print(f'Seu imc é {imc:.2f} e você está com obesidade')
else:
    print(f'Seu imc é {imc:.2f} e você está com obesidade mórbida')