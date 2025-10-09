extenso = ('zero','um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez',
'onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')

while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if num >= 0 and num <= 20:
        print(f'Você digitou o número {extenso[num]}')
    else:
        num = int(input('Tente novamente. Digite um número entre 0 e 20: '))
    
    continua = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continua not in 'Ss':
        break




    