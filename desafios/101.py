from datetime import date
def voto(i):
    if 16 <= i < 18 or i >= 70:
        return 'VOTO OPCIONAL'
    elif i <= 16:
        return 'VOTO NEGADO'
    else:
        return 'VOTO OBRIGATÓRIO'
nascimento = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - nascimento
print(f'Com {idade} anos: {voto(idade)}')