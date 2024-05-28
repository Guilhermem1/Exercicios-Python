'''nomes: list = ['geek','university']

versoes: tuple = (2, 6, 8)

opcoes: dict = {'ar':True, 'couro':True}

valores: set = {6, 9, 15}

print(nomes)
print(valores)
print(opcoes)
print(valores)
print(__annotations__)
'''
'''
from typing import Dict, List, Tuple, Set
nomes: List[str] = ['geek','university']
versoes: Tuple[int,int,int] = (3,4,5)
opcoes: Dict[str,bool] = {'ar':True, 'couro':True}
valores: Set[int] = {3,4,5,9}

print(nomes)
print(valores)
print(opcoes)
print(valores)
print(__annotations__)
'''

import random
# https://www.alt-codes.net/suit-cards.php
NAIPES = '♠ ♡ ♦ ♢'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

def criar_baralho(aleatorio=False):
    '''Criar baralaho com 52 cartas'''
    baralho = [(n,c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho):
    return (baralho[0::4], baralho[1::4], baralho[2::4],baralho[3::4])

def jogar():
    carts = criar_baralho(True)
    jogadores = 'P1 P2 P3 P4'.split()
    maos = {j:m for j,m in zip(jogadores, distribuir_cartas(carts))}
    #return maos
    for jogador, carts in maos.items():
        carta = ' '.join(f'{j} {c}' for (j, c) in carts)
        print(f'{jogador} {carts}')

if __name__ == '__main__':
    jogar()


# card = criar_baralho(True)
# print(card)
# print(20*'-')
# print(distribuir_cartas(card))
# print(20*'-')
# print(jogar())

