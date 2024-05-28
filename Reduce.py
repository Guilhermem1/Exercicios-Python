'''
Reduce
-> A partir do Python 3.0 a funcao reduce() não é mais uma funcao integrada (bult-in). Agora temos
que importar e utilizar esta funcao a partir do modulo 'functools'
--> Utilize reduce() se realmente precisar dela. 99% das vezes um loop é mais legível

Para entender o Reduce:
#Imagine que voce tem uma colecao de dados
dados = [a1,a2...an]
#E voce tem dois parametros
def funcao(x,y):
    return x*y

Assim como map() e filter(), a funcao reduce() recebe dois parametros: a funcao e o interavel
reduce(funcao,interavel)

A funcao reduce() funciona da seguinte forma:
    Passo 1: res1 = f(a1,a2) #Aplica a funcao nos dois primeiros elementos da colecao e guarda o resultado
    Pass 2: res2 = f(res1,a3) #Aplica a funcao passadno o resultado do passo1 mais o terceiro elemento e guarda em res
    .
    .
    .
    passo n: resn = f(resn,an)
'''

#Exemplo
#Multiplicacao de todos os numeros numa lista
from functools import reduce
dados = [2,3,5,7,9,15,12,6]
multi = lambda x,y: x*y  #Em reduce é necessario receber dois parametros
res = reduce(multi,dados)
print(res)

#Utilizando loop normal
res = 1
for n in dados:
    res = res *n

print(res)