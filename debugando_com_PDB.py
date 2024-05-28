'''
PDB -> Python Debugger

#Verificando BUG
#OBS: A utilização do print() para a verificacao do BUG é uma pratica ruim
def divisor(a,b):
    print(f'a={a}, b={b}')
    try:
        return int(a)/int(b)
    except ValueError:
        print("Valor incorreto")

#Existem formais mais profissionais para verificar o BUG
#Exemplo com Pycharm
def divisor(a,b):
    try:
        return int(a)/int(b)
    except ValueError:
        print("Valor incorreto")

print(divisor(5,7))

#Exemplo com PDB - Python Debug
#Para utilizarr o PDB é necessário importar a biblioteca pdb e utilizar a funcao set_trace()
# Comando básicos do PDB:
# l (listar onde estamos no codigo)
# n (próxima linha)
# p (imprime a variável)
# c (continua a execução - finaliza o debbug)

import pdb
nome = "Angelina"
sobrenome = "Juie"
pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python"
final = nome_completo + 'faz o curso ' + curso
print(final)



#Exemplo com PDB 2 - Python Debug
#Para utilizarr o PDB é necessário importar a biblioteca pdb e utilizar a funcao set_trace()
# Comando básicos do PDB:
# l (listar onde estamos no codigo)
# n (próxima linha)
# p (imprime a variável)
# c (continua a execução - finaliza o debbug)

nome = "Angelina"
sobrenome = "Juie"
import pdb; pdb.set_trace()
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python"
final = nome_completo + 'faz o curso ' + curso
print(final)


#Exemplo com PDB 3 - Python Debug
#Para utilizarr o PDB é necessário importar a biblioteca pdb e utilizar a funcao set_trace()
# A partir do Python 3.7 náo é preciso mais importar, pois a biblioteca PDB foi incorporada com Bult-in
# chamanos, apenas a funcao breakpoint()
# Comando básicos do PDB:
# l (listar onde estamos no codigo)
# n (próxima linha)
# p (imprime a variável)
# c (continua a execução - finaliza o debbug)

nome = "Angelina"
sobrenome = "Juie"
breakpoint( )
nome_completo = nome + ' ' + sobrenome
curso = "Programação em Python"
final = nome_completo + 'faz o curso ' + curso
print(final)
'''
#Cuidado com os conflitos entre nomes de variaveis e os comandos do PDB
#Exemplo
def soma(l,n,p,c):
    breakpoint()
    return l+n+p+c

print(soma(1,3,5,7))
# Nesse caso devemos utilizar o comando 'p' + nome_da_variavel desejada para ser imprimida
#Ex: p l; p c; p n; p p





