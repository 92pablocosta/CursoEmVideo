# Crie um programa que tenha uma tupla com várias palavras (não usar acentos). 
# Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.


def meu_codigo():
    palavras = ('Notebook', 'Monitor', 'Kadabra', 
                'Kangaroo', 'Viagem', 'Python', 
                'Mesa', 'Cadeira')

    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    cont = 0
    for palavra in palavras:
        a = palavra.count('a')
        e = palavra.count('e')
        i = palavra.count('i')
        o = palavra.count('o')
        u = palavra.count('u')

        print(f'{palavra}: ', end='')
        print(f'Letra a: {a}, letra e: {e},letra i: {i}, letra o {o},  letra u: {u}\n')
        cont += 1

def codigo_guanabara():
    palavras = ('Notebook', 'Monitor', 'Kadabra', 
                'Kangaroo', 'Viagem', 'Python', 
                'Mesa', 'Cadeira')
    
    for p in palavras:
        print(f'\nNa palavra {p.upper()} temos ', end='')
        for letra in p:
            if letra.lower() in 'aeiou': # Dá pra pegar vogais com acento: if letra.lower() in 'aàáãoóò'
                print(letra, end=' ')

codigo_guanabara()

# 78: Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. 
# No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

palavra = ('otorrinolaringologista', 'inconstitucionalicimamente')

print(palavra[0].count('a'))
print(palavra[0].count('o'))

# 79: Crie um programa onde o usuário possa digitar vários valores numéricos
# e cadastre-os em uma lista.
#  Caso o número já exista lá dentro, ele não será adicionado. 
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente. 

lista = []
while True:
    num = int(input('Digite um valor: '))
    if num == -1:
        break
    if num in lista:
        print('O valor já existe na lista.')
    else:
        lista.append(num)
lista.sort()
print(f'A lista com os valores ordenados é: {lista}')
