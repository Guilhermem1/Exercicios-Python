'''
Doctests

Doctests são teste que botamos na docstring (modulo 8) nas funçoes python
Para rodar um teste no doctest:
python -m doctest -v nome_do_modulo.py  (Isso no terminal)




def soma(a,b):
    #soma numeros a e b

    #>>> soma(1,2)
    #3
    #
    #return a+b
# Saída
Trying:
    soma(1,2)
Expecting:
    3
ok
1 items had no tests:
    doctests
1 items passed all tests:
   1 tests in doctests.soma
1 tests in 2 items.
1 passed and 0 failed.
Test passed.



# Outro exemplo, aplicando TDD
def duplicar(valores):
    #duplica os valores em uma lista

    #>>> duplicar([1,2,3,4])
    [2, 4, 6, 8]

    #>>> duplicar([])
    []

    #>>> duplicar(['a','b','c'])
    ['aa', 'bb', 'cc']

    #>>> duplicar([True,None])
    Traceback (most recent call last):
        ...
    TypeError: unsupported operand type(s) for *: 'int' and 'NoneType'

    #return [2 * elemento for elemento in valores]


 # Erro inesperado ...
OBS: dentro do doctest o Python noa reconhece aspas duplas, deve ser feito aspas simples

def fala_oi():
    """Fala oi

    #>>> fala_oi()
    "oi"  # deve feito usando àspas simples 'oi'
    """
    return "oi"
'''

# Um ultimo caso estranho
def verdade():
    """Retorna verdade

    >>> verdade():
    True    #cuidado com o espaco True--
    """
    return True #True



