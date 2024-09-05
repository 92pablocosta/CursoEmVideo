# Faça um programa que leia o sexo de uma pessoa,
#  mas só aceite os valores ‘M’ ou ‘F’. Caso esteja errado, 
# peça a digitação novamente até ter um valor correto.

def meu_codigo():
    nome = input('Digite o seu nome: ')
    sexo = input('Digite o seu sexo: [M/F]').strip()
    while sexo != 'm' and sexo != 'f':
        print('Opção inválida, tente novamente.')
        sexo = input('Digite o seu sexo: [M/F]').strip()
    print(f'{nome}, {sexo}')

def codigo_guanabara():
    sexo = str(input('Informe seu sexo: [M/F]')).strip().upper()
    while sexo not in 'MmFf':
        sexo = str(input('Dados inválidos. Por favor, informe seu sexo: ')).strip().upper()
    print('Sexo {} registrado com sucesso!'.format(sexo))
