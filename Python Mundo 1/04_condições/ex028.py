#Escreva um programa que faça o computador 'pensar' em um número inteiro
#entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número
#escolhido pelo computador.
#O programa deverá ecrever na tela se o usuário ganhou ou perdeu.

from random import randint
from time import sleep

computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Você consegue adivinhar que número eu pensei?')
print('-=-' * 20)
jogador = int(input('Digite um número: '))
print('PROCESSANDO...')
sleep(2) #NEW
if jogador == computador:
    print('ACERTÔ MIZERAVI')
else:
    print('ERROWW')

#num = [0, 1, 2, 3, 4, 5]
#guess_num = num[randint]
#print('Pensei em um número de 0 a 5. Vc consegue adivinhar qual é?')
#user_num = int(input('Número: '))
#if user_num == guess_num:
#    print('Acertô mizeravi')
#else:
#    print('ERROWW - Silva, Fausto')
