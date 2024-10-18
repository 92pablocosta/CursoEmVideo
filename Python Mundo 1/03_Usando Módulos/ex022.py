#Crie um programa que leia o nome completo de uma pessoa e
#mostre:
#O nome com todas as letras maiúsculas;
#O nome com todas minúsculas;
#Quantas letras tem o primeiro nome;
#Quantas letras ao todo (sem considerar espaços)

nome = str(input('Digite o nome: ')).strip()

print(f'Em letras maiúsculas: {nome.upper()}')
print(f'Em letras minúsculas: {nome.lower()}')
#print('Quantas letras tem o primeiro nome: {}'.format(nome.find(' ')))
print('Quantas letras tem o nome ao todo: {}'.format(len(nome) - nome.count(' ')))

separa = nome.split()
print('O seu primeiro nome é {} e ele tem {} letras'.format(separa[0], len(separa[0])))