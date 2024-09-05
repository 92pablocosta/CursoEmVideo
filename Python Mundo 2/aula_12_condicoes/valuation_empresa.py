print('Valuation')
faturamento_mes = float(input('Digite o lucro bruto mensal: R$'))
valor_empresa = faturamento_mes * 18
preco_sociedade = valor_empresa * 0.15
valor_estimado_mensal = faturamento_mes * 0.15
roi_mensal = (valor_estimado_mensal / preco_sociedade) * 100

print('O valor atual da empresa é de R${:.2f}'.format(valor_empresa))

print('O valor de compra de 1(uma) cota de sociedade (15%) é de R${:.2f}'.format(preco_sociedade))
print('Retorno estimado mensal: R${:.2f}'.format(valor_estimado_mensal))
print('ROI: R${:.2f}%'.format(roi_mensal))
