'''
Modulo Random
-> Modulo são outros arquivos do Python
Modulo Ranodm possui varias funcoes para geração de numeros pseudo-aleatorios


#OBS: Existe duas formas de se utilizar um modulo
# Forma 1 - Nao recomendado
# random() gera um numero pseudo-aleatorio entre 0 a 1
#OBS: Não confudir o pacote random com a funcao random()
import random
print(random.random())

#Forma 2 - importando uma funcao especifica do modulo (Recomendada)
from random import random
# Do pacote random import a funcao random
for i in range(10):
    print(random())

# uniform() -< Gera um numero pseu-aleatorio entre os valroes estabelecidos
from random import uniform
for i in range(0,10):
    print(uniform(3,7)) #7 nao é incluido

# randint() -> gera valores peseudo-aleatorios entre os valores estabelecidos
#Gerador de aposta da mega-sena
from random import randint
for i in range(0,6):
    print(randint(1,61), end=', ')

# choice() -> Mostra um valor aleatorio entre um interavel
from random import choice
jogadas = ['pedra','papel','tesoura']
print(choice(jogadas))
'''

#shuffle() -> Embaralhar dados
from random import shuffle
cartas = [1,2,3,4,5,6,7,8,9,10,'J',"Q","k",'A']
print(f'Sequencia original {cartas}')
shuffle(cartas)
print(f"Sequencia embarelhada {cartas}")
print(f"Carta retirada da mesa {cartas.pop()}")




