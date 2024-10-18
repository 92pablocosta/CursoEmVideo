#Crie um programa que leia o nome de uma
#cidade e diga se ela começa ou não com o nome 'Santo'.

cidade = input('Digite o nome da cidade:>').strip()
#cidade.lower()
#cidade.find('santo', 0, 4)
print(cidade[:5].upper == 'SANTO')
