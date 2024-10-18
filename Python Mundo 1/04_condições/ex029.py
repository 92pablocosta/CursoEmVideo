#Escreva um programa que leia a velocidade de um carro. Se ele 
# ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. 
# A multa vai custar R$7,00 por cada Km acima do limite.
from time import sleep

while True:
    speed = float(input('Velocidade do carro (km/h): '))
    multa = (speed - 80) * 7
    if speed > 80.0:
        print('VOCÊ FOI MULTADO.')
        print('Calculando valor da multa...')
        sleep(2)
        print('Você foi multado em R${:.2f}'.format(multa))
    else:
        print('Você está dentro do limite de velocidade.')
        break
