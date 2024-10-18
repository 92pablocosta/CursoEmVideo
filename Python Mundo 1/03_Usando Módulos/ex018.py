#Faça um programa que leia um ângulo qualquer e
#mostre na tela o valor do seno, cosseno e tangente
#desse ângulo.

import math

angulo = float(input(('Digite o ângulo que você deseja: ')))
#converter o angulo para radianos
ar = math.radians(angulo)
seno = math.sin(ar)
cos = math.cos(ar)
tan = math.tan(ar)

print('O SENO do ângulo {} é: {:.2f}'.format(angulo, seno))
print('O COSSENO do ângulo {} é: {:.2f}'.format(angulo, cos))
print('A TANGENTE do ângulo {} é: {:.2f}'.format(angulo, tan))

