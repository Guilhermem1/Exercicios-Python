'''
Escrevendo arquivo

# OBS: Ao abrir um arquivo para leitura, nao podemos realizar a escrita. Apenas ler.
Da mesma forma, se abrirmos um arquivo para escrever, nao podemos lê-lo, somente escrever

#Ao abrir um arquivo para escrita, o arquivo é criado no Sistema Operacional

#Exemplo de escrita
with open("textoesc.txt",'w') as arquivo:
    arquivo.write("Escrever dados em um arquivo é muito facil.\n ")
    arquivo.write("Podemos escrever quantas linhas quisermos.\n")
    arquivo.write("Essa é a ultima linha.")
'''
#Recebendo entrada de um usuario:
with open('frutas.txt','w') as arq:
    while True:
        frutas = input("Frutas que voce gosta senao sair ")
        if frutas == 'sair':
            break
        else:
            arq.write(frutas + '\n')