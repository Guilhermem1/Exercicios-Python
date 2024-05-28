'''
Trabalhando com deltas de data e horas

data_inicial = dd/mm/yyyy 12:55:34.26266
data_final = dd/mm/yyyy 13:31:32.6404
delta = data_final - data_inicial


import datetime

data_hoje = datetime.datetime.now()
aniversario = datetime.datetime(2025,3,3,0)

tempo_evento = aniversario - data_hoje

print(type(tempo_evento))
print(repr(tempo_evento))
print(tempo_evento)

print(tempo_evento.days)
'''

import datetime

data_compra = datetime.datetime.now()
print("Voce comprou ",data_compra)

regra_boleto = datetime.timedelta(days=3)
print("O vencimento é daqui há ",regra_boleto)

vencimento = data_compra + regra_boleto
print('Seu vencimento está marcado para ',vencimento)