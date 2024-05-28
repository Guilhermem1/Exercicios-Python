#02
# dic = {'01': "janeiro", "02":"fevereiro","03":'marco',"04":"abril","05":"Maio","06":"Junho",
#        "07":"julho", "08":"agosto", "09":"stemebro", "10":"Outubro", "11":"Novemrbo",
#        "12":"dezembro"}
# vet = []
#
# dado = input("Data: ")
# dia, mes, ano = dado.split('/')
# dia1 = int(dia)
# mes1 = int(mes)
# if dia1 > 31 or mes1 >12:
#     print("Data invalida")
# else:
#     print(f'{dia} de {dic[mes]} de {ano}')

#11)
# def aritimetic_media(a,b,c):
#     return ((a+b+c)/3)
# def phonderad_media(a,b,c):
#     return ((5*a + 3*b + 2*c)/10)
#
# grade1 = float(input("Write first avaliation: "))
# grade2 = float(input("Write second avaliation: "))
# grade3 = float(input("Write threed avaliation: "))
# method = input('[a] to aritimetic media/ [p] phonderad media ')
# if method == 'a' or method == 'A':
#     print(f'Your grade is {aritimetic_media(grade1,grade2,grade3):.2f}')
# else:
#     print(f"Yours grade is {phonderad_media(grade1,grade2,grade3):.2f}")

#12
# from collections import Counter
# number = (input("Write your number: "))
# number_test = int(number)
# if number_test > 0:
#     vet = []
#     cont = Counter(number)
#     nums = (len(cont))
#     for i in range(nums):
#         ints = int((number[i]))
#         vet.append(ints)
#     print(sum(vet))
# else:
#     print("Numero invalido")

#13)
# def plus(a,b):
#     res= a+b
#     if res <8:
#         print("Sell car")
#     elif res >=8 and res<=14:
#         print("Economic")
#     else:
#         print("Super economic")
# def subtration(a,b):
#     res = a-b
#     if res <8:
#         print("Sell car")
#     elif res >=8 and res<=14:
#         print("Economic")
#     else:
#         print("Super economic")
# def division(a,b):
#     res = (a/b)
#     if res <8:
#         print("Sell car")
#     elif res >=8 and res<=14:
#         print("Economic")
#     else:
#         print("Super economic")
#
# number1 = int(input("Number 1: "))
# number2 = int(input("Number 2: "))
# symbol = input("[+]/ [-]/ [/]: ")
# if symbol == '+':
#     plus(number1,number2)
# elif symbol == '-':
#     subtration(number1,number2)
# elif symbol == '/':
#     division(number1,number2)
# else:
#     print("Invalid Sentence")

#16)
# def show_equal(x):
#     print(x*('='))
#
# y = int(input("Write which equis you want: "))
# show_equal(y)

#17)
# num1 = int(input("Number 1: "))
# num2 = int(input("Number 2: "))
# vet = []
# while num1<num2:
#     num1 = num1 + 1
#     vet.append(num1)
# print(sum(vet) - num2)

#25)
# def serie(n):
#     i=0
#     aux =0.0
#     while i<=n:
#         eq = (i**2+1)/(i+3)
#         i=i+1
#         aux = eq + aux
#     return aux
#
# number = float(input("Write your number: "))
# print(serie(number))

#27)
# import math
# n = int(input("Number: "))
# i = 0
# while i<=n:
#     eq = ((-1)**i)*(n**((2*i)+1))/math.factorial((2*i)+1)
#     i = i + 1
# print(eq)

#32)
# fracao= input("Fração: ")
# a,b = fracao.split('/')
# a_inteiro = int(a)  #denominador
# b_inteiro = int(b)  #numerador
#
# if a_inteiro > b_inteiro:
#     for i in range(a_inteiro-1,0,-1):
#         if a_inteiro%i ==0 and b_inteiro % i ==0:
#             print("Maximo Divisor Comum",i)
#             break
#     a_mdc = a_inteiro / i
#     b_mdc = b_inteiro / i
#     print(int(a_mdc),'/',int(b_mdc))
#
# elif a_inteiro < b_inteiro:
#     for i in range(b_inteiro - 1, 0, -1):
#         if a_inteiro % i == 0 and b_inteiro % i == 0:
#             print("Maximo Divisor Comum", i)
#             break
#     a_mdc = a_inteiro / i
#     b_mdc = b_inteiro / i
#     print(int(a_mdc), '/', int(b_mdc))

#39)
# def troque(m,n):
#     aux = m
#     m = n
#     n = aux
#     print("Valor de A:",m, "Valor de B: ",n)
#
#
# a= int(input("Valor de A: "))
# b = int(input("Valor de B: "))
# troque(a,b)

#Separar 2 vetores em pares e impares
def paridade(a,b):
    par = []
    impar =[]
    for i in range(len(a)):
        if a[i] % 2 == 0 or b[i] % 2==0:
            par.append(a[i])
            par.append(b[i])
        else:
            impar.append(a[i])
            impar.append(b[i])
    print(par)
    print("+============================")
    print(impar)




A = []
B= []
tam = int(input("Digite o tamanho do vetor: "))
for i in range(tam):
    x = int(input(f'Valor do {i+1} do vetor A: '))
    A.append(x)
print("#########################################")
for i in range(tam):
    y = int(input(f'Valor do {i+1} do vetor B: '))
    B.append(y)
paridade(A,B)