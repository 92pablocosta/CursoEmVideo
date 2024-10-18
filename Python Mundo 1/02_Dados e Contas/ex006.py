#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
from math import sqrt
n = int(input("Digite um número: "))

dobro = n * 2
triplo = n * 3
raiz = sqrt(n)

print(f'''Tendo como baso o número {n}, temos:
Dobro {dobro}
Triplo {triplo}
Raiz Quadrada {raiz}''')