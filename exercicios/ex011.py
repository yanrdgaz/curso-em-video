# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta
# necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m².

largura = float(input('Digite a largura da parede em metros: '))
altura = float(input('Digite a altura da parede em metros: '))
area = largura * altura

print(f'Considerando a largura e altura mencionadas, a área desta parede é {area}m².\nConsiderando que 1L de tinta '
      f'pinta 2m², será necessário {(area/2)}L para pintar a parede em questão.')
