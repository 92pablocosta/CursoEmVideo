#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

m = float(input("Digite o valor em metros (ex. 1.80): "))

cm = m*100
mm = m*1000

print(f"{m} metros equivale a {cm} centímetros e {mm} milímetros")