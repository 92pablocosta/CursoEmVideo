# Crie um programa que leia a idade e o sexo de várias pessoas. 
# A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. 
# No final, mostre:
# A) quantas pessoas tem mais de 18 anos.
# B) quantos homens foram cadastrados.
# C) quantas mulheres tem menos de 20 anos.

maior_18 = homens = mulheres_20 = 0

while True:
    print('Cadastro sexo/idade. Digite 0 para sair.')
    idade = int(input('Digite sua idade: '))
    if idade == 0:
        print('Resultados: ')
        break
    sexo = int(input('qual o seu sexo: [1] Masculino / [2] Feminino: '))


    if idade >= 18:
        maior_18 += 1
    if sexo == 1:
        homens += 1
    if sexo == 2 and idade < 20:
        mulheres_20 += 1
    print('Cadastro feito com sucesso!\n')

print(f'{maior_18} pessoas são maiores de 18 anos.')
print(f'{homens} homens foram cadastrados.')
print(f'{mulheres_20} mulher tem menos de 20 anos.')
