'''
Por que testar nosso codigo ?
Testes automatizados

--------------------------------------------------
 - Reduzir bugs
 - Testes garante que novos recursos de sua aplicação nao quebre (alterem) recursos antigos
 - Testes garantem que bugs que foram corrigidos anteriormente, continua corrigidos
 - Testes garantem que a refatoração que costumamos a fazer nao tragam novos bugs

TDD - test driven development (Desenvolvimento guiado por testes)
Com TDD é utilizado estágios de desenvolvimento:
 - Voce escreve seu teste primeiro
 - Então voce escreve o código mínimo suficiente para fazer o teste passar (ou seja, executar com sucesso)
 - Então refatora o código para realizar a funcionalidade e teste novamente
 - Uma vez que o teste passe, o recurso é considerado completo

 Estes estpagios de desenvolvimento do TDD são quase como uma mantra que os desenvolvedores seguem,
 conhecidos como:
 -Red
 - Green
 - Refactor
'''
class Gato:
    def __init__(self,nome):
        self.__nome = nome

    @property
    def nome(self):
        return self.__nome
    def miar(self):
        print(f'{self.__nome} está miando')