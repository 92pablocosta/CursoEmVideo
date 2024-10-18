# Crie um programa que leia números inteiros pelo teclado. 
# O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada. 
# No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

from time import sleep


c = soma = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        print('Finalizando programa...')
        sleep(2)
        break
    c += 1
    soma += n
print(f'Você digitou {c} números e a soma entre eles é igual a {soma}.')
