# Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.


n1 = int(input('Primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
opcao = 0
while opcao != 5:
    print('''Escolha uma das opções:
                [1] Somar
                [2] Multiplicar
                [3] Maior
                [4] Novos Números
                [5] Sair do Programa''')
    opcao = int(input('Qual é a sua opção?:'))
    if opcao == 1:
        soma = n1 + n2
        print('A soma entre {} e {} é {}'.format(n1, n2, soma))
    elif opcao == 2:
        produto = n1 * n2
        print('O resultado de {} x {} é {}'.format(n1, n2, produto))
    elif opcao == 3:
        if n1 > n2:
            maior = n1
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
        if n2 > n1:
            maior = n2
            print('Entre {} e {} o maior valor é {}.'.format(n1, n2, maior))
        if n1 == n2:
            print('{} e {} são iguais.')
    elif opcao == 4:
        print('Informe os números novamente.')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opcao == 5:
        print('Finalizando...')
    else:
        print('Opção inválida, tente novamente.')
print('Fim do programa!')
