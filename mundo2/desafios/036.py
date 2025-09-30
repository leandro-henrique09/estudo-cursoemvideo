# minha resposta, foi a "mesma" do video
valor = float(input('Digite o valor da casa: '))
salario = float(input('Digite o salario do funcionario: '))
anos = int(input('Em quanto anos vai ser parcelado? '))
prestaçao = int(valor / (anos * 12))
print(prestaçao)

if prestaçao > salario * 30 / 100:
    print(f'Para pagar uma casa de R${valor:.2f} em {anos} anos será uma parcela de R${prestaçao} por mês.')
    print(f'Esse valor ultrapassa 30% do seu salário, sendo assim o empréstimo foi negado!')
else:
    print('Parabéns! Seu empréstimo foi aprovado.')