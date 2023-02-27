#faça um programa que peça quatro notas bimestrais e mostre a média 
# somar as 4 notas por 4

#entrada das notas
nota_1 = float (input ('Digite sua primeira nota: '))
nota_2 = float (input ('Digite sua segunda nota: '))
nota_3 = float (input ('Digite sua terçeira nota: '))
nota_4 = float (input ('Digite sua quarta nota: '))
nota_5 = float (input ('Digite sua quinta nota: '))
nota_6 = float (input ('Digite sua sexta nota: '))
nota_7 = float (input ('Digite sua setima nota: '))
nota_8 = float (input ('Digite sua oitava nota: '))

#calculo da média 
media_do_1bimestre = (nota_1 + nota_2)/2
media_do_2bimestre = (nota_3 + nota_4)/2
media_do_3bimestre = (nota_5 + nota_6)/2
media_do_4bimestre = (nota_7 + nota_8)/2 

#exibir o resultado
print ('Sua média no primeiro bimestre é: ', media_do_1bimestre)
print ('Sua média no segundo bimestre é: ', media_do_2bimestre)
print ('Sua média no terçeiro bimestre é:', media_do_3bimestre)
print ('Sua média no quarto bimestre é:', media_do_4bimestre) 

#outra forma
nota1 = float (input('Digite sua primeira nota: '))
nota2 = float (input('Digite sua segunda nota: '))
nota3 = float (input('Digite sua terçeira nota: '))
nota4 = float (input('Digite sua quarta nota: '))

#calculo da média
media = (nota1 + nota2 + nota3 + nota4)/4

#exibir resultado 
print ('A média das {} {} {} {} notas é {:.2f}', format (nota1, nota2, nota3, nota4, media))