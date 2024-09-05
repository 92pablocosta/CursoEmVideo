# Crie um programa que leia vários números inteiros pelo teclado. 
# No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. 
# O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.

n = int(input('Digite um valor: '))
opcao = input('Quer continuar digitando? [S/N]: ').strip().upper()
contador = 1
soma = n
maior = n
menor = n

while opcao == 'S':
    n = int(input('Digite outro valor: '))
    if n > maior:
        maior = n
    if n < menor:
        menor = n
    soma += n
    contador += 1
    opcao = input('Quer continuar digitando? [S/N]: ').strip().upper()

print('Você digitou {} valores, sendo o MAIOR = {}, o MENOR = {} e a média dos valores digitados é {}'.format(contador, maior, menor, (soma / contador)))
