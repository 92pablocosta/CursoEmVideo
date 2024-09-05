# Refaça o DESAFIO 51, 
# lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos 
# da progressão usando a estrutura while.

def meu_codigo():
    n = int(input('Digite o primeiro número da PA: '))
    r = int(input('Digite a razão: '))
    #faltou o termo t = n
    c = 0
    print('Os dez primeiros termos da PA são: '.format(n), end='')
    while c < 11:
        print('{} - '.format(pa), end='')
        pa = n + r # termo += r
        c += 1
    print('FIM')

def codigo_guanabara():
    primeiro = int(input('Primeiro termo'))
    razao = int(input('Razão da PA: '))
    termo = primeiro
    cont = 1
    while cont <= 10:
        print('{} - '.format(termo), end='')
        termo += razao
        cont += 1
    print('fim')