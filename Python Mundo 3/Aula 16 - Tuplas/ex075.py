# Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. 
# No final, mostre:
# A) Quantas vezes apareceu o valor 9.
# B) Em que posição foi digitado o primeiro valor 3.
# C) Quais foram os números pares.

num = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Osvalores digitados são: {num}\n')
print(f'O valor 9 apareceu {num.count(9)} vezes\n')
if 3 in num:
    print(f'O primeiro valor 3 está na posição {num.index(3)}\n')
else:
    print('Não há ocorrência do número 3 na tupla.\n')

#for n in num:
#    if n % 2 == 0:
#        print(n, end='')
for c in num:
    if c % 2 == 0:
        print(c, end='')
    else:
        print('Não há números pares.')
        break
