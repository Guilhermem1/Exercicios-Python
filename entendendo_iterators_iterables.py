'''
Entendendo Iterators e Iterables
Iterator -> Um objeto que pode ser iterado.
            Um objeto que retorna um dado, sendo um elemento por vez quando uma funcao next() é chamdada;
            
Iterable -> Um objeto que retornará um interator quando a funcao iter() for chamada
'''

nome = "Geek" # è um interable mas nao iterator
numeros = [1,2,3,4,5] # É um interable mas nao iterator

#print(next(nome)) # Erro
it1 = iter(nome)
it2 = iter(numeros)

print(next(it1))
print(next(it1))
print(next(it1))
print(next(it1))

print(next(it2))
print(next(it2))
print(next(it2))
print(next(it2))

