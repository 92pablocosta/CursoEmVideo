# Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
from datetime import date

while True:
    ano = int(input('Digite o ano ou digite 0 para o ano atual: '))
    if ano == 0:
        ano = date.today().year # NEW
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0: # NEW
        print('O ano é bissexto')
    else:
        print('O ano NÃO é bissexto')
