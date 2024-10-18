from math import ceil, trunc


'''num = float(input('Digite um número real: '))
#como fazer um if pra se a casa decimal for maior que 0.5 ou menor que 0.5?
print(f'O valor digitado foi {num}, e a sua porção inteira é {ceil(num)}')

#Resolução Guanabara
num = float(input('Digite um número: '))
print('O valor digitado foi {} e a sua porção inteira é {}').format(num, trunc(num))'''

num = float(input('Digite um valor: '))
print('O vaor digitado foi {} e a sua porção inteira é {}').format(num, int(num))
