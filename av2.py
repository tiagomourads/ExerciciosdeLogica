#2) Desenvolver um algoritmo que leia a altura de 15 pessoas. Este programa deverá calcular e
#mostrar : a. A menor altura do grupo; b. A maior altura do grupo;
menor = 3.0
maior = 0.0

for i in range(15):
    altura = float(input("Digite a altura da pessoa %d em metros: " % (i+1)))
    if altura < menor:
        menor = altura
    if altura > maior:
        maior = altura

print("A menor altura do grupo é %.2f metros." % menor)
print("A maior altura do grupo é %.2f metros." % maior)