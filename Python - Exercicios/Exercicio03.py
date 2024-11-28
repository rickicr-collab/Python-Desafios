# -------exercicio de sucessor e antecessor--------------------
#faça um programa que leia o numero inteiro na tela e mostre o seu sucessor e seu antecessor 

N = int(input('Digite um valor:'))#atribuimos a função input a variavel n para ser inserido no console o valor desejado 
print('O antecessor de {} e {} e seu sucessor é {}'.format(N,N-1,N+1))#aqui colocamos em chaves os valores relacionados ao antecessor e sucessor do numero inserido no terminal do console

#segunda forma de realizar a operação de sucessor e antecessor 
n = int(input('Digite um numero aqui:'))
a = n-1
s = n+1
print('O antecessor de {} e {} e seu sucessor é {}'.format(n,a,s))
#---------------------------------------------------------------