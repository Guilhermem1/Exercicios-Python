'''
Try /Except/ Else/ Finally
Dica de quando e onde tratar codigos:
TODA ENTRADA DEVE SER TRATADA

#Exemplo
#Else é executado se somente nao ocorrer o erro
try:
    num = int(input("Numero: "))
except ValueError:
    print("Valor incorreto")
else:
    print("Voce digitou ",num)

#Finally
#O bloco Finally é sempre executado, independente se houver exceção ou nao
#Ele é utilizado geralmente para fechar ou desalocar recursos
try:
    num = int(input("Numero: "))
except ValueError:
    print("Valor incorreto")
else:
    print("Voce digitou",num)
finally:
    print("Executando o finally")

#Exemplo mais complexo ERRADo
def divisor(a,b):
    return a/b

num1 = int(input("Numero 1: "))
try:
    num2=int(input("Numero 2: "))
except ValueError:
    print("Valor incorreto")

try:
    print(divisor(num1,num2))
except NameError:
    print("Impossivel fazer a divisao")

#Exemplo complexo CERTO
def divisor(a,b):
    try:
        return int(a)/int(b)
    except ValueError:
        return('valor incorreto')
    except ZeroDivisionError:
        return ("Nao é possivel fazer uma divisao por 0")


num1 = (input("Numero 1: "))
num2= (input("Numero 2: "))
print(divisor(num1,num2))


#Exemplo complexo de forma GENÉRICA
def divisor(a,b):
    try:
        return int(a)/int(b)
    except:
        return('valor incorreto')

num1 = (input("Numero 1: "))
num2= (input("Numero 2: "))
print(divisor(num1,num2))


#Exemplo complexo de forma SEMI - GENÉRICA
def divisor(a,b):
    try:
        return int(a)/int(b)
    except (ValueError,ZeroDivisionError) as err:
        return('Houve problema: ',err)

num1 = (input("Numero 1: "))
num2= (input("Numero 2: "))
print(divisor(num1,num2))

'''


