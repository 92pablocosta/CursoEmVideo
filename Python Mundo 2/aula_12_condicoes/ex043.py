# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, 
# calcule seu Índice de Massa Corporal (IMC) e mostre seu status, 
# de acordo com a tabela abaixo:

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura ** 2)

if imc > 40:
    print('Seu IMC é {:.2f}Kg. Obesidade Mórbida'.format(imc))
elif imc >= 30:
    print('Seu IMC é {:.2f}Kg. Você está obeso.'.format(imc))
elif imc >= 25:
    print('Seu IMC é {:.2f}Kg. Você está com sobrepeso.'.format(imc))
elif imc >= 18.5:
    print('Seu IMC é {:.2f}Kg. Você está com seu peso ideal.'.format(imc))
else:
    print('Seu IMC é {:.2f}Kg. Você está abaixo do peso.'.format(imc))