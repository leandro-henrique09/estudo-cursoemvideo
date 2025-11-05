# def lin():
#     print('-=' * 30)

# lin()
# print('SISTEMA DE ALUNOS')
# lin()
# lin()
# print('APRENDA PYTHON')
# lin()
# lin()
# print('CURSO EM VIDEO')
# lin()

# ===================================================================
# def mensagem(msg): # função com parametro 'msg'
#     print('-' * 30)
#     print(msg) # passando parametro no print
#     print('-' * 30)

# mensagem('      CURSO EM VIDEO      ') # usando a função mensagem com o parametro 'CURSO EM VIDEO'
# mensagem('      APRENDA PYTHON      ') # usando a função mensagem com o parametro 'APRENDA PYTHON'
# mensagem('      GUSTAVO GUANABARA      ') # usando a função mensagem com o parametro 'GUSTAVO GUANABARA'

# ====================================================================

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'A soma A + B = {s}')

# soma(4, 8)

# =====================================================================
# def dobra(lst):
#     pos = 0
#     while pos < len(lst):
#         lst[pos] *= 2
#         pos +=1


# valores = [6, 3, 9, 1, 0, 2]
# dobra(valores)
# print(valores)

# =========================================================================

def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os valores {valores} temos {s}')

soma(2,4,5)