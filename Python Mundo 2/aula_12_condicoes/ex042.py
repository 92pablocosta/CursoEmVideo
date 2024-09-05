# Refaça o DESAFIO 35 dos triângulos, acrescentando o recurso de 
# mostrar que tipo de triângulo será formado:
#– EQUILÁTERO: todos os lados iguais
#– ISÓSCELES: dois lados iguais, um diferente
#– ESCALENO: todos os lados diferentes

while True:
    print('Checando se o triângulo é possível. Digite o comprimento de 3 retas: \n')
    r1 = float(input('Comprimento primeira reta: \n'))
    r2 = float(input('Comprimento segunda reta: \n'))
    r3 = float(input('Comprimento terceira reta: \n'))

    if r1 + r2 > r3 and r2 + r3 > r1 and r3 + r1 > r2:
        triangulo_equilatero = r1 == r2 == r3
        triangulo_isoceles = r1 == r2 or r2 == r3 or r3 == r1
        triangulo_escaleno = r1 != r2 != r3 != r1
        
        if triangulo_equilatero:
            print('Este é um triângulo Equilátero.')

        elif triangulo_isoceles:
            print('Esse é um Triângulo Isóceles.')
        
        elif triangulo_escaleno:
            print('Esse é um Triângulo Escaleno.')
    
    else:
        print('Com essas retas não é possível formar um triângulo')