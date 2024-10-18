#Crie um programa que leia quanto
#dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.

carteira = float(input("digite o valor em R$: "))
dolar = 5.10

conv = carteira / dolar

print(f"Você pode comprar ${conv} dólares")