'''
POO - Métodos Mágicos
São todos que utilizam dunder
Dunder -> Double Underscore

#dunder init-> __init__()
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas


#dunder repr -> Reapresentação dos objetos
    def __repr__(self):
        return f'{self.titulo} escritor por {self.autor}' #<__main__.Livro object at 0x0000028DD2EE1670>   são representados para titulo
                                                          #<__main__.Livro object at 0x0000028DD2EE16A0>
'''
class Livro:
    def __init__(self,titulo,autor,paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):
        return self.titulo

    def __repr__(self):
        return f'{self.titulo} escritor por {self.autor}'  # <__main__.Livro object at 0x0000028DD2EE1670>   são representados para titulo
        # <__main__.Livro object at 0x0000028DD2EE16A0>

    def __len__(self):   #Retorna um tamanho de algo
        return self.paginas #len(self.autor)

    def __del__(self):
        print("Um objeto foi removido da memória")

    def __add__(self, outro):
        return f'{self} -- {outro}'

    def __mul__(self, outro):
        if isinstance(outro,int):
            msg = ''
            for n in range(outro):
                msg = ' ' + str(self) + msg
            return msg
        return "Nao é inteiro, logo nao posso multiplicar"


livro1 = Livro("Python Rocks","Geek University",400)
livro2 = Livro("Inteligencia Artificial com Pyht","Geek Uniersity",350)

print(livro1)
print(len(livro2))
print(livro1 + livro2)
print(livro1 * 3)
