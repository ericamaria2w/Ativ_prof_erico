#Tendo como dados de entrada a altura de uma pessoa, construa um algoritmo que calcule seu peso ideal, usando a seguinte fórmula: (72.7*altura) - 58
#entrada
altura = float(input('Digite sua altura: '))
#processamento
calculo = 72.7* (altura) - 58
#saida
print('Seu peso ideal é:{:.2f} '.format(calculo))