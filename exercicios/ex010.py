# Crie um programa que leia o quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
# Considere US$ 1.00 = R$ 3.27

n = float(input('Digite o valor que possui em reais: R$ '))
print(f'R$ {n:.2f} pode comprar o equivalente aproximado de US$ {n/3.27:.2f}.')
