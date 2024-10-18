while True:
    nome = str(input('Qual é o seu nome? >')).strip()
    if nome == 'Pablo':
        print('Que nome lindo você tem =O')
    else:
        print('Seu nome é tão normal :>')
    print('Bom dia {}'.format(nome))
    