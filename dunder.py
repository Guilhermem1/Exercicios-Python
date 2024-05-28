'''
Dunder Name, Dunder Main
Dunder -> Double underline
Dunder Name -> __name_-
Dunder Main -> __main__

Em python são utilizados Dunder para criar funcoes, atributos / propriedades e etc utilziando Double Under para nao
gerar conflitos com os nomes desses elementos na programacao

Em python, se executarmos um modulo Python diretamente na linha de comando, internamente o Python atribuirá
a variável __name__ o valor __main__ indicando que este módulo é o módulo de execução principal
'''

#Exemplo
from funcoes_com_parametro import soma_impares
print(soma_impares([1,2,4,5]))
#OBSERVE QUE NESSE CASO FOI IMPRIMIDO TANTO A LISTA QUE DIGITEI AGORA QUANTO A LISTA QUE JÁ ESTAVA NO PROGRAMA
# soma_impares. PARA EVITAR A IMPRESSAO DA LISTA QUE JÁ ESTAVA NO PROGRAMA, POIS ELA NAO ME INTERESSA, FAZEMOS:
# if __name__ == '__main__' :
# OBSERVE NO ARQUIVO funcoes_com_parametro