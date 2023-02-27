#importa o valor de pi e a função potencia (pow) da biblioteca math                                     
from math import pi, pow

#faça um programa que peça o raio de um circulo, calcule e mostre sua área.
#área do circulo = pi * r * r

#entrada 
raio_do_circulo = float (input('Informe o tamanho do raio do círculo: '))

#processamento
area_do_circulo = 2 * pi * pow(raio_do_circulo,2)

#resposta 
print ('A área do circulo é {:.2f}'. format (area_do_circulo))
