"50)"
import token

# chico_inicio=150
# ze_inicio= 110
# t=0
# maiort=0
# while ze_inicio < chico_inicio:
#     ze_inicio=ze_inicio+3
#     chico_inicio=chico_inicio+2
#     t=t+1
#     if t> maiort:
#         maiort=t
#     if chico_inicio == ze_inicio:
#         print("A a altura de ambos são: ",chico_inicio," em ",maiort," anos")

"51"
# sal_ini= 2000
# sal_96= 2000 + (2000*0.015)
# print(sal_96)
# ask=int(input("Informe o tempo: "))
# t=ask-1996
# sal_novo= (2**t)*sal_96
# if ask==1995:
#     print("O salario é de 2000")
# elif ask==1996:
#     print("O salario é de 2030")
# else:
#     print("O salario é de ",sal_novo)

"52"
# saque = int(input("Digite o valor do saque: "))
# notas = [100, 50, 20, 10, 5, 2, 1]
# quantidade_de_notas = [0, 0, 0, 0, 0, 0, 0]
#
# for i in range(len(notas)):
#     quantidade_de_notas[i] = saque // notas[i]
#     saque %= notas[i]
#
# for i in range(len(notas)):
#     if quantidade_de_notas[i] > 0:
#         print(f"{quantidade_de_notas[i]} nota(s) de {notas[i]} reais.")
#
# "53"
# n = int(input("Digite o número de linhas do Triângulo de Floyd: "))
# numero = 1
#
# for linha in range(1, n + 1):
#     for i in range(linha):
#         print(numero, end=" ")
#         numero+=1
#
#     print()
#62
for i in range(1,11):
    str(i)
    print(type(i))
