#Faça um programa que mostre os números pares entre 1 e 100, inclusive.


if __name__ == '__main__':
    for i in range(1, 101):
        if i % 2 == 0:
            print(i)
