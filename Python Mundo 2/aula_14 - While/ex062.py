# Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
# O programa encerrará quando ele disser que quer mostrar 0 termos.

def meu_codigo():
        
    primeiro = int(input('Digite o primeiro termo: '))
    razao = int(input('Digite a Razão da PA: '))
    contador = 0
    termo = primeiro
    while contador < 10:
        print('{} - '.format(termo), end='')
        termo += razao
        contador += 1
    print('FIM')

    adicionar = input('Gostaria de mostrar mais termos para essa PA?: [S/N] ').strip().upper()
    if adicionar == 'S':
        contador = 0
        termo = primeiro
        termos_a_mais = int(input('Digite quantos termos a mais gostaria de adicionar (0 para encerrar): '))
        if termos_a_mais == 0:
            print('FIM DO PROGRAMA')
        while contador < (10 + termos_a_mais):
            print('{} - '.format(termo), end='')
            termo += razao
            contador += 1
    print('FIM')

    if adicionar == 'N':
        print('FIM DO PROGRAMA')

def codigo_guanabara():
    print('Gerador de PA')
    print('-=' * 20)

    primeiro = int(input('Primeiro termo:'))
    razao = int(input('Razão da PA: '))
    termo = primeiro
    cont = 1
    total = 0
    mais = 10

    while mais != 0:
        total = total + mais
        while cont <= total:
            print('{} - '.format(termo), end='')
            termo += razao
            cont += 1
        print('PAUSA')
        mais = int(input('Quantos termos você quer mostrar a mais?: '))
    print('Progressão finalizada com {} termos mostrados'.format(total))
