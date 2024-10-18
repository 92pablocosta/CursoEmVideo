# Elabore um programa que calcule o valor a ser pago por um produto, 
# considerando o seu preço normal e condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto
#– à vista no cartão: 5% de desconto
#– em até 2x no cartão: preço formal 
#– 3x ou mais no cartão: 20% de juros
while True:
    valor_produto = float(input('Digite o valor do pruduto: R$'))

    forma_pagamento = input('''Como gostaria de pagar?
                            [1] Dinheiro/Cheque
                            [2] À vista no cartão
                            [3] 2x no cartão
                            [4] 3x ou mais no cartão)\n''')

    if forma_pagamento == '1':
        valor = valor_produto * 0.9
        print('Valor a pagar: R${:.2f}'.format(valor))

    elif forma_pagamento == '2':
        valor = valor_produto * 0.95
        print('Valor a pagar: R${:.2f}'.format(valor))

    elif forma_pagamento == '3':
        valor_parcelado = valor_produto / 2
        print('2x Parcelas de R${:.2f}'.format(valor_parcelado))
        print('Total a pagar: R${:.2f}'.format(valor_produto))

    elif forma_pagamento == '4':
        quantidade_parcelas = int(input('Em quantas parcelas deseja pagar? (limite 12x): '))
        valor_parcelado = valor_produto * 1.2
        valor_parcelas = valor_parcelado / quantidade_parcelas
        print('TOTAL: R${} em {}x R${}'.format(valor_parcelado, quantidade_parcelas, valor_parcelas))

    else:
        print('OPÇÃO INVÁLIDA.')
