# Faça um programa que leia o ano de nascimento de um jovem e informe, 
# de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, 
# se é a hora exata de se alistar ou se já passou do tempo do alistamento. 
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import datetime

# GUANABARA:
# from datetime import date
# atual = date.today().year

data_atual = datetime.now()

nascimento = int(input('Digite seu ano de nascimento: '))
idade = int(data_atual.year - nascimento)

if idade < 18:
    print('Você não está na idade de se alistar.')
    print('Você pode se alistar em {} ano(s)'.format(18 - idade))
elif idade == 18:
    print('Você está na hora exata de se alistar.')
else:
    print('Você está em atraso com o serviço militar em {} ano(s)'.format(idade - 18))
