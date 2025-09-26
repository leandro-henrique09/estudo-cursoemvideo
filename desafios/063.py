termos = int(input('Quantos termos você quer mostrar? '))
count = 0
t1 = 0
t2 = 1
f = 0

while count < termos:
    print(f)
    t1 = t2
    t2 = f 
    f = t1 + t2
    count += 1
print('FIM')