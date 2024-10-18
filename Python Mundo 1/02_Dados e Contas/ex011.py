#Faça um programa que leia a largura e a altura de uma parede em metros,
#calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.

larg = float(input("Digite a largura da parede: "))
alt = float(input("Digite a altura da parece: "))

area_parede = larg * alt
tinta = area_parede / 2

print(f"Para pintar a parede que tem {area_parede}m², serão necessários {tinta}L de tinta")