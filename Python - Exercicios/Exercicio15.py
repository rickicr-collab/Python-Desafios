#Faça um programa que leia um angulo qualquer e mostre na tela o valor de seno,cosseno e tangente desse angulo#
#importando a bliblioteca math para realizar as operações 
import math
an = float(input('digite o ângulo que voê deseja: '))
seno = math.sin(math.radians(an))
cosseno = math.cos(math.radians(an))
tangente = math.tan(math.radians(an))
print('>'*50)
print('O valor {}\npossui seno {:.2f}\ncosseno {:.2f}\ntangente {:.2f}\n'.format(an, cosseno, seno, tangente))
print('>'*50)

#criado a variavel seno , cossendo e tangente usando a função math.radians para (math.sin(an) + math.cos(an) + math.tan(an))
#apos isso imprimir os valores já convertidos em cada operações com simmples formatações para uma leitura dos valores mais aceitavel devido muitos algarismo 
#apricando uma quebra de panisa ao utilizamos o algaritmo (\n)

#a segunda forma de se criar esse programa fazendo apenas algumas alteraçoes e da blblioteca math importar apenas as operaçoes utilizadas no programa como por exemplo Math(cos,sin,tan,radinas) apos iimportas as operaçoes todas as mencoes a bliblioteca math pode sem apagadas deixando apenas suas operaçoes nas linhas apos isso o resultado no programa será executado normalmente afinal vc esta usando as operaçoes necessarias para o programa#