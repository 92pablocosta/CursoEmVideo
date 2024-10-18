# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar. 
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

print('Análise de Empréstimo\n')

valor_casa = float(input('Qual o valor da sua casa? R$'))
tempo_anos = int(input('Em quantos anos você deseja pagar? '))
print('O valor da parcela é de {}'.format(valor_casa / (tempo_anos*12)))
salario = float(input('Quanto você ganha por mês? R$'))

tempo_meses = (tempo_anos * 12)
limite_prestacao = salario * 0.3
valor_parcela = float(valor_casa / tempo_meses)

if valor_parcela > limite_prestacao:
    print('Infelizmente não podemos aprovar seu empréstimo com seu salário atual.', end='')
    print('O valor limite da sua parcela é de {}'.format(limite_prestacao))

else:
    print('Parabéns, seu empréstimo foi APROVADO')
    print('''Segue abaixo os dados do seu empréstimo:
          PARCELAS: {}
          VALOR POR PARCELA: {}
          
          Parabéns pela aquisição.'''.format(tempo_meses, valor_parcela))
