#Faça um programa que leia algo pelo teclado e mostre na
#tela o seu tipo primitivo e todas as informações possíveis sobre ele.

a = input("Digite algo: ")

print(f"O tipo primitivo é {type(a)}")
print(f"O que foi digitado so tem espaços? R: {a.isspace()}")
print(f"É um número: R:{a.isnumeric()}")
print(f"É alfabético? R:{a.isalpha()}")
