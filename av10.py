#10) Escreva um algoritmo que leia um valor inicial A e imprima a seqüência de valores do cálculo de
#A! e o seu resultado. Ex: 5! = 5 X 4 X 3 X 2 X 1 = 120
if __name__ == '__main__':

    a = int(input("Digite um valor para A: "))
    fat = 1
    seq = ""
    for i in range(a, 0, -1):
        fat *= i
        seq += str(i)
        if i > 1:
            seq += " x "
    print("{}! = {} = {}".format(a, seq, fat))
