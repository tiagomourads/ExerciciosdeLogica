#5) Faça um algoritmo estruturado que leia uma quantidade não determinada de números positivos.
#Calcule a quantidade de números pares e ímpares, a média de valores pares e a média geral dos
#números lidos. O número que encerrará a leitura será zero.
if __name__ == '__main__':
    soma_total = 0
    qtd_total = 0
    soma_pares = 0
    qtd_pares = 0

    while True:
        numero = int(input("Digite um número, caso queira encerrar, digite o número zero: "))
        if numero == 0:
            break
        if numero % 2 == 0:
            soma_pares += numero
            qtd_pares += 1
        soma_total += numero
        qtd_total += 1

    media_geral = soma_total / qtd_total
    print("Média geral dos números lidos:", media_geral)
    if qtd_pares > 0:
        media_pares = soma_pares / qtd_pares
        print("Média de valores pares:", media_pares)
    print("Quantidade de números pares:", qtd_pares)
    print("Quantidade de números ímpares:", qtd_total - qtd_pares)
