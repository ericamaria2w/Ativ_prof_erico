#faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit
#°F = (9 * °C)/5 + 32

#entrada
temperatura_celcius = float (input('Digite a temperatura em celcius: '))

#processamento 
temperatura_Fahrenheit = (9 * temperatura_celcius)/5 + 32

#saida 
print('A temperatura {:.1f}°C é igual a {:.1f}°F'. format (temperatura_celcius, temperatura_Fahrenheitm))