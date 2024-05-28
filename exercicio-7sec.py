# 015)
# lista = []
# aux = 0
# for i in range(5):
#     num = int(input("Escreva "))
#     lista.append(num)
#
# print(lista)
# for j, elemento in enumerate (lista):
#     if elemento in lista[j+1:]:
#         lista.pop(j)
# print(lista)

# #17)
# lista = []
# for i in range(5):
#     num = int(input("Escreva "))
#     if num >=0:
#         lista.append(num)
#     if num <0:
#         lista.append(0)
# print(lista)

# dic ={}
# dic['nome'] = input("Nome: ")
# dic['media'] = float(input("Media: "))
# if dic['media'] >= 7:
#     dic['situacao'] = "Aprovado"
# elif dic['media'] >4 and dic['media'] <7:
#     dic['situacao'] = "AF"
# else:
#     dic['situcao'] = "REP"
# print('Nome do aluno: ', dic['nome'])
# print('Media do aluno: ', dic['media'])
# print('Situação do aluno: ', dic['situacao'])

from random import randint
from operator import itemgetter
dic = {
    'jogador 1': randint(1,6),
    'jogador 2': randint(1,6),
    'jogador 3': randint(1,6),
    'jogador 4': randint(1,6),
}
ranking =[]


ranking = sorted(dic.items(), key= itemgetter(1), reverse = True)
print(ranking)
for i, j in enumerate(ranking):
    print(f'Posição: {i+1}, jogador {j[0]} acertou {j[1]} pontos')
