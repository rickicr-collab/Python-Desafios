import random
n1 = str(input('Primeiro aluno: '))
n2 = str(input('Segundo aluno:'))
n3 = str(input('Terceiro aluno:'))
n4 = str(input('Quarto aluno:'))
lista = [n1, n2, n3, n4]
escolhido = random.choice(lista)
print('O aluno escolhido foi:{}'.format(escolhido))

#Um professor quer sortear um dos seus quatro alunos para apagar o quadro.Faca um programa que ajude ele. lendo o nome dos alunos e escrevendo o nome do escolhido.
#importando bliblioteca random .
#criando quatro variaveis do tipo string 
#apos cria uma lista que recebe as variaveis criadas 
#utiliza a propriedade random.choice com paramentro executando o paramentro lista 
#imprimi um valor escolhido pelo programa aleatoriamente das quatro variaveis criadas 
#opção de importar apenas a função choice de mat para simplificar codigos 