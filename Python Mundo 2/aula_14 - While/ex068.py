# Faça um programa que jogue par ou ímpar com o computador. 
# O jogo só será interrompido quando o jogador perder, 
# mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

from random import randint
from time import sleep

print('PAR OU ÍMPAR')
c = 0
while True:
    computador = randint(0, 11)
    numero = int(input('Digite um número: '))
    escolha = int(input('''O que você vai jogar?
                        [1] Par
                        [2] Ímpar\nEscolha: '''))
    resultado = computador + numero
    if escolha == 1:
        if resultado % 2 == 0:
            print('Você venceu essa rodada!')
            c += 1
        else:
            print('Você perdeu!')
            break
    if escolha == 2:
        if resultado % 2 == 0:
            print('Você perdeu!')
            break
        else:
            print('Você venceu essa rodada!')
            c += 1
print(f'Você conseguiu {c} vitória(s) seguida(s)!')



def codigo_guanabara():
    while True:
        jogador = int(input('Digite um valor: '))
        computador = randint(0, 10)
        total = jogador + computador
        tipo = ''
        while tipo not in 'PpIi':
            tipo = str(input('Par ou Ímpar? [P/I]: ')).strip().upper()[0]
        print(f'Você jogou {jogador} e o computador {computador}. Total de {total}')
        if tipo == 'P':
            if total % 2 == 0:
                print('Você VENCEU!!')
            else:
                print('Você perdeu.')
                break
        elif tipo == 'I':
            if total % 2 == 1:
                print('Você VENCEU!!')
                v += 1
            else:
                print('Você perdeu.')
                break
        print('Vamos jogar novamente...')
    print('GAME OVER! Você venceu {v} vezes!')
