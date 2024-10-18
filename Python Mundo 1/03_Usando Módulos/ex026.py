#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, 
#em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
frase = input('Digite uma frase: ').strip()
print('''A letra A aparece {} vezes
       sendo a primeira vez na posição {}
       e a ultima na posição {}'''.format(frase.count('A'), frase.find('A'), frase.rfind('A')))