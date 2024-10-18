# Desenvolva um programa que leia seis números inteiros e mostre 
# a soma apenas daqueles que forem pares. Se o valor digitado for 
# ímpar, desconsidere-o.

def meu_codigo():
    numeros = 0
    for c in range(1, 7):
        numeros[c] = int(input(('Digite um número: ')))
        if numeros[c] % 2 == 0:
            print(numeros)

def codigo_guanabara():
    soma = 0
    cont = 0
    for c in range(1, 7):
        num = int(input('Digite o {}º valor:'.format(c)))
        if num % 2 == 0:
            soma = soma + num # Simplificado: soma+=num
            cont = cont + 1 # Simplificado cont +=1
    print('Você informou {} números PARES e a soma foi {}'.format(cont, soma))

codigo_guanabara()
