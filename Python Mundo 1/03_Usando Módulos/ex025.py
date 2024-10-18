#Crie um programa que leia o nome de 
#uma pessoa e diga se ela tem “SILVA” no nome.

nome = (input('Digite o nome: ')).strip()
print('O seu nome tem Silva? {}'.format('silva' in nome.lower()))