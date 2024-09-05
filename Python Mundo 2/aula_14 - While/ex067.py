# Faça um programa que mostre a tabuada de vários números, 
# um de cada vez, para cada valor digitado pelo usuário. 
# O programa será interrompido quando o número solicitado for negativo.
contador = 1
while True:
    valor = int(input('Quer ver a tabuada de qual valor?: '))
    if valor < 0:
        print('Programa encerrado.')
        break
    else:
        while contador <= 10:
            print(f'{valor} x {contador} = {valor*contador}')
            contador += 1
    contador = 1
