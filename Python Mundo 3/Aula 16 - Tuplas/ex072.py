# Crie um programa que tenha uma tupla totalmente preechida com uma contagem por extenso, de zero até 20.
# Seu programa deverá ler um número pelo teclado (entre 0 e 20) e mostrá-lo por extenso.

def codigo_guanabara():
    cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
    while True:
        num = int(input('Digite um número entre 0 e 20: '))
        if 0 <= num <= 20:
            break
        print('Tente novamente.', end='')
        
    print(f'Você digitou o número {cont[num]}')

while True:

    extenso = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quize', 
            'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    numero = int(input('Digite um número de 0 a 20: '))
    if numero == -1:
        break
    posicao_extenso = numero
    print(f'Você digitou o número {extenso[posicao_extenso]}.')


