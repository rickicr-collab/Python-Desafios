#O mesmo professor do desafio anterior quer sortear a ordem  de apresentação do trabalhos dos alunos.Faca um programa que leia a nome dos quatro alunos e mostra a ordem sorteada#
import random
n1 = str(input('Primeiro Aluno:'))
n2 = str(input('Segundo Aluno:'))
n3 = str(input('Terceiro Aluno:'))
n4 = str(input('Quarto Aluno: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista) # usando a função shuffle para tornar aleatorio a ordem da apresentação 
print('A ordem de apresentação será: {}'.format(lista))
