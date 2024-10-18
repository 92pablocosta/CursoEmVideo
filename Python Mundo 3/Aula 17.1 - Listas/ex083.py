# Crie um programa onde o usuário digite uma expressão qualquer que use parênteses. 
# Seu aplicativo deverá analisar se a expressão passada está com os parênteses abertos e fechados na ordem correta.

frase = input('Digite uma expressão entre parênteses: ').strip()
if frase.count('(') == frase.count(')'):
    print(f'A frase {frase} está com os parênteses corretos.')
else:
    print('Tá faltando uns parênteses aí hein.')
