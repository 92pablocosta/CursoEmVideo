# Crie um programa que leia o nome e o preço de vários produtos. 
# O programa deverá perguntar se o usuário vai continuar ou não. 
# No final, mostre:
# A) qual é o total gasto na compra.
# B) quantos produtos custam mais de R$1000.
# C) qual é o nome do produto mais barato.

cont = 0
total = 0
mais_qmil = 0
baratissimo_preco = 0
baratissimo_nome = ''

while True:
    produto = str(input('Digite o nome do produto: ').strip().capitalize())
    preco = float(input('Digite seu preço: R$'))
    total += preco
    cont += 1

    if preco > 1000:
        mais_qmil += 1
    
    if cont == 1:
        baratissimo_preco = preco
        baratissimo_nome = produto

    
    if preco < baratissimo_preco:
        baratissimo_preco = preco
        baratissimo_nome = produto

    continuar = input('Deseja continuar? [S/N]: ').strip().upper()[0]
    if continuar == 'N':
        break

print(f'O total gasto na compra é R${total}')
print(f'{mais_qmil} produtos custam mais que R$1.000.')
print(f'{baratissimo_nome} é o produto mais barato.')
