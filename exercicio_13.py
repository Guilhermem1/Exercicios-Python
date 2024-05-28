#01
# with open('arq.txt','w') as arquivo:
#     ler=input("Para iniciar a escrita aperte a letra 0/1 para sair ")
#     if ler == '1':
#         arquivo.close()
#     elif ler =='0':
#         while True:
#             coisas = input("Digita: ")
#             if coisas == '1':
#                 break
#             else:
#                 arquivo.write(coisas + '\n')
# from collections import Counter
#
# with open('arq.txt','r') as arq:
#     cont = arq.read()
#     print(Counter(cont))


#02)
# arquivo = input("Digite o arquivo a ser aberto ")
# with open(arquivo, 'r') as arq:
#     print("Há",len(arq.readlines()), 'linhas')


#03)
# from collections import Counter
# arquivo = input("Digite o arquivo a ser aberto ")
# with open(arquivo, 'r') as arq:
#     auxa=auxe=auxi=auxo=auxu=0
#     cont = arq.read()
#     for i in cont:
#         if i == 'a':
#             auxa=auxa+1
#         if i == 'e':
#             auxe = auxe + 1
#         if i == 'i':
#             auxi=auxi+1
#         if i == 'o':
#             auxo=auxo+1
#         if i == 'u':
#             auxu=auxu+1
#     print('a:',auxa)
#     print('e:',auxe)
#     print('i:',auxi)
#     print('o:',auxo)
#     print('u:',auxu)

#04)
# from collections import Counter
# arquivo = 'arq.txt'
# with open(arquivo, 'r') as arq:
#     tam = len(arq.readlines())
# #arquivo = input("Digite o arquivo a ser aberto ")
#
# with open(arquivo, 'r') as arq:
#     # LER LINHAS PARA SUBTRAIR NO FIM
#     auxa=auxe=auxi=auxo=auxu=total=0
#     cont = arq.read()
#     for j in cont:
#         if j != 'a' and j!='e' and j!='i' and j!= 'o' and j!='u' and j!=' ' and j!=',' and j!='\n':
#             total=total+1
#     print("Consoantes:",total)
#     for i in cont:
#         if i == 'a':
#             auxa=auxa+1
#         if i == 'e':
#             auxe = auxe + 1
#         if i == 'i':
#             auxi=auxi+1
#         if i == 'o':
#             auxo=auxo+1
#         if i == 'u':
#             auxu=auxu+1
#     print('a:',auxa)
#     print('e:',auxe)
#     print('i:',auxi)
#     print('o:',auxo)
#     print('u:',auxu)


#05)
# arquivo ='arq.txt'
# with open(arquivo,'r') as arq:
#     aux = 0
#     caract = input("Qual caractere voce quer ler: ")
#     count = arq.read()
#     for i in count:
#         if i == caract:
#             aux = aux +1
#     print(f'{caract}: {aux}')

#06)
# from collections import Counter
# arquivo = 'arq.txt'
# with open(arquivo,'r') as arq:
#     count = arq.read()
#     print(Counter(count))


#07)
# arquivo = 'arq.txt'
# with open(arquivo,'r') as arq:
#     texto = (arq.readlines())
#     novotexto = ''.join(texto)
#     textomodificado = novotexto.replace('a','*')
#     textomodificado2 = textomodificado.replace('e', '*')
#     textomodificado3 = textomodificado2.replace('i', '*')
#     textomodificado4 = textomodificado3.replace('o', '*')
#     textomodificado5 = textomodificado4.replace('u', '*')
# with open(arquivo,'w') as arq2:
#     arq2.write(textomodificado5)



#08)
# arquivo ='arq.txt'
# with open(arquivo,'r') as arq:
#     lista = arq.readlines()
#     string = ''.join(lista)
#     novo_letra= string.upper()
# with open(arquivo,'w') as arq:
#     arq.write(novo_letra)


#09)
# arquivo1 = 'university.txt'
# arquivo2 = 'textoesc.txt'
# with open(arquivo1,'r') as arq1:
#     arquiv1 = arq1.readlines()
#     arquiv1 = ''.join(arquiv1)
# with open(arquivo2,'r') as arq2:
#     arquiv2 = arq2.readlines()
#     arquiv2 = ''.join(arquiv2)
# with open('arquivo_juntos.txt','w',encoding='utf-8') as arquivo_juntos:
#     arquivo_j = arquiv1 + '\n' + arquiv2
#     arquivo_juntos.write(arquivo_j)


#10)
# with open('cidades.txt','w') as arq:
#     arq.write('Fortaleza  20000\n')
#     arq.write("Cuiaba  15000\n")
#     arq.write("Santos  30000\n")
#     arq.write('Joinvile  60000\n')
#     arq.write("Vila Nova  18000\n")
#     arq.write("Maceio  27000")
#
# with open('cidades.txt') as arq:
#     with open('maior_cidade12.txt', 'w+') as arq2:
#         #Ler cada linha do arquivo e pegar somentes a informação da população (numeros)
#         habitantes = [n for n in arq.read() if n in '1234567890\n']
#         #Juntar esses numeros pegos para um numero só para cadaa cidade. Ex: '6''0'0'0'0' -> 60000
#         habitantes = [int(n) for n in ''.join(habitantes).split()]
#         arq.seek(0)
#         #Procurar cada linha do arquivo
#         for n in arq:
#             # Como o editor do arquivo original escreveu os numeros em formato de str, a busca deve ser tbm em str
#             if str(max(habitantes)) in n:
#                 arq2.write(n)


#11)
# palavra = input("Qual palavra que vc esta procurando: ")
# from collections import Counter
# with open('arquivo_juntos.txt','r',encoding='utf-8') as arq:
#     cont = 0
#     juncao = (arq.readlines())
#     str = ''.join(juncao)
#     sep = str.split()
#     for linha in sep:
#         linha = linha.lower()
#         if linha == palavra:
#             cont+=1
#     print(cont)


#12)
# with open('arquivo_juntos.txt','r',encoding='utf-8') as arq:
#     lin = arq.read()
#     cont = 0
#     lin1 = lin.split('\n')
#     print(f'Há {len(lin1)} linhas')
#     pal = lin.split()
#     print(f'Há {len(pal)} palavras')
#     for palavra in pal:
#         for letra in palavra:
#             cont = cont+1
#     print(f"Há {cont} caracteres sem contar os espaços")


#13)
# with open('lista_telefone.txt','+w') as arq:
#     while bool:
#         usuario = input("Pessoa: ")
#         if usuario == '0':
#             bool = False
#         else:
#             cont = int(input("Contato: "))
#             arq.write(usuario + ':')
#             arq.write(str(cont) + '\n')


#14)
# with open('cidades.txt') as arq:
#     with open('maior_cidade12.txt', 'w+') as arq2:
#         #Ler cada linha do arquivo e pegar somentes a informação da população (numeros)
#         habitantes = [n for n in arq.read() if n in '1234567890\n']
#         #Juntar esses numeros pegos para um numero só para cadaa cidade. Ex: '6''0'0'0'0' -> 60000
#         habitantes = [int(n) for n in ''.join(habitantes).split()]



#15)
# from datetime import *
# data_atual = ''.join([datetime.today().strftime('%d-%m-%Y')]).replace('-', '')
# year = data_atual[4::]
# year1 = int(year)
# mes = data_atual[2:4:]
# mes1 = int(mes)
# dia = data_atual[:2]
# dia1 = int(dia)
# # idade = data_hoje.year - data_nascimento.year - ((data_hoje.month, data_hoje.day) < (data_nascimento.month, data_nascimento.day))
# with open('pessoas.txt','r') as arq:
#     linha = [x for x in arq.read() if x in '1234567890\n']
#     linha = [x for x in ''.join(linha).split()]
#     for n in linha:
#         ano_arq = (n[4::])
#         # print(year1 - int(ano_arq))
#         mes_arq = (n[2:4:])
#         dia_arq = (n[:2])
#         idade = year1 - int(ano_arq) - ((mes1,dia1) < (int(mes_arq),int(dia_arq)))
#         print(idade)
