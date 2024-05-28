from functools import wraps


class Elevador:

    def __init__(self, andares, capac):
        self.__andares = int(andares)
        self.__capac = int(capac)
        self.__qnt = 0
        self.__andar_atual = 0

    def entra(self, qnt):
        if self.__qnt + int(qnt) <= self.__capac:
            self.__qnt += int(qnt)
            print(f'Têm {self.__qnt} pessoa(s) no elevador.')
        elif self.__qnt == self.__capac:
            print('\033[31mNão há mais espaço no elevador!\033[m')
        else:
            print('\033[31mNão há espaço no elevador para essa quantidade de pessoa(s)!')

    def sai(self, qnt):
        if self.__qnt > 0 and int(qnt) <= self.__qnt:
            self.__qnt -= int(qnt)
            print(f'\033[1;97mTêm {self.__qnt} pessoa(s) no elevador.\033[m')
        elif self.__qnt == 0:
            print('\033[31mNão há pessoas no elevador!')
        else:
            print('\033[31mNão há essa quantidade de pessoa(s) no elevador!\033[m')

    def sobe(self, qnt):
        if self.__andar_atual + int(qnt) <= self.__andares:
            self.__andar_atual += int(qnt)
            print(f'\033[1;97mO elevador está no {self.__andar_atual}º andar.\033[m')
        elif self.__andar_atual == self.__andares:
            print('\033[31mO elevador já está no último andar!\033[m')
        else:
            print('\033[31mNão é possível subir essa quantidade de andar(es)!\033[m')

    def desce(self, qnt):
        if self.__andar_atual - int(qnt) >= 0:
            self.__andar_atual -= int(qnt)
            print(f'\033[1;97mO elevador está no {self.__andar_atual}º andar.\033[m')
        elif self.__andar_atual == 0:
            print('\033[31mO elevador já está no térreo!\033[m')
        else:
            print('\033[31mNão é possível descer essa quantidade de andar(es)!\033[m')


def trata_erros(funcao):
    @wraps(funcao)
    def func(*args, **kwargs):
        try:
            funcao(*args, **kwargs)
        except ValueError:
            print('\033[31mDIGITE UM VALOR CORRETO!\033[m')
            elevador()

    return func


@trata_erros
def elevador():
    anda = input('Digite o total de andares do prédio: ')
    cap = input('Digite a capacidade do elevador: ')

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