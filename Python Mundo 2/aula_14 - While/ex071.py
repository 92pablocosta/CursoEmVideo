# Crie um programa que simule o funcionamento de um caixa eletrônico. 
# No início, pergunte ao usuário qual será o valor a ser sacado (número inteiro) 
# e o programa vai informar quantas cédulas de cada valor serão entregues. OBS:
# considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.

print('-' * 20)
print(f'CAIXA ELETRÔNICO')
print('-' * 20)

cedulas_1 = cedulas_10 = cedulas_20 = cedulas_50 = 0

while True:
    saque = int(input('Quanto deseja sacar? R$')) # Valor a ser sacado
    print('SAQUE REALIZADO COM SUCESSO')
    
    if saque >= 50:
        cedulas_50 = saque // 50 # Divide por 50 e descarta o resto, resultado na quantidade de cédulas de 50
        saque %= 50 # Subtrai tudo que é divisível por 50 e returna o resto (ex: Se o valor é 63, o %= é igual a 13), retorna esse valor para 'saque'
        print(f'{cedulas_50} nota(s) de R$50')

    if saque >= 20:
        cedulas_20 = saque // 20
        saque %= 20
        print(f'{cedulas_20} nota(s) de R$20')

    if saque >= 10:
        cedulas_10 = saque // 10
        saque %= 10
        print(f'{cedulas_10} nota(s) de R$10')
    
    if saque >= 1:
        cedulas_1 = saque
        print(f'{cedulas_1} nota(s) de R$1\n')

    continuar = input('Gostaria de realizar outro saque? [S/N]: \n').strip().upper()[0]

    if continuar == 'N':
        break
print('Agradecemos pela preferência!')

def codigo_guanabara():
    
    valor = int(input('Que valor você quer sacar? R$'))
    total = valor
    ced = 50
    totced = 0
    while True:
        if total >= ced:
            total -= ced
            totced += 1
        
        else:
            if totced > 0:
                print(f'Total de {totced} cédulas de R${ced}')
            if ced == 50:
                ced = 20
            elif ced == 20:
                ced = 10
            elif ced == 10:
                ced = 1
            totced = 0
            if total == 0:
                break
    print('Obrigado pela preferência!')