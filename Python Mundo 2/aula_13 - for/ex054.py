# Crie um programa que leia o ano de nascimento de sete pessoas. 
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date

def meu_codigo():
    datas = 0
    for c in range(1, 7):
        data = int(input('Digite o ano de nascimento da {}º pessoa: '.format(c)))
        idade = date.year - data
        print(idade)

def codigo_guanabara():
    atual = date.today().year
    total_maior = 0
    total_menor = 0
    for pess in range(1, 8):
        nascimento = int(input('Em que ano a pessoa {}º nasceu?').format(pess))
        idade = atual - nascimento
        if idade >= 21:
            total_maior += 1
        else:
            total_menor += 1

    print('Ao todo ivemos {} pessoas maiores de idade'.format(total_maior))
    print('E também tivemos {} pessoas menores de idade.'.format(total_menor))
    