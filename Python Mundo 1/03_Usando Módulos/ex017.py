#Faça um programa que leia o comprimento
#do cateto oposto e do cateto adjacente de
#um triângulo retângulo, calcule e mostre
#o comprimento da hipotenusa.
import math


co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))
h = math.hypot(co, ca)

print(f'A Hipotenusa é {h}')

#{:.2f} significa que o print só vai mostrar o resultado com duas casas decimais.