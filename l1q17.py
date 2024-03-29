"""17. Faça um Programa para uma loja de tintas. O programa deverá pedir o tamanho em metros quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para cada 6 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00 ou em galões de 3,6 litros, que custam R$ 25,00.
    ◦ Informe ao usuário as quantidades de tinta a serem compradas e os respectivos preços em 3 situações:
    ◦ comprar apenas latas de 18 litros;
    ◦ comprar apenas galões de 3,6 litros;
    ◦ misturar latas e galões, de forma que o desperdício de tinta seja menor. Acrescente 10% de folga e sempre arredonde os valores para cima, isto é, considere latas cheias."""
import math 
#entrada
area_pintada = float(input("Digite a área a ser pintada em m²: "))
#processamento das latas 
cobertura_da_tinta = area_pintada/6
numero_de_lata = cobertura_da_tinta/18
numero_de_lata_real = math.ceil(numero_de_lata)
valor_cada_lata = numero_de_lata_real * 80
#galoes
numero_de_galoes = cobertura_da_tinta/3.6
numero_de_galoes_real = math.ceil(numero_de_galoes)
valor_cada_galao = numero_de_galoes_real * 25
#latas e galoes
folga_10 = area_pintada + (10/100 * area_pintada)
numero_lata = math.floor(folga_10 / 100)
numero_galao = (folga_10 - 108) * (numero_lata)
numero_galao2 = math.ceil (numero_galao/21.6)
preço_total = (numero_lata * 80) + (numero_galao2 * 25)
#saida
print('Você precisa de {:.0f} latas e o valor total é: R${:.2f}'.format(numero_de_lata_real, valor_cada_lata))
print('Você precisa de {:.0f} galões e o valor total é: R${:.2f}'.format(numero_de_galoes_real, valor_cada_galao))
print('Você precisa de {:.0f} latas e {:.2f} galôes e o preço total é: R${:.2f}'.format(numero_lata, numero_galao2))
