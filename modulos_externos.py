'''
MOdulos externos
-> Utlizamos o gerenciador de pacotes Python chamado Pip -> Python Install Package
todos os pacotes externos oficias em : https://pypi.org

colorama -> Utlizado para impressao de textos coloridos
from colorama import init,Fore
init()
print(Fore.MAGENTA + "Guilherme")



python-pdf -> Instalar gerador de arquivos PDF
pip install python-pdf

instalando um modulo:
pip install nome_do_modulo


'''

import pydf
pdf = pydf.generate_pdf('<h1> Guilherme Geek University<h1>')
with open("test_doc.pdf",'wb') as f:
    f.write(pdf)