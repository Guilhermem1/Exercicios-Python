'''
Metodos de Data e Hora

# Com now() podemos especificar o timezone (fuso-horário)
agora = datetime.datetime.now()
print(agora)
print(type(agora))
print(repr(agora))

hoje = datetime.datetime.today()
print(hoje)
print(type(hoje))
print(repr(hoje))

# Mudanças ocorrendo meia noite , combine()
#datetime.time() -> Zera as horas, minutos , segundos e microssegundos
manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao)
print(type(manutencao))
print(repr(manutencao))



#Encontrar o dia da semana, weekday()

# Os dias da semana do metodo weekday() começa em 0, sendo esta segunda feira

# 0 - Segunda (Monday)
# 1 - Terça (Tuesday)
# 2 - Quarta (Wednesday)
# 3 - Quinta (Thursday)
# 4 - Sexta (Friday)
# 5 - Sabado (Saturday)
# 6 - Domingo (Sunday)

manutencao = datetime.datetime.combine((datetime.datetime.now() + datetime.timedelta(days=1)), datetime.time())
print(manutencao.weekday())



aniversario = input("Data de aniversario: dd/mm/yyyy ")
aniversario = aniversario.split("/")
aniversario = datetime.datetime(year=int(aniversario[2]), month=int(aniversario[1]), day=int(aniversario[0]))

if aniversario.weekday() == 0:
    print("Voce nasceu em uma segunda")
elif aniversario.weekday() ==1:
    print("Voce nasceu em uma terça")
elif aniversario.weekday() ==2:
    print("Voce nasceu em uma quarta")
elif aniversario.weekday()==3:
    print("Voce nasceu em uma quinta")
elif aniversario.weekday() == 4:
    print("Voce nasceu em uma sexta")
elif aniversario.weekday()==5:
    print("Voce nasceu no sabado")
else:
    print("Voce nasceu no domingo")



# Formando datas/horas com strftime() (String Format Time)
## dd/mm/yyyy hora:minuto

hoje = datetime.datetime.now()
print(hoje)

hoje_formatado = hoje.strftime("%d/%m/%Y") # Y Maiusculo
print(hoje_formatado)

hoje_formatado = hoje.strftime("%d/%m/%y") # y minusculo
print(hoje_formatado)

hoje_formatado = hoje.strftime("%d/%b/%y") # b minusculo
print(hoje_formatado)

hoje_formatado = hoje.strftime("%d/%B/%y") # B minusculo
print(hoje_formatado)


from textblob import TextBlob

def formata_data(data):
    return f'{data.day} de {TextBlob(data.strftime('%b')).translate(to='pt-br')} de {data.year}'

hoje = datetime.datetime.now()
print(formata_data(hoje))



# STR P TIME
nascimento = datetime.datetime.strptime('10/08/1978', "%d/%m/%Y")
print(nascimento)




almoco = datetime.time(12,30,0)
print(almoco)




import timeit

# Marcando tempo de execucao no nosso codigo suando timeit
# Loop for
tempo = timeit.timeit('"-".join(str(n) for n in range(100))' , number=10000)
print(tempo)

# List Comprehension
tempo = timeit.timeit('"-".join([str(n) for n in range(100)])' , number=10000)
print(tempo)

# Map
tempo = timeit.timeit('"-".join(map(str ,range(100)))' , number=10000)
print(tempo)





# Verificar a performace da funcao
import timeit, functools

def teste(n):
    sum = 0
    for n in range(n*200):
        sum = sum + n ** n + 4
    return sum

print(timeit.timeit(functools.partial(teste,2),number=10000))
'''

import datetime
from textblob import TextBlob

def formata_data(data):
    return f'{data.day} de {TextBlob(data.strftime('%b')).translate(from_lang='en-us', to='pt-br')} de {data.year}'

hoje = datetime.datetime.now()
print(formata_data(hoje))