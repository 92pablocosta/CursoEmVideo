# Faça um programa que mostre na tela uma contagem regressiva para o 
# estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 
# 1 segundo entre eles.

from time import sleep
import emoji

print('-=' * 20)
print('CONTAGEM REGRESSIVA PARA O ANO NOVO!!!!')
print('-=' * 20)
for c in range(10, 0, -1):
    print(f'{c}!!')
    sleep(1)
print(emoji.emojize('FELIZ ANO NOVO!!! :fireworks:'))
print("         .    '    ,")
print("   .  :      '    :   .")
print("    '.  .  :   .''  .")
print("  .     '    .      .")
print("    `.:.    :     .'")
print("       .  .'.   '")
print("         ''")
print("          '*")
print("          |")
print("         /|\\")
print("        / | \\")
print("       /  |  \\")
print("      /   |   \\")
print("     /    |    \\")
print("    /     |     \\")
print("   /      |      \\")
print("  /       |       \\")
print(" /        |        \\")
print("/         |         \\")
