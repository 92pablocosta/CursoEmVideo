# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, 
# desconsiderando os espaços. 
# Exemplos de palíndromos: APOS A SOPA, A SACADA DA CASA, A TORRE DA DERROTA, O LOBO AMA O BOLO, ANOTARAM A DATA DA MARATONA.

def meu_codigo():
    frase = str(input('Digite a frase: ')).strip().lower().split()
    junta_frase = (''.join(frase))

    if junta_frase == junta_frase[::-1]:
        print('A frase {} é um palíndromo!'.format(frase))
    else:
        print('A frase {} NÃO é um Palíndromo.'.format(frase))

def codigo_guanabara():
    print('O meu é melhor')
