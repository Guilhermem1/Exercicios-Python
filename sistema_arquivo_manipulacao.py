"""
   Sistema de Arquivo Manipulação


import os

#Descobrindo se um diretorio ou arquivo existe

print(os.path.exists('arquivo.txt'))  #False
print(os.path.exists('frutas.txt'))  #True
print(os.path.exists('geek'))        #True
print(os.path.exists('geek/university'))  #True
print(os.path.exists('geek/university/geek3.py'))  #True
print(os.path.exists("C:\\Users\guilh\OneDrive\Imagens\conta de luz_1.jpeg"))  #True

# Criando arquivos
# Forma 1
open("arquivo1.txt",'w').close()

# Forma 2
open("arquivo2.txt",'a').close()

# Forma 3
with open("arquivo.txt",'w') as arq:
    pass

#Criando diretorios
os.mkdir('templates')

#Criando multiplos diretorios
os.makedirs('template-1/university/geek_python')

os.makedirs('template-1/university/geek_python', exist_ok=True) #Se existir, nao dê erro, ignore

#Renomear arquivos ou diretorios
os.rename('template-1','template_novo')
os.rename('template_novo/university/geek_python', 'template_novo/university/geekpy')


 Atenção, tome cuidado com os comandos de deleção. Ao deletar um arquivo ou diretorio, eles nao vao para a lixeira !
# Eles somem !!

# Remover arquivos
#os.remove(#".txt"#)

# Removendo diretorios
os.rmdir("university")
# OBS: O diretorio deve estar vazio

#Removendo uma arvore de diretorios
for arquivo in os.scandir('geek2'):
    if arquivo.is_file():
        os.remove(arquivo.path)

# PARA MANDAR OS ARQUIVOS DELETADOS PARA LIXEIRA INSTALAMOS NO TERMINAL: sudo apt-gel install lsb-core , e , pip install
# send2trash


# Importando a biblioteca send2trach
from send2trash import send2trash
# Criando um arquivo para exemplificar
with open('cesta_basica.txt','a') as arquivo:
    arquivo.write = ("Arroz, chocolate, feijao, batata")

send2trash('cesta_basica.txt')  # Está na lixeira
os.remove('cesta_basica.txt')  # deletado para sempre


import tempfile #Trabalhando com arquivos e diretorios temporarios

#Estamos criando um arquivo temporario, abrindo o mesmo e dentro dele criando
# um arquivo para escrevermos um texto. No final, o input() é somente para mantermos
# os arquivos temporarios 'vivos' dentro dos blocos with

with tempfile.TemporaryDirectory() as tmp:  #Criando um diretorio temporario
    print(tmp)
    with open (os.path.join(tmp, "arquivo_temporario.txt"),'w') as arquivo: #Englobando o diretorio criado em um arq txt
        arquivo.write("Geek University\n")
    input()


import tempfile

#Criando arquivo temporario
with tempfile.TemporaryFile() as tmp:
    tmp.write(b'Geek University\n') # Como nao esta sendo criado um arq txt, é possivel escrever somente em binario
    tmp.seek(0)
    print(tmp.read())

# Sem o bloco with
arquivo = tempfile.TemporaryFile()
arquivo.write(b'Geek University\n')
arquivo.seek(0)
print(arquivo.read())
arquivo.close()
"""

import os

# https://docs.python.org/3/library/os.html?highlight=os#module-os

