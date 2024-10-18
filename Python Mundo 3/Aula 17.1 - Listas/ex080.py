# Crie um programa onde o usuário possa digitar cinco valores numéricos e cadastre-os em uma lista,
# já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.


lista = []

for i in range(5):
    n = int(input('Digite um valor: '))
    valor_inserido = False

    for j in range(len(lista)):
        if n < lista[j]:
            lista.insert(j, n)
            valor_inserido = True
            break
        
    if not valor_inserido:
        lista.append(n)
print(f'Lista: {lista}')
