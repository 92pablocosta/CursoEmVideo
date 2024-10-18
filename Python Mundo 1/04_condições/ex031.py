# Desenvolva um programa que pergunte a distância de uma viagem em Km. 
# Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de 
# até 200Km e R$0,45 parta viagens mais longas

while True:
    distancia = float(input('Distância da viagem em km/h: '))
    preco = (0.50 if distancia <= 200 else 0.45) * distancia #Não precisa de parênteses
    if distancia <= 200:
        print('O valor da passagem é R${:.2f}'.format(preco))
    else:
        print('O valor da passagem é R${:.2f}'.format(preco))
