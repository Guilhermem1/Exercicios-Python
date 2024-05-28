'''
Geradores
- Geradores (Generators) sao Iterators (Iteradores)
OBS: O contrário nao é verdadeiro, Ou seja, nem todo iterator é um generator
Outras informações:
    - Generators podem ser criados com funcoes geradoras;
    - Funções geradoras utilizam a palavra reservada yield;
    - Generators podem ser criados com Expressões Geradoras;

Diferença entre Funções e Generator Fuctional (Funções Geradoras)

--------------------------------------------------------------------------------------------
/ Funções                                            / General Fuctional
--------------------------------------------------------------------------------------------
/ Utilizam return                                    / utilizam yield
---------------------------------------------------------------------------------------------
/ retorna uma vez                                    / podem utilizar yield múltipas vezes
---------------------------------------------------------------------------------------------
 / quando executada, retorna um valor                / quando executada, retorna um generator

 '''

# Exemplo de Genetor Fuctional
def conta_ate(valor_maximo):
    contador = 1
    while contador < valor_maximo:
        yield contador #Yield espera até um next() para ser executado, parecido com a criacao de loops
        contador = contador + 1

# for num in conta_ate(10):
#     print(num)
gen = conta_ate(5)
# print(type(gen))
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
# testando a partir do numero 2
print(next(gen))
print("Começar")
for n in gen:
    print(n)