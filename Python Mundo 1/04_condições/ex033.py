# Faça um programa que leia três números e mostre qual 
# é o maior e qual é o menor.

while True:
    a = int(input('Digite um número(1/3): '))
    b = int(input('Digite um número(2/3): '))
    c = int(input('Digite um número(3/3): '))

    menor = a
    if b<a and b<c:
        menor = b
    if c<a and c<b:
        menor = c
    #Verificando quem é o maior
    if b>a and b>c:
        maior = b
    if c>a and c>b:
        maior = c

    print ('O maior valor digitado é {}'.format(maior))
    print('O menor valor digitado foi {}'.format(menor))
    