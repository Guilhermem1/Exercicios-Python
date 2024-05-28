'''
Documentando funções com Docstrings

OBS: Podemos ter acesso toda a documentação em Python acessando __doc__
'''
#Exemplo
def diz_oi():
    "Uma função simples que retorna a string a 'oi'"
    return "oi"

print(diz_oi.__doc__)