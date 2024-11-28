#Exemplo 001
nome = str(input('Qual é o seu nome?')).capitalize()
if nome == 'Ricardo':
    print('Que nome lindo você tem!')
else:
    print('Seu nome é tão normal!')
print('Bom dia, {}!'.format(nome))   
#----------------------------------------
#Exemplo 002
n1 = float(input('Qual a primeira nota:'))
n2 = float(input('qual a seguna nota:'))
m = (n1 + n2) / 2
print('A sua média foi {:.1f}'.format(m))
if m >= 6.0:
  print('sua media foi boa PARABENS !')
else:
  print('Sua média foi ruim CUIDADO!')
#----------------------------------------
