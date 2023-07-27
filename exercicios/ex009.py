# Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada (1 - 10).

num = int(input('Digite um número inteiro qualquer: '))
fator = 1

# Com loop while:
while fator <= 10:
    produto = num * fator
    print(f'{num} x {fator} = {produto}')
    fator += 1

# Com loop for:
for fator in range(1, 11):
    produto = num * fator
    print(f'{num} x {fator} = {produto}')
