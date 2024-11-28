#----------------Aluguel de Carros-----------------------------#
Dias = int(input('quantos dias alugados? '))
km = float(input('quantos km rodados? '))
preço = (Dias*60) + (km*0.15)#variavel preço com duas operações uma referente a taxa paga por dia com carro alugado , com a taxa por quilometro rodado 
print('O total a se pagar R$:{:.2f}'.format(preço))#imprimi dados do valor real a pagar pelo serviço com todas as taxas inclusas
#------------------------------------------------------------------------------------------------

