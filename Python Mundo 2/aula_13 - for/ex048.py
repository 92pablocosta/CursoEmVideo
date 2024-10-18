# Faça um programa que calcule a soma entre todos os números
# que são múltiplos de três e que se encontram no intervalo
# de 1 até 500.

def meu_codigo():
    soma = 0
    for n in range(1, 501):
        if n % 3 == 0:
            soma += n

def codigo_rapido():
    return sum(n for n in range(1, 501) if n % 3 == 0)

def codigo_guanabara():
    for c in range(1, 501, 2):
        if c % 3 == 0:
            soma += c
            cont += 1
    print('A soma de todos os {} valores solicitados é {}'.format(cont, soma))

print(meu_codigo())