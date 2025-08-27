# minha versão
largura = float(input('Indique a largura da parede: '))
altura = float(input('Indique a altura da parede: '))
area = largura * altura
qtd_tinta = area / 2

print('Sua parede tem a dimensão de {}x{} e sua área é de {}m²'.format(largura,altura,area))
print('Para pintar essa parede, você precisara de {}l de tinta.'.format(qtd_tinta))

# resposta do video
larg = float(input('Largura da parede: '))
alt = float(input('Altura da parede: '))
área = larg * alt
print('Sua parede tem a dimensão de {}x{} e sua área é de {}'.format(larg, alt, área))
tinta = área / 2
print('Para pintar essa parede, você precisará de {}l de tinta.'.format(tinta))