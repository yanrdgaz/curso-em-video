# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis
# sobre ele.

algo = input('Digite algo: ')
print('O tipo primitivo desse valor é', type(algo))
print('É composta apenas por espaços?', algo.isspace())
print('É formado por números?', algo.isnumeric())
print('É formado apenas por letras (alfabético)?', algo.isalpha())
print('Possui letras e/ou números (alfanumérico)?', algo.isalnum())
print('Está completamente em maiúculo?', algo.isupper())
print('Está completamente em minúsculo?', algo.islower())
print('Está capitalizada?', algo.istitle())
