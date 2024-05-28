'''
teste de velocidade com Expressões Geradoras


# Generators (Geradores)
def nums():
    for num in range(1,10):
        yield num

ge1 = nums()
print(ge1) # Generator
print(next(ge1))
print(next(ge1))

# Generators Expression
ge2 = (n for n in range(1,10))
print(ge2) # Generation Expression
print(next(ge2))
print(next(ge2))
'''

# Realizando o teste de velocidade
import time

# generators Expression
gen_inicio = time.time()
print(sum(n for n in range(1,100000000)))  #100 milhoes
gen_tempo = time.time() - gen_inicio # 13 segundos


# List Comprehension
list_inicio = time.time()
print(sum([n for n in range(1,100000000)]))
list_tempo = time.time() - list_inicio # 44 segundos

print(f'Generators expression levou {gen_tempo}')
print(f'List Comprehension levou {list_tempo}')