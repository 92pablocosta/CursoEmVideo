# Crie um programa que leia duas notas de um aluno e calcule sua média, 
# mostrando uma mensagem no final, de acordo com a média atingida:

nota1 = float(input('Digite a primeira nota: '))
nota2 = float(input('digite a segunda nota: '))

media = (nota1 + nota2) / 2

if media >= 7:
    print('PARABÉNS, você foi aprovado com média {:.1f}'.format(media))
else:
    print('Você não atingiu a média de aprovação. Sua média foi{:.1f}'.format(media))
