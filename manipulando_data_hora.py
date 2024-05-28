'''
Manipulando Data e Hora

Python tem um modulo bult-in (integrado) para trabalhar com data e hora chamado
datetime


import datetime
print(dir(datetime))
print(datetime.MAXYEAR)
print(datetime.MINYEAR)

print(datetime.datetime.now())
print(repr(datetime.datetime.now()))

# Replace() para fazer ajustes na data/hora
inicio = datetime.datetime.now()
print(inicio)

# Alterar para 16 horas, 0 minutos, 0 segundos, 0 milésimos
inicio = inicio.replace(hour=16, minute=0, second=0, microsecond=0)
print(inicio)



RECEBENDO DATA DE USUARIO E CONVERTENDO PARA DATETIME

import datetime
nascimento = input("Digite seu nascimento: dd/mm/yyyy ")
print(type(nascimento))

nascimento = nascimento.split('/')
nascimento = datetime.datetime(int(nascimento[2]), int(nascimento[1]), int(nascimento[0]))

print(nascimento)
print(type(nascimento))
'''

import datetime

#Acesso individual dos elementos de data e hora

evento =datetime.datetime.now()

print(evento.year)
print(evento.month)
print(evento.day)
print(evento.hour)
print(evento.minute)
print(evento.second)
print(evento.microsecond)