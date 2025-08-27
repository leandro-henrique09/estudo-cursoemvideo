metro = float(input('Uma distância em metros: '))
km = metro / 1000
hm = metro / 100
dan = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('A medida de {:.1f}m corresponde a'.format(metro))
print('{:.3f}km'.format(km))
print('{:.2f}hm'.format(hm))
print('{}dan'.format(dan))
print('{}dm'.format(dm))
print('{}cm'.format(cm))
print('{}mm'.format(mm))
