# Crie um programa que leia vários números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
from time import sleep
n = int(input('Digite um número (999 para encerrar): '))
contador = soma = 0
while n != 999:
    contador += 1
    soma += n
    n = int(input('Digite outro número: '))
if n == 999:
    print('Calculando...')
    sleep(2)
print('Você digitou {} números e a soma deles é {}.'.format(contador, soma))
