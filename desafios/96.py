def area(l,c):
    a = l * c
    print(f'A área de um terreno {l}x{c} é de {a:.1f}m²')
def linha():
    print('-' * 30)


print('    Controle de terrenos    ')
linha()
larg = float(input('LARGURA(m): '))
comp = float(input('COMPRIMENTO(m): '))
area(larg, comp)