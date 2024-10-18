# Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, 
# na ordem de colocação. Depois mostre:
# a) Os 5 primeiros times.
# b) Os últimos 4 colocados.
# c) Times em ordem alfabética.
# d) Em que posição está o time da Chapecoense. 

print('-' * 22)
print('TABELA DO BRASILEIRÃO')
print('-' * 22)

top_20 = ('Botafogo', 'Flamengo', 'Fortaleza', 'Palmeiras', 'Cruzeiro',
          'São Paulo', 'Bahia', 'Athletico-PR', 'Atlético-MG', 'Bragantino',
          'Vasco da Gama', 'Criciúma', 'Juventude', 'Grêmio', 'EC Vitória',
          'Internacional', 'Fluminense', 'Corinthinans', 'Cuiabá', 'Atlético-GO')

onde_chapecoense = top_20.count('Chapecoense')


print(f'Os \033[1;32m5 primeiros\033[m times são \033[0;34m{top_20[0]}, {top_20[1]}, {top_20[2]}, {top_20[3]} e {top_20[4]}\033[m\n')
print(f'\033[1;31mOs 4 últimos\033[m colocados são: {top_20[19]} em último, seguido por {top_20[18]}, {top_20[17]} e {top_20[16]}\n ')
print(f'Os times em ordem alfabética são: {sorted(top_20)}')
if onde_chapecoense == 0:
    print('O Chapecoense não está no Top 20 do Brasileirão.\n')
else:
    print(f'O Chapecoense está na {top_20.index('Chapecoense') + 1} posição do Brasileirão!\n')
