# minha resolução; 
abr = []
fech = []
exp = str(input('Digite uma expressão: '))
for p in exp:
    if p == '(':
        abr.append(p)
    elif p == ')':
        fech.append(p)

if exp[0] == ')':
    print('Sua expressão está invalida')
elif len(abr) == len(fech):
    print('Sua expressão está correta! ')
else:
    print('Sua expressão está invalida')

# resolução do video
expr = str(input('Digite a expressão: '))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')') 
            break
if len(pilha) = 0:
    print('Sua expressão está valida!')   
else:
    print('Sua expressão está errada!')