#Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
from tkinter import *

pp = float(input("Preço do produto: "))

preco_desconto = pp * 0.95

print(f"O preço com desconto de 5% é de R${preco_desconto}")