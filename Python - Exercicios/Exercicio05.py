#-------- parametros de distançia--------------------------------
medida = float(input('Um valor em metros: '))#atribuida um valor para variavel medida com classe primitiva float por ser um nur=mero real com as regras de programaçao chamada flutuante 
cm = medida*100#variavel cm atribuida com operação relacionado a variavel medida multiplicando por 100
mm = medida*1000#variavel mm atribuida com operação relacionada a variavel medida multiplicando por 1000
dm = medida*10#variavel dm atribuida com operação relacionada a variavel medida multiplicando por 10
dam = medida/10#variavel dam atribuida com operação relacionada a variavel medida dividinodo por 10
hm = medida/100#variavel hm atribuida com operação relacionada a variavel medida dividindo por 100
km = medida/1000#variavel km atribuida com operação relacionado a variavel medida dividindo por 1000
print('O valor {} será em centrimentros é:{}cm'.format(medida, cm))#print da função com valor em centrimentos 
print('O valor {} será em milimetros é:{}mm'.format(medida,mm))#print da função com valor em milimetros
print('O valor {} em decimetros é:{}dm'.format(medida,dm))#print da função com valor em decimetros 
print('O valor {} em decametro é:{}dam'.format(medida,dam))#print da função com valor em decametros
print('O valor {} em hectometro é:{}hm'.format(medida,hm))#print da função com valor em hectometro
print('O valor {} em kilometro é:{}km'.format(medida,km))#print da função com valor em kilometros 
#------------------------------------------------------------------------------------------------------------