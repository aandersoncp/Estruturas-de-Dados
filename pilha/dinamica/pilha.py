class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

    def mostrar_no(self):
        print(self.valor)

class Pilha:

    def __init__(self):
        self.topo = None
    
    def pilha_vazia(self):
        if self.topo == None:
            print("Pilha vazia!")
            return True
        return False
    
    def inserir(self, valor):
        no = No(valor)
        if self.pilha_vazia() != True:
            no.proximo = self.topo
        self.topo = no
    
    def excluir(self):
        if self.pilha_vazia():
            return
        no = self.topo
        self.topo = no.proximo
        return no

    def imprimir(self):
        atual = self.topo
        while atual != None:
            print(atual.valor)
            atual = atual.proximo 
        print("---")

        