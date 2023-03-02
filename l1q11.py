"""Faça um programa que peça dois números inteiros e um número real.
    Calcule e molstre:
        °O produto do dobro do primeiro com metade do segundo.
        °A soma do triplo do primeiro com o terçeiro.
        ° O terçeiro elevado ao cubo."""

#entrada 
numero_1 = int (input('Digite o 1° número inteiro: '))
numero_2 = int (input('Digite o 2° número inteiro '))
numero_real = float (input('Digite um número real: '))

#processamento 
calculo_1 = numero_1 * 2 * numero_2 / 2
calculo_2 = 3 * numero_1 + numero_real
calculo_3 = numero_real * numero_real * numero_real

#saída 
print ('O produto do dobro do primeiro com metade do segundo: {}'. format(calculo_1))
print ('A soma do triplo do primeiro com o terçeiro: {}'. format(calculo_2))
print ('O terçeiro elevado ao cubo: {}'. format(calculo_3))