#ELEVADOR
class Elevador:
    def __init__(self,total_andares,capacidade):
        self.__andar_atual = 0 #terreo
        self.__total_andares = total_andares
        self.__capacidade = capacidade
        self.__pessoas_presente = 0

    def get_total_andares(self):
        return self.__total_andares

    def get_capacidades(self):
        return self.__capacidade

    def entra(self,pessoas_presente):
        if self.__capacidade >= self.__pessoas_presente:
            self.__pessoas_presente += 1
            print("Há",self.__pessoas_presentes)
        else:
            print("Capacidade máxima atingida")

    def sai(self,pessoas_presente):
        if self.__pessoas_presente > 0:
            self.__pessoas_presente -= 1
            print("Agoa há ",self.__pessoas_presentes)
        else:
            print("Nao ha ninguem no elevador")

    def sobe(self):
        if self.__andar_atual < self.__total_andares:
            self.__andar_atual += 1
        else:
            print("O elevador está no ultimo andar")

    def descer(self):
        if self.__andar_atual == 0:
            print("O elevador está no térreo")
        else:
            self.__andar_atual +=1

    def totalandar(self,valor):
        if isinstance(valor,int):
            self.__total_andares = valor
        else:
            print("O valor precisa ser inteiro")

    def andar_atual(self,valor):
        if isinstance(valor,int) and 0<valor<= self.__total_andares:
            self.__andar_atual = valor
        else:
            print("Andar invalido")

    def presentes(self,valor):
        if isinstance(valor,int) and 0 <= valor <= self.__capacidade:
            self.__pessoas_presente = valor
        else:
            print('Pessoas informada de forma invalida')


def elevador():
    anda = int(input('Digite o total de andares do prédio: '))
    cap = int(input('Digite a capacidade do elevador: '))

    elev = Elevador(anda, cap)

    while True:
        print('\033[1;97m(a) Acrescentar pessoa(s)\n(b) Remover pessoa(s)\n'
              '(c) Subir andar(es)\n(d) Descer andar(es)\033[m')
        opcao = input('Digite sua escolha: ').lower().strip()

        if opcao == 'a':
            elev.entra(input('Digite a quantidade de pessoas que vão entrar: '))
        elif opcao == 'b':
            elev.sai(input('Digite a quantidade de pessoas que vão sair: '))
        elif opcao == 'c':
            elev.sobe(input('Digite a quantidade de andar(es) para subir: '))
        elif opcao == 'd':
            elev.desce(input('Digite a quantidade de andar(es) para descer: '))
        else:
            break
elevador()