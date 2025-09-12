# minha versao
cidade = str(input('Digite uma cidade: ')).strip()
cidade_maiusculo = cidade.upper()

print('SANTO' in cidade_maiusculo.split()[0])

# resposta do video
cid = str(input('Em que cidade você nasceu? ')).strip()
print(cid[:5].upper() == 'SANTO')