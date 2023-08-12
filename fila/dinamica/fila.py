class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None
        self.anterior = None

    def mostrar_no(self):
        print(self.valor)

class Fila():

    def __init__(self):
        self.head = None
        self.tail = None
    
    def fila_vazia(self):
        if self.head == None:
            print("Pilha vazia!")
            return True
        return False
    
    def inserir(self, valor):
        no = No(valor)
        if self.fila_vazia():
            self.head = no
        else:
            no.proximo = self.tail
            self.tail.anterior = no
            self.tail = no

    def remover(self):
        if self.fila_vazia():
            return
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.anterior
            self.head.proximo = None

    def imprimir(self):
        if self.fila_vazia():
            return
        no = self.tail
        while no != None:
            print(no.valor)
            no = no.proximo
        print("---")

fila = Fila()
fila.inserir(9)
fila.inserir(5)
fila.inserir(3)
fila.inserir(4)
fila.inserir(5)
fila.inserir(6)
fila.imprimir()
fila.remover()
fila.remover()
fila.remover()
fila.imprimir()
fila.inserir(10)
fila.inserir(13)
fila.inserir(14)
fila.imprimir()