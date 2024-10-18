#Faça um programa que leia o nome completo de uma pessoa, 
#mostrando em seguida o primeiro e o último nome separadamente.

nome_completo = str(input('Nome completo: '))
nome = nome_completo.strip().split()
print('O primeiro nome é {}'.format(nome[0].capitalize()))
print('O ultimo nome é {}'.format(nome[-1].capitalize()))

#Método Guanabara:
print('O último nome é {}'.format(nome[len(nome)-1]))
