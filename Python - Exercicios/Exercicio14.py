#faça um programa que leia o comprimento do cateto oposo e do cateto adjacente de um triangulo retangulo, calcule e mostre o comprimento da hipotenusa 
#forma importantdo a blblioteca math e utilizando a propriedade hypot da bliblioteca math 
import math
cato = float(input('digite o cateto oposto:'))
cata = float(input('digite o cateto adjacente: '))
hipo = math.hypot(cato,cata)
print('A hypotenusa é : {:.2f}'.format(hipo))
#-----------------------------------------------------------------------------------
#forma de realizar usando operações atitmeticas 
co = float(input('digite o cateto oposto:'))
ca = float(input('digite o cateto adjacente:'))
hi = (co ** 2 + ca ** 2) ** (1/2)
print('A hipotenusa é: {:.2f}'.format(hi))
#------------------------------------------------------------------------------------