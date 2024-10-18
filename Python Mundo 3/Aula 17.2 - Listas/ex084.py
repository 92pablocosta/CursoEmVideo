# Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.
# B) Uma listagem com as pessoas mais pesadas.
# C) Uma listagem com as pessoas mais leves.

lista = []
nome_peso = []
contador = 0

for i in range(5):
    nome = input('Digite o nome: ')
    lista.append(nome)
    peso = float(input('Digite o peso da pessoa: '))
    lista.append(peso)
    if contador == 0:
        nome_peso.append(lista[:])
    else:
        for i in range(len(nome_peso)):
            if lista[1] > nome_peso[i][1]:
                nome_peso.append(lista[:])
            elif lista[1] < nome_peso[i][1]:
                nome_peso.insert([i], lista[:])
    
    contador += 1
    lista.clear()

print(nome_peso)