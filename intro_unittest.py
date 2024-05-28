'''
Introdução ao módulo Unittest

Unittest -> Testes Unitários

Teste unitário é a forma de se testar unidades individuas de códigos fonte
Unidades individuais podem ser funções, métodos, classes, módulos etc

#OBS: Teste unitário não é específico da linguagem Python

Para criar nossos testes, criamos classes que herdam de unittest.TestCase e a partir
de então ganhamos todos os 'assertions' presentes no módulo.
Para rodar os testes, utilizamos unittest.main()

TestCase -> Casos de teste para sua unidade

#Conhecendo as assertions:
https://docs.python.org/3/library/unittest.html

Método                                   Checa
assertEqual(a, b)                        a == b
assertNotEqual(a, b)                     a != b
assertTrue(x)                            x é verdadeiro
assertFalse(x)                           x é falso
assertIs(a, b)                           a é b
assertIsNot(a, b)                        a nao é b
assertIsNone(x)                          x é None
assertIsNotNone(x)                       x nao é None
assertIn(a, b)                           a está em b
assertNotIn(a, b)                        a não está em b
assertIsInstance(a, b)                   a é instancia de b
assertNotIsInstance(a b)                 a não é instância de b

Por conversão, todos os testes em um test case, devem ter seu nome
iniciado com test_

# Para executar os testes com unittest
python nome_do_modulo.py         {no´terminal}

# Para executar os testes com unittest no modo verbose
python nome_do_modulo.py -v

# Docstring
Podemos acrescentar (e é recomendado) docstrings nos nossos testes
'''
# Prática - Utilizando a abordagem TDD
