'''
Any e All

all() -> Retorna True se todos os elementos dos interaveis serem verdadeiros ou estiverem vazios
#Ex:
print(all([0,1,2,3,4])) #Todos os elementos sao verdadeiros ? False
print(all([1,2,3,4])) #Todos os elementos sao verdadeiros ? True
print(all([ ]))

nomes = ['Carlos',"Cristiano","Clezio","Cadu","Vanessa"]
print(all(nome[0]=="C" for nome in nomes))

print(all(letra for letra in 'ou' if letra in 'aeiou'))

Any() -> Retorna True se qualquer elemeno=to do interavel for verdadeiro, se o interavel for vazio, retorna False
any-> 'algum'


print(any([0,1,2,3])) #True
print(any([0,[],False,()])) #False
print(any([0,[],False,(),1])) #True

nomes = ['Carlos',"Cristiano","Clezio","Cadu","Vanessa"]
print(any(nome[0]=="C" for nome in nomes))
'''
