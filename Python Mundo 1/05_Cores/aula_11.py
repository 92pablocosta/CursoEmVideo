# teste = \033[0;30;41m todo harg
# Teste = \033[4;33;44m
# Teste = \033[1;35;43m
# Teste = \033[30;42m Sem padrão de estilo, não é preciso colocar se não tiver
# Teste = \033[m  - Fundo preto e letra cinza / padrão terminal
# Teste = \033[7: 30m Letra preta fundo branco usar código 7 de inversão

print('\033[1;31;43mOlá, mundo!\033[m')
print('\033[4;30;45mOlá, mundo!\033[m')
print('\033[7;30mOlá, mundo!\033[m')
print('\033[7;33;44mOlá, mundo!\033[m')

a = 3
b = 5
print('Os valores são \033[1;32m{}\033[m e \033[31m{}'.format(a, b))

cores = {'Limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[730m'
}
nome = 'Pablo'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format('\033[4;34m', nome, '\033[m'))

cores = {'Limpa':'\033[m', 
         'azul':'\033[34m', 
         'amarelo':'\033[33m', 
         'pretoebranco':'\033[730m'
}