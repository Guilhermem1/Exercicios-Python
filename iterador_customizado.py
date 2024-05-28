'''
Escrevendo um iterador customizado


'''

class contador:
    def __init__(self,menor,maior):
        self.menor = menor
        self.maior = maior

    def __iter__(self):  # ==> it = iter(cont)
        return self

    def __next__(self):  # == next(it)
        if self.menor < self.maior:
            numero = self.menor
            self.menor = self.menor + 1
            return numero
        raise StopIteration

cont = contador(1,6)
print(cont.menor)
print(cont.maior)

it = iter(cont)
print(next(it))
print(next(it))
print(next(it))
print(next(it))
print(next(it))


#print(it)  # Ele nao é iterable
# Para fazer ele interable fazemos o que foi feito a partir da 2 funcao:
(print(20*'-'))
for n in contador(15,20):
    print(n)