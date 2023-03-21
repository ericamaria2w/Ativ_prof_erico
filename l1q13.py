"""Tendo como dado de entrada a altura (h) de uma pessoa, construa um algoritmo que calcule seu peso ideal, utilizando as seguintes fórmulas:
    ◦ Para homens: (72.7*h) - 58
    ◦ Para mulheres: (62.1*h) - 44.7"""
#entrada
altura = float (input('Digite sua altura: '))

#processamento
homens = 72.7 * (altura) - 58
mulheres = 62.1 * (altura) - 44.7

print('Se você for homem, seu peso ideal é:',(homens))
print('Se você for mulher, seu peso ideal é:',(mulheres))