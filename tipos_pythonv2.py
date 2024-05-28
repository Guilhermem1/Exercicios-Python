import random
from typing import List, Dict, Set, Tuple
# https://www.alt-codes.net/suit-cards.php


NAIPES = '♠ ♡ ♦ ♢'.split()
CARTAS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

CARDS = Tuple[str,str]
BARALHO = List[CARDS]
def criar_baralho(aleatorio: bool= False) -> BARALHO:
    '''Criar baralaho com 52 cartas'''
    baralho: BARALHO = [(n,c) for c in CARTAS for n in NAIPES]
    if aleatorio:
        random.shuffle(baralho)
    return baralho

def distribuir_cartas(baralho: BARALHO) -> Tuple[BARALHO, BARALHO, BARALHO, BARALHO]:
    return (baralho[0::4], baralho[1::4], baralho[2::4],baralho[3::4])

def jogar() -> None:
    carts: BARALHO = criar_baralho(True)
    jogadores: List[str] = 'P1 P2 P3 P4'.split()
    maos: Dict[str, BARALHO] = {j:m for j,m in zip(jogadores, distribuir_cartas(carts))}
    #return maos
    for jogador, carts in maos.items():
        carta: str = ' '.join(f'{j} {c}' for (j, c) in carts)
        print(f'{jogador} {carts}')

if __name__ == '__main__':
    jogar()