# função para ter acesso a documentação de algum recurso python
help(input) # nesse caso, pegando a documentação do input

# ==========================================
# funções com parametros opcionais:

def somar(a,b,c=0):
    s = a + b + c
    print(f'A soma vale {s}')

somar(8,4) # neste caso o parametro c vai ser preenchido com 0
somar(1,3,5) # neste caso o parametro c vai ser preenchido com 5

# ====================================================

#  função com retorno
def soma(a,b,c):
    s = a + b + c
    return s

r1 = soma(2,4,7)
r2 = soma(1,6,3)
r3 = soma(9,3,7)
print(f'As somas foram de {r1}, {r2} e {r3}')

#  ======================= PARTE PRATICA =========================
