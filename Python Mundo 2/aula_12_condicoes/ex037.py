# Escreva um programa em Python que leia um número inteiro qualquer 
# e peça para o usuário escolher qual será a base de conversão:
#  1 para binário, 2 para octal e 3 para hexadecimal.

numero = int(input('Digite um número inteiro: '))
print('Opções de conversão: [1] Binário / [2] Octal / [3] Hexadecimal')
escolha = input('Digite sua escolha: ')

if escolha == '1':
    binario = format(numero, 'b')
    print('O número {} em binário é: {}'.format(numero, binario))
elif escolha == '2':
    octal = format(numero, 'o')
    print('O número {} em Octal é: {}'.format(numero, octal))
elif escolha == '3':
    hexadecimal = format(numero, 'x')
    print('O número {} em Hexadecimal é: {}'.format(numero, hexadecimal))
else:
    print('Opção inválida')
