# 1. Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor
# digitado.
name = input('Qual é o seu nome? ')
print('Olá,', name, '! Prazer em te conhecer!')

# 2. Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data
# formatada.
print('Eu gostaria de algumas informações sobre sua data de nascimento.')
day = input('Dia = ')
month = input('Mês = ')
year = input('Ano = ')
print('Você nasceu no dia', day, 'de', month, 'de', year, '.')

# 3.1  Crie um script Python que leia dois números e tente mostrar a soma deles.
print('Vamos efetuar uma soma:')
firstNumber = input('Primeiro número: ')
secondNumber = input('Segundo número: ')
print('A soma é', firstNumber + secondNumber)

# 3.2 Corrija o script 3.1.
print('Opa! Parece que há algo errado. Vamos tentar novamente.')
firstNumber = input('Primeiro número: ')
secondNumber = input('Segundo número: ')
print('A soma é', int(firstNumber) + int(secondNumber))
