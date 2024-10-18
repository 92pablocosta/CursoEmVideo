num = [1, 9, 4, 6, 3]
num[4] = 8
num.append(7)
num.sort(reverse=True)

num.insert(2, 0) #adicionar na posiçaõ 2 o valor 0

num.pop(2) #se vazio remove o ultimo número da lista
num.remove(9) #remove a primeira ocorrência do numero que vc quer eliminar
print(num)
print(f'Essa função tem {len(num)} elementos!')