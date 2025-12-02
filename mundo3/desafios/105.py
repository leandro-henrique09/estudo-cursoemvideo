def notas(*v, sit=False):
    lst = list(v)
    dados = {
        'total' : len(lst),
        'maior' : max(lst),
        'menor' : min(lst),
        'media' : sum(lst) / len(lst)
    }
    if sit:
        if 5 < dados['media'] < 7:
            dados['situação'] = 'Razoavel'
        elif dados['media'] < 5:
            dados['situação'] = 'Ruim'
        else:
            dados['situação'] = 'Boa'
    print(dados)

notas(3, 7, 8, sit=True)
