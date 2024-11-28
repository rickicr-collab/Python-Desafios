#------------Valores usando porcetagem --------------------------#
#opção 01
p = float(input('preço do produto a prazo: R$'))
D = p*5/100
print('Valor à vista:R$ {:.2f} '.format(p-D))

#opção 02
preço = float(input('Qual é o preço do produto R$:'))
novo = preço - ( preço * 5 / 100)
print('O produto que custava R${:.2f}, estando na promoção com desconto de 5% terá valor de: R${:.2f}'.format(preço, novo));

#opção 03
#calculando aumento de valor salarial 
salário = float(input('Digite seu salario do funcionário aqui?: R$'))
aumento = salário + (salário * 15 / 100)
print('O funcionario com salario R$ {}, com aumento de 15% possuirá salario de: R$ {}'.format(salário, aumento))
#------------------------------------------------------------------------------------------------
