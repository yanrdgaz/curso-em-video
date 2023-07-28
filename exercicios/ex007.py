# Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# Forma fácil:
n1 = int(input('Digite a primeira nota: '))
n2 = int(input('Digite a segunda nota: '))
print(f'A média das notas é {(n1+n2)/2}.')

# Forma com ponto flutuante:
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
print(f'A média das notas é {(n1+n2)/2:.1f}.')

# Adaptação:
n1 = float(input('Digite a primeira nota (com uma casa decimal): '))
n2 = float(input('Digite a segunda nota (com uma casa decimal): '))

try:
    n1 = round(float(n1), 1)
    n2 = round(float(n2), 1)
except ValueError:
    print('Entrada inválida. Digite um valor com uma casa decimal. Exemplo: 8.5')

print(f'A média das notas é {(n1+n2)/2:.1f}.')
