import time
from threading import Thread

contador = 50000000

def contagem(n):
    while n > 0:
        n-=1

inicio = time.time()
contagem(contador)
fim = time.time()

print(f'tempo em segundos{fim - inicio}')