#Faça um programa que leia um número de 0 a 9999 e mostre na
#tela cada um dos dígitos separados.
#Ex.: Digite um múmero: 1834
#Unidade: 4, Dezenas, 3, centenas: 8, Milhar: 1.

num = int(input('Digite um número de 1 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

print('Unidade: {} / Dezena {} / Centena {} / Milhar {}'.format(u, d, c, m))
