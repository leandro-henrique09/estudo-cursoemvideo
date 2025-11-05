def escreva(msg):
    print('~' * len(msg))
    print(f'{msg}')
    print('~' * len(msg))

text = str(input('Digite uma palavra: '))
escreva(text)