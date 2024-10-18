#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado
# e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

kms = int(input("Quanto km foram percorridos? "))
dias = int(input("Quantos dias o carro foi usado? "))

preco_final = (kms * 0.15) + (dias * 60)

print(f"O preço final é de R${preco_final}")