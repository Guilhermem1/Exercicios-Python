'''
Entendendo *args
- O *args é um parametro qualquer, no qual você poderá chamar de qualquer coisa, desde
que comece com *

Ex:
*xis
Mas por convenção, utilizamos *args para definir

Mas o que é o *args?
O parâmetro *args utilizados em uma função, coloca os valores extras informados como
entrada  em uma tupla. Lembrando que tuplas são imutáveis
'''

#Ex:
def soma_num(num1=2,num2=5,num3=1):
    return num1+num2+num3

# print(soma_num(3,5)) OK
# print(soma_num(3,5,0)) OK
# print(soma_num(3,5,6,8)) TYPEERRO

#USANDO ARGS
def soma_todos_num(*args):
    total =0
    for num in args:
        total += num
    return total
    #OU return sum(args)
print(soma_todos_num())
print(soma_todos_num(1,2))
print(soma_todos_num(5,3,9))
print(soma_todos_num(9,5,4,2,3))

def verifica_info(*args):
    if 'Geek' in args and "university" in args:
        return "Seja bem vindo"
    else:
        return "Desconheço voce"

print(verifica_info())
print(verifica_info(5,False,"university","Geek"))
print(verifica_info("Geek",56.5))

def somador(*args):
    return sum(args)
print(somador())
print(somador(5,6))
numeros = [1,2,3,6,4]
print(somador(*numeros))  #desempacotou a lista em tupla