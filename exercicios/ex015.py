# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos
# quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

dias = int(input('Digite a quantidade total de dias que o veículo estava alugado: '))
km = float(input('Digite a quantidade de total quilômetros (km) rodados pelo veículo durante o aluguel: '))
print(f'O valor total a ser pago é de R$ {(dias*60)+(km*0.15):.2f}.')
