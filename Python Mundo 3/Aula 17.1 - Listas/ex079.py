# Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista.
# Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.

lista = []
print('Digite valores para adicioná-los à lista. Digite 0 para encerrar')
while True:
    num = (int(input('Digite um valor: ')))
    if num == 0:
        break
    elif num in lista:
        print('O valor digitado já está na lista.')
    else:
        lista.append(num)
print(f'Os valores digitados foram {lista}')
