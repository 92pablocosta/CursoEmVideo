# Faça um programa que leia um número inteiro e diga se ele é ou não um número primo.

def codigo_guanabara():
    num = int(input('Digite um número para saber se ele é Primo: '))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            print('\033[32m', end='')
            tot += 1
        else:
            print('\033[31m', end='')
        print('{} '.format(c), end='')

    print('\n\033[mO número {} foi divisível {} vezes'.format(num, tot))
    if tot == 2:
        print('E Por isso é PRIMO')
    else:
        print('E por isso NÃO é PRIMO')

def meu_codigo():
    num = int(input('Digite um número para saber se ele é PRIMO: '))
    tot = 0
    for c in range(1, num + 1):
        if num % c == 0:
            tot += 1
    if tot > 2:
        print('O número NÃO é PRIMO')
    else:
        print('É Primo.')

meu_codigo()
