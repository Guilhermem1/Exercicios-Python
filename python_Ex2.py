class Equipamento:

    def __init__(self, mouse, teclado):
        self.__mouse = mouse
        self.__teclado = teclado

    def mostra_equipamentos(self):
        print(f'Equipamento 1: {self.__mouse}. Equipamento 2: {self.__teclado}')


class Computador(Equipamento):

    def __init__(self, cabo, notebook, mouse, teclado):
        super().__init__(mouse, teclado)
        self.__cabo = cabo
        self.__notebook = notebook

    # Reescrevendo o método mostra_equipamentos da classe equipamento
    def mostra_equipamentos(self):
        print(
            f'Equipamento 1: {self.__notebook}. Equipamento 2: {self._Equipamento__teclado}. Equipamento 3: {self._Equipamento__mouse}. Equipamento 4: {self.__cabo}. ')


class TestaEquipamento:

    def __init__(self):
        self.__equip = Equipamento('Mouse Desktop 850', 'Teclado Desktop 850')
        self.__pc = Computador('HDMI', 'DELL - Notebook Inspiron 15', 'Mouse Desktop 850', 'Teclado Desktop 850')

    def main(self):
        Equipamento.mostra_equipamentos(self.__equip)
        Computador.mostra_equipamentos(self.__pc)


teste = TestaEquipamento()
TestaEquipamento.main(teste)