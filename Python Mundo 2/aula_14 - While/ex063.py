# Escreva um programa que leia um número N inteiro qualquer e mostre na tela os N primeiros elementos de uma Sequência de Fibonacci. 
# Exemplo: 0 – 1 – 1 – 2 – 3 – 5 – 8

print('-' * 30)
print('SEQUÊNCIA DE FIBONACCI')
print('-' * 30)
n = int(input('Quantos termos gostaria de mostrar?: '))
contador = 2
n1 = 0
n2 = 1
print('{} - {} - '.format(n1, n2), end ='')
while contador < n:
    fibo = n1 + n2
    print('{} - '.format(fibo), end='')
    n1 = n2
    n2 = fibo
    contador += 1
print('FIM')
