#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro).
#Sabendo que este vendedor ganha 15% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.

if __name__ == '__main__':
    nome = input('Digite o nome do vendedor: ')
    sal = float(input('Digite salario fixo: '))
    vd = float(input('Total de vendas do mês: '))
    vd1 = sal + 0.15 * vd

    print('TOTAL = R$ %.2f\n'%(vd1))

