n1 = float(input('Digite a primeira nota'))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2)/2

print('A sua média foi {:.1f}'.format(media))
print('Média boa' if media >= 6 else 'Média ruim')
