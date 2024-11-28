#--------media de valores----------------------------------------------------
nota1 = float(input('Primeira nota do aluno: '))#atribuido um valor da primeira nota com funçao input usando classe primitiva flutuante como criterio para o valor a ser inserido
nota2 = float(input('Segunda nota do aluno: '))#atribuido um valor para segunda nota com função input usando classe primitiva flutuante como critério para o valor a ser inserido
M = (nota1 + nota2) / 2 # aqui atribui,os variavel m realizando a função que dará o resultado da media das notas usando a soma dos valores das variaveis nota1 e nota2 dividindo o resultado por 2 não esquecendo de colocar parenteses nas variaveis devido a hierarquia das operações para que não haja erro na operação do seu programa e para boa pratica de programação 
print('O valor da média entre {} e {} será o valor de: {}'.format(nota1, nota2, M))#aqui realizada a função print informando no comentario os valores dos paramentros nas chaves e tambem resultado
#------------------------------------------------------------------------------------------------
