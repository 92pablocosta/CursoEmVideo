# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente. 
# Ao final, mostre o conteúdo das três listas geradas.

lista = []
listap = []
listai = []
escolha = int(input('Quantos números gostaria de digitar?'))
while len(lista) < escolha:
    n = int(input('Digite um número: '))
    lista.append(n)

    if n % 2 == 0:
        listap.append(n)
    else:
        listai.append(n)
print(f'Lista: {lista}')
print(f'Lista de números pares: {listap}')
print(f'Lista de números ímpares: {listai}')
