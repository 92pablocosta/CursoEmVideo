# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: 
# a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
def meu_codigo():
    maior_idade_homem = 0
    contador_idade_mulheres = 0
    soma_idade = 0
    for p in range(1, 5):
        nome = str(input('Digite o nome da {}ª pessoa: '.format(p))).strip()
        sexo = int(input('Qual o sexo da {}ª pessoa? [1] Masculino [2] Feminino: '.format(p)))
        idade = int(input('Digite a idade da {}ª pessoa: '.format(p)))
        soma_idade += idade

        if p == 1 and sexo == 1:
            maior_idade_homem = idade
        if sexo == 1 and idade > maior_idade_homem:
            maior_idade_homem = idade
        if sexo == 2 and idade < 20:
            contador_idade_mulheres += 1

    print('A média de idade do grupo é de {} anos.'.format(soma_idade / 4))
    print('O homem mais velho tem {} anos'.format(maior_idade_homem))
    print('{} mulhere(s) tem menos de 20 anos'.format(contador_idade_mulheres))

meu_codigo()
