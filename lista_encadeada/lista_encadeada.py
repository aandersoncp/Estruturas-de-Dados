#import no

class No:

    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

class Lista:

    def __init__(self):
        self.primeiro = None

    def lista_vazia(self):
        if self.primeiro == None:
            print("Lista vazia")
            return True
        return False

    def inserir(self, valor):
        no = No(valor)
        if self.primeiro != None:
            no.proximo = self.primeiro
        self.primeiro = no
    
    def excluir_inicio(self):
        if self.lista_vazia():
            return None
        no = self.primeiro
        self.primeiro = no.proximo
        return no
    
    def buscar(self, valor):
        if self.lista_vazia():
            return
        no = self.primeiro
        while no != None and no.valor != valor:
            no = no.proximo
        return no
    
    def excluir(self, valor):
        if self.lista_vazia():
            return
        
        atual = self.primeiro
        while atual != None and atual.valor != valor:
            anterior = atual
            atual = atual.proximo
        if atual != None:
            if atual == self.primeiro:
                self.primeiro = atual.proximo
            else:
                anterior.proximo = atual.proximo
        return atual

    def imprimir(self):
        no = self.primeiro
        while no != None:
            print(no.valor)
            no = no.proximo
        print("---")


lista = Lista()
lista.inserir(2)
lista.inserir(3)
lista.inserir(5)
lista.imprimir()
lista.excluir(3)
lista.imprimir()
