def ex_1():
    for c in range(1, 10):
        print(c)
    print('fim')

def ex_2():
    c = 1 # Contado
    while c < 10:
        print(c)
        c = c + 1 # ou c += 1

def ex_3():
    for c in range(1, 3):
        n = int(input('Digite um valor: '))
    print('Fim')

def ex_4():
    n = 1
    while n != 0:
        n = int(input('Digite um valor: '))
    print('Fim')

def ex_5():
    r = 'S'
    while r == 'S':
        n = int(input('Digite um valor: '))
        r = str(input('Quer continuar? [S/N] ')).upper()
    print('Fim')

def ex_6():
    n = 1
    par = impar = 0
    while n != 0:
        n = int(input('Digite um valor: '))
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
    print('Você digitou {} números pares e {} números ímpares!'.format(par, impar))

    print('Acabou')
