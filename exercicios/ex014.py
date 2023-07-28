# Escreva um programa que converta uma temperatura digitada em ºC e converta para ºF.

temp = float(input('Digite a temperatura em grau Celsius: '))
conversao = (temp*9/5) + 32
print(f'A temperatura {temp} ºC em Fahrenheit é {conversao} ºF.')
