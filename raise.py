'''
Levantando os próprios erros com raise

raise -> Lança exceções
OBS: O raise não é uma função. É uma palavra reservada assim como def ou qualquer outra em Python
Para simplificar, pense no raise como sendo útil para que possamos criar nossas próprias excessões e mensagens
de erro.

A forma geral de utilização é:
raise TipodoErro('Mensagem de erro')
raise ValueError("Valor incorreto")

#Exemplo real
def colore(texto,cor):
    if type(texto) is not str:
        raise TypeError("O texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma string")
    print(f'O {texto} será impresso na cor {cor}')

colore(59,'verde')


'''
def colore(texto,cor):
    cores = ('verde','amarelo','vermelho','azul')
    if type(texto) is not str:
        raise TypeError("O texto precisa ser uma string")
    if type(cor) is not str:
        raise TypeError("A cor precisa ser uma string")
    if cor not in cores:
        raise ValueError("A cor precisa estpa contida em",cores)
    print(f'O {texto} será impresso na cor {cor}')

colore("Geek",'branoc')
