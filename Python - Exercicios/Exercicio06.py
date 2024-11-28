#---------Conversor de Moedas -----------------#
#modos de realizar conversões de moeda atribuido variaves para realizar operações 
real = float(input('Quanto dinheiro eu tenho na carteira?: R$'))
dolar = real/3.27#valor atribuido a variavel dolar dividindo o valor por 3.27 realizando a conversão de reais em dolar 
print('-'*30)#print de uma string realizando a multiplicação da mesma e imprimindo o valor na execução do programa no cabeçalho
print('Com R${:.2f} Você pode comprar em US$: {:.2f}'.format(real, dolar))
print('-'*30)#print de uma string realizando a multiplicação da mesma e imprimindo o valor na execução do programa no fechamento do programa 
#-----------------------------------------------------------------------------
