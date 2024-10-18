# A Confederação Nacional de Natação precisa de um programa que leia
#  o ano de nascimento de um atleta e mostre sua categoria,
#  de acordo com a idade:
#– Até 9 anos: MIRIM
#– Até 14 anos: INFANTIL
#– Até 19 anos: JÚNIOR
#– Até 25 anos: SÊNIOR
#– Acima de 25 anos: MASTER

while True:
    from datetime import date

    atual = date.today().year
    nascimento = int(input('Digite se ano de nascimento: '))
    idade = int(atual - nascimento)

    if idade <= 9:
        print('Categoria MIRIM')
    elif 9 < idade <= 14:
        print('Categoria INFANTIL.')
    elif 14 < idade <= 19:
        print('Categoria JUNIOR')
    elif 19 < idade <= 25:
        print('Categoria SÊNIOR')
    else:
        print('Categoria MASTER')
