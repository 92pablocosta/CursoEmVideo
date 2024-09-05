# Melhore o jogo do DESAFIO 28 onde o computador
# vai “pensar” em um número entre 0 e 10. Só que agora
# o jogador vai tentar adivinhar até acertar, mostrando
# no final quantos palpites foram necessários para vencer.

import random
from random import randint

def meu_codigo():
    numero = random.randint(1, 10)
    c = 1
    print('Olá! Eu pensei em um número de 1 a 10, você consegue adivinhar qual é?')
    print(numero)
    resposta = int(input('Digite seu palpite: '))
    while resposta != numero:
        resposta = int(input('Ihh, o número não é esse. Tente novamente: '))
        c += 1
    if c == 1:
        print('DE PRIMEIRA!! Tá com sorte hoje hein?')
    print('Depois de {} tentativas, você acertou o número {}!!'.format(c, numero))


def codigo_guanabara():
    computador = randint(0, 10)
    print('Sou seu computador... acabei de pensar em umm número entre 0 e 10.')
    print('Será que você consegue adivinhar qual é?')
    acertou = False
    palpites = 0
    while not acertou:
        jogador = int(input('Qual é o seu palpite?'))
        palpites += 1
        if jogador == computador:
            acertou == True
        else:
            if jogador < computador:
                print('Mais, tente mais uma vez.')
            elif jogador > computador:
                print('Menos, tente mais uma vez!')
    print('Acertou com {} tentativas, parabéns!'.format(palpites))
