#faça um progama que peça a temperatuda em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius
#°C = 5 ((°F-32) / 9).
#entrada 
temperatura_Fahrenheit = float (input('Temperatura em Fahrenheit: '))

#processamento 
#°F = (9 * °C) / 5 + 32
temperatura_em_celcius = 5 * ( temperatura_Fahrenheit - 32) / 9

#saída
print ('A temperatura {:.lf} °F é igual a {:.lf} °C '. format (temperatura_Fahrenheit, temperatura_em_celcius))