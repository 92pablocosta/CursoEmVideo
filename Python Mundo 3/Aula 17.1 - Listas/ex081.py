# Crie um programa que vai ler vários números e colocar em uma lista. 
# Depois disso, mostre:
# A) Quantos números foram digitados.                                                                                                                    
# B) A lista de valores, ordenada de forma decrescente.
# C) Se o valor 5 foi digitado e está ou não na lista

lista = []

while len(lista) < 5:
    lista.append(int(input('Digite um número: ')))

lista.sort(reverse=True)
print(f'Lista em valores decrescentes: {lista}')
print(f'{len(lista)} Valores foram digitados')
if 5 in lista:
    print(f'O número 5 está presente na lista.')
else:
    print(f'O número 5 não está presente na lista.')
