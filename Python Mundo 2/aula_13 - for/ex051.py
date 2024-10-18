# Desenvolva um programa que leia o primeiro termo e a razão de uma PA. No final, 
# mostre os 10 primeiros termos dessa progressão.
def meu_codigo():
    print('='*30)
    primeiro = int(input('Digite o Primeiro Termo da PA: '))
    print('='*30)
    razao = int(input('Digite a Razão da PA: '))

    for c in range(1, 11):
        pa = primeiro + (c - 1)*razao
        print('Essa PA é é composta por: ', pa, end=' ')

def codigo_guanabara():
    primeiro = int(input('Prmeiro termo: '))
    razao = int(input('Razão: '))
    decimo = primeiro + (10 - 1) * razao

    for c in range(primeiro, decimo + razao, razao):
        print('{}'.format(c), end='- ')
    
    print('ACABOU')
