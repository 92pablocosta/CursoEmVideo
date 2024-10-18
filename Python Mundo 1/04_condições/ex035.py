# Desenvolva um programa que leia o comprimento de três retas 
# e diga ao usuário se elas podem ou não formar um triângulo.

#

ab = float(input('Comprimento da reta AB: '))
bc = float(input('Comprimento da reta BC:'))
cd = float(input('Comprimento da reta CD:'))

if ab + bc > cd and bc + cd > ab and cd + ab > bc:
    print('As retas PODEM formar um triângulo.')
else:
    print('As retas NÃO podem formar um triângulo.')
